__author__ = 'sara'

from django import forms
from .models import browser, Test_user

browser_list = browser.objects.all()
browser_choice = []

for browser in browser_list:
    tmp = (browser.id, browser.browser)
    browser_choice.append(tmp)

test_user_list = Test_user.objects.all()
test_user_choice = []

for test_user in test_user_list:
    tmp = (test_user.id, test_user.user_name)
    test_user_choice.append(tmp)


class TestWebForm(forms.Form):
    website = forms.CharField(max_length=70, widget=forms.TextInput(attrs={'class': 'form-control round-input'}))
    test_cases = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control round-input'}))

    test_user_input = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control round-input'}),
                                choices=tuple(test_user_choice))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control round-input'}))

    browser_input = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control round-input'}),
                                choices=tuple(browser_choice))

    # class Meta:
    #     model = Test_web
    #     fields = ('website', 'test_cases', 'test_user', 'desc', 'email', 'browser_input')
