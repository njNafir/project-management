from django.contrib import admin
from django.urls import re_path
from .views import project_page, single_project, add_project #, ProductDownloadView #, search_project # ProjectAddView # add_project

urlpatterns = [
    re_path(r'^project$', project_page, name='project_page'),
    # re_path(r'^project?search=(?P<search>[-\w]+)$', search_project, name='search_project'),
    re_path(r'^project/(?P<group_number>\d+)/(?P<pk>\d+)$', single_project, name='single_project'),
    # re_path(r'^project/download/(?P<group>\d+)/(?P<pk>\d+)$', ProductDownloadView.as_view(), name='ProductDownloadView'),
    re_path(r'^project/new$', add_project, name='add_project'),
]