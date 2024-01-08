from django import forms

class NewListingForm(forms.Form):
    title = forms.CharField(max_length=64)
    description = forms.CharField()
    image = forms.ImageField()
    date_listed = forms.DateTimeField()