from django.contrib import admin
from django.urls import re_path

from pro.views import home_page, about_page

urlpatterns = [
    re_path(r'^$', home_page, name='home_page'),
    re_path(r'^about$', about_page, name='about_page'),
]