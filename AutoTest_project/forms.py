__author__ = 'sara'

from django import forms
from .models import browser

browser_list = browser.objects.all()
browser_choice =[]

for browser in browser_list:
    tmp = (browser.id, browser.browser)
    browser_choice.append(tmp)


class TestWebForm(forms.Form):

    website = forms.CharField(max_length=70, widget=forms.TextInput(attrs={'class': 'form-control round-input'}))
    test_cases = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control round-input'}))
    test_user = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control round-input'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control round-input'}))
    browser_input = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control round-input'}),
                                choices=tuple(browser_choice))
