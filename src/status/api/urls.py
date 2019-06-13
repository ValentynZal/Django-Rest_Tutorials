from django.conf.urls import url
from .views import (
    StatusAPIView,
    # StatusDetailAPIView,
)

urlpatterns = [
    url(r'^$', StatusAPIView.as_view()),
    # url(r'^(?P<pk>\d+)/$', StatusDetailAPIView.as_view()),            
]

# http://127.0.0.1:8000/api/status/ 
# http://127.0.0.1:8000/api/status/?id=5
# http://127.0.0.1:8000/api/status/?q=was