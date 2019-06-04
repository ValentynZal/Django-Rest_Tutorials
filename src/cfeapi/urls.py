"""cfeapi URL Configuration
"""
from django.conf.urls import url
from django.contrib import admin

from updates.views import json_example_view, JsonCBV, JsonCBV2, SerializedDetailView, SerializedListView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^json/example', json_example_view),
    url(r'^json/cbv', JsonCBV.as_view()),
    url(r'^json/cbv2', JsonCBV2.as_view()),
    url(r'^json/serialized/detail', SerializedDetailView.as_view()), 
    url(r'^json/serialized/list', SerializedListView.as_view()),     
]
