from django.contrib import admin

# Register your models here.

from .models import Test_web, Test_user, browser

admin.site.register(Test_web)
admin.site.register(Test_user)
admin.site.register(browser)
