from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import StatusSerializers
from status.models import Status


class StatusListSearchAPIView(APIView):
    permission_classes = []
    authentication_classe = []

    def get(self, request, format=None):
        qs = Status.objects.all()
        serializer = StatusSerializers(qs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        qs = Status.objects.all()
        serializer = StatusSerializers()
        return Response(serializer.data)

    
class StatusAPIView(generics.ListAPIView):
    permission_classes = []
    authentication_classe = []   
    serializer_class = StatusSerializers

    def get_queryset(self):
        qs = Status.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs


class StatusCreateAPIView(generics.CreateAPIView):
    permission_classes = []
    authentication_classe = []   
    serializer_class = StatusSerializers
    queryset = Status.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class StatusDetailAPIView(generics.RetrieveAPIView):
    permission_classes = []
    authentication_classe = []   
    serializer_class = StatusSerializers
    queryset = Status.objects.all()    
    # lookup_field = 'id'  # slug


class StatusUpdateAPIView(generics.UpdateAPIView):
    permission_classes = []
    authentication_classe = []   
    serializer_class = StatusSerializers
    queryset = Status.objects.all()    


class StatusDeleteAPIView(generics.DestroyAPIView):
    permission_classes = []
    authentication_classe = []   
    serializer_class = StatusSerializers
    queryset = Status.objects.all()    