from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import User, Auctions, Bids, Comments
from .forms import NewListingForm

def index(request):
    auctions = Auctions.objects.all()
    
    return render(request, "auctions/index.html", {
        "auctions": auctions
    })

@login_required
def watchlist(request, username):
    user = User.objects.get(username=username)
    watchlist = user.watchlist.all()

    return render(request, "auctions/watchlist.html", {
        "user": user,
        "watchlist": watchlist
    })


@login_required
def create_listing(request):
    if request.method == "POST":
        form = NewListingForm(request.POST, request.FILES)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()

            return redirect("index")
        else:
            return render(request, "auctions/create_listing.html", {
                "form": form
            })

    return render(request, "auctions/create_listing.html", {
        "form": NewListingForm()
    })


def listing_page(request, item_id):
    item = get_object_or_404(Auctions, pk=item_id)
    bids = Bids.objects.filter(auction=item_id)
    comments = Comments.objects.filter(auction=item_id)
    winner = bids.order_by('-timestamp').first()
    
    return render(request, "auctions/listing_page.html", {
        "item": item,
        "bids": bids,
        "comments": comments,
        "winner": winner
    })


@login_required
def place_bid(request, item_id):
    item = get_object_or_404(Auctions, pk=item_id)

    if request.method == "POST":
        amount = request.POST["bid_amount"]

        if float(amount) > item.bid:
            print("success")
            new_bid = Bids.objects.create(auction=item, bidder=request.user, amount=amount)
            
            item.bid = new_bid.amount
            item.save()
            
            messages.success(request, "Bid placed successfully!")
            return redirect(reverse('listing_page', kwargs={'item_id': item_id}))
            
        print("error")
        messages.error(request, "Invalid bid amount")

    return redirect(reverse('listing_page', kwargs={'item_id': item_id}))


@login_required
def close_bid(request, item_id):
    item = get_object_or_404(Auctions, pk=item_id)

    if request.method == "POST":
        if request.user == item.user:
            item.is_active = False
            item.save()

            messages.success(request, "Bid closed successfully")
            return redirect(reverse('listing_page', kwargs={'item_id': item_id}))    

        messages.error(request, "An error occurred")

    return redirect(reverse('listing_page', kwargs={'item_id': item_id}))


@login_required
def make_comment(request, item_id):
    item = get_object_or_404(Auctions, pk=item_id)

    if request.method == "POST":
        comment = request.POST["comment"]

        Comments.objects.create(auction=item, user=request.user, comment=comment)
        return redirect(reverse('listing_page', kwargs={'item_id': item_id}))


@login_required
def add_watchlist(request, item_id):
    user = request.user
    item = get_object_or_404(Auctions, pk=item_id)

    if item not in user.watchlist.all():
        messages.success(request, "Successfully added to watchlist")
        user.watchlist.add(item)

    return redirect(reverse('listing_page', kwargs={'item_id': item_id}))


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
