from django.contrib import admin
from django.urls import path, include

from .views import *

admin.site.index_title = 'TM Plumbing'
admin.site.site_header = 'TM Plumbing'

app_name = "base"

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]
