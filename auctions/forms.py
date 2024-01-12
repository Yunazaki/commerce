from django import forms
from .models import Auctions

class NewListingForm(forms.ModelForm):
    class Meta:
        model = Auctions
        exclude = ["date_listed", "user", "is_active"]