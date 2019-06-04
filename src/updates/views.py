import json
from django.views.generic import View
from django.http import JsonResponse, HttpResponse
from cfeapi.mixins import JsonResponseMixin
from django.core.serializers import serialize
from .models import Update


def json_example_view(request):
    '''
    URI -- for REST API
    GET -- Retrieve
    '''
    data = {
        "count": 100,
        "content": "Update EPTA"
    }
    # return JsonResponse(data)
    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type='application/json')


class JsonCBV(View):
    def get(self, request, *args, **kwargs):
        data = {
            "count": 100,
            "content": "Update EPTA"
        }
        return JsonResponse(data)

    
class JsonCBV2(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):
        data = {
            "count": 100,
            "content": "Update EPTA"
        }
        return self.render_to_json_response


class SerializedDetailView(View):
    def get(self, request, *args, **kwargs):
        obj = Update.objects.get(id=1)
        data = serialize("json", [obj, ], fields=('user', 'content'))
        json_data = data
        # data = {
        #     "user": obj.user.username,
        #     "content": obj.content
        # }
        # json_data = json.dumps(data)
        return HttpResponse(json_data, content_type='application/json')


class SerializedListView(View):
    def get(self, request, *args, **kwargs):
        queryset = Update.objects.all()
        data = serialize("json", queryset, fields=('user', 'content'))
        json_data = data
        # data = {
        #     "user": obj.user.username,
        #     "content": obj.content
        # }
        # json_data = json.dumps(data)
        return HttpResponse(json_data, content_type='application/json')
