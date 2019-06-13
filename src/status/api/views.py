from rest_framework import generics, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import StatusSerializers
from status.models import Status
from django.shortcuts import get_object_or_404
from updates.api.utils import is_json
from json import loads, dumps

    
class StatusAPIView(
    mixins.CreateModelMixin, 
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,    
    generics.ListAPIView
):
    permission_classes = []
    authentication_classe = []   
    serializer_class = StatusSerializers
    passed_id = None

    def get_queryset(self):
        request = self.request
        qs = Status.objects.all()
        query = request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def get_object(self):
        request = self.request
        passed_id = request.GET.get('id', None) or self.passed_id
        queryset = self.get_queryset()
        obj = None
        if passed_id is not None:
            obj = get_object_or_404(queryset, id=passed_id)
            self.check_object_permissions(request, obj)
        return obj

    def perform_destroy(self, instance):
        if instance is not None:
            return instance.delete()
        return None
        
    def get(self, request, *args, **kwargs):
        url_passed_id = request.GET.get('id', None)
        json_data = {}
        if is_json(request.body):
            json_data = loads(request.body)
        new_passed_id = json_data.get('id', None)
        passed_id = url_passed_id or new_passed_id or None
        self.passed_id = passed_id
        print(request.body)
        if passed_id is not None:        
            return self.retrieve(request, *args, **kwargs)  
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        url_passed_id = request.GET.get('id', None)
        json_data = {}
        if is_json(request.body):
            json_data = loads(request.body)
        new_passed_id = json_data.get('id', None)
        passed_id = url_passed_id or new_passed_id or None
        self.passed_id = passed_id
        print(request.body)
        return self.update(request, *args, **kwargs) 

    def patch(self, request, *args, **kwargs):
        url_passed_id = request.GET.get('id', None)
        json_data = {}
        if is_json(request.body):
            json_data = loads(request.body)
        new_passed_id = json_data.get('id', None)
        passed_id = url_passed_id or new_passed_id or None
        self.passed_id = passed_id
        print(request.body)
        return self.update(request, *args, **kwargs) 

    def delete(self, request, *args, **kwargs):
        url_passed_id = request.GET.get('id', None)
        json_data = {}
        if is_json(request.body):
            json_data = loads(request.body)
        new_passed_id = json_data.get('id', None)
        passed_id = url_passed_id or new_passed_id or None
        self.passed_id = passed_id
        print(request.body)
        return self.destroy(request, *args, **kwargs)


# class StatusDetailAPIView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.RetrieveAPIView):
#     permission_classes = []
#     authentication_classe = []   
#     serializer_class = StatusSerializers
#     queryset = Status.objects.all()    

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)    

#     def patch(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs) 

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

