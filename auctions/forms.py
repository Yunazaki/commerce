from django import forms

class NewListingForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    image = forms.ImageField()
    date_listed = forms.DateTimeField()