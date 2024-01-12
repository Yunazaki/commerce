from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("listing/create", views.create_listing, name="create_listing"),
    path("listing/<int:item_id>", views.listing_page, name="listing_page"),
    path("listing/<int:item_id>/bid", views.place_bid, name="place_bid"),
    path("listing/<int:item_id>/comment", views.make_comment, name="make_comment")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)