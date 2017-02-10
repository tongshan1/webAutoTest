"""webAutoTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from AutoTest_project import views as views

urlpatterns = [
    # url(r'^$', views.index),
    url(r'^web/', views.WebView.as_view(), name='web'),
    url(r'^web_detail/edit/(?P<Test_id>\d+)/$', views.WebEditView.as_view(), name="web_edit"),
    url(r'^web/fun/(?P<Test_id>\d+)/$', views.WebEditView.as_view(), name="web_run"),
    url(r'^admin/', admin.site.urls),
]
