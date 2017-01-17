__author__ = 'sara'

from django.views.generic import View
from django.shortcuts import render


class WebUI(View):

    def get(self, request):
        return render(request, 'web.html')

    def post(self, request, webID):
        pass