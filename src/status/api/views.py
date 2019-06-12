from rest_framework import generics, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import StatusSerializers
from status.models import Status

    
class StatusAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = []
    authentication_classe = []   
    serializer_class = StatusSerializers

    def get_queryset(self):
        qs = Status.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class StatusDetailAPIView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.RetrieveAPIView):
    permission_classes = []
    authentication_classe = []   
    serializer_class = StatusSerializers
    queryset = Status.objects.all()    

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)    

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs) 

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

