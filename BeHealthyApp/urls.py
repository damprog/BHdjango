from django.urls import re_path
from BeHealthyApp import views

urlpatterns=[
    re_path(r'^package/$', views.packageApi),
    re_path(r'^package/([0-9]+)$', views.packageApi)
]