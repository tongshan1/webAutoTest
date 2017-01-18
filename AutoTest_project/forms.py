__author__ = 'sara'

from django import forms
from .models import browser


class Form(forms.Form):

    website = forms.CharField(max_length=70, widget=forms.TextInput)
    test_cases = forms.CharField(max_length=100, widget=forms.TextInput)
    test_user = forms.CharField(widget=forms.TextInput)
    email = forms.EmailField(widget=forms.TextInput)
    browser = forms.ChoiceField(widget=forms.ChoiceField, queryset=browser.objects.all())