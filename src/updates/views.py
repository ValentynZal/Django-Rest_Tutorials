import json
from django.views.generic import View
from django.http import JsonResponse, HttpResponse
from cfeapi.mixins import JsonResponseMixin
from django.core.serializers import serialize
from .models import Update as UpdateModel


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
        obj = UpdateModel.objects.get(id=1)
        json_data = obj.serialize()
        return HttpResponse(json_data, content_type='application/json')


class SerializedListView(View):
    def get(self, request, *args, **kwargs):
        qs = UpdateModel.objects.all()
        json_data = UpdateModel.objects.all().serialize()
        return HttpResponse(json_data, content_type='application/json')
