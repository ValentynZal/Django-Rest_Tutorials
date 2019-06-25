from rest_framework import generics, mixins, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import StatusSerializers
from status.models import Status
from django.shortcuts import get_object_or_404
from updates.api.utils import is_json
from json import loads, dumps
from rest_framework.authentication import SessionAuthentication
from accounts.api.permissions import *


class StatusDetailAPIView(
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.RetrieveAPIView
):
    # comment if you use default classes
    # permission_classes = []
    # authentication_classe = []   
    # or
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = StatusSerializers
    queryset = Status.objects.all()    
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)    

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs) 

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class StatusAPIView(
    mixins.CreateModelMixin, 
    generics.ListAPIView
):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = StatusSerializers
    passed_id = None

    def get_queryset(self):
        request = self.request
        qs = Status.objects.all()
        query = request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

