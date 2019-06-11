"""
run file with: python manage.py shell
"""

# import json
from django.utils.six import BytesIO
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from status.api.serializers import StatusSerializers
from status.models import Status


''' Serialize a single object '''
obj = Status.objects.first()
serializer = StatusSerializers(obj)
serializer.data                                         # dictionary
# json_data1 = json.dumps(serializer.data)              # <class 'str'>
json_data = JSONRenderer().render(serializer.data)      # <class 'bytes'>
print(json_data)

# data1 = json.loads(json_data1)                       # dictionary 
stream = BytesIO(json_data)
data = JSONParser().parse(stream)                      # dictionary
print(data)

''' Serialize a queryset '''
qs = Status.objects.all()
serializer2 = StatusSerializers(qs, many=True)
serializer2.data                                         # list of OrderedDict
json_data2 = JSONRenderer().render(serializer2.data)      # <class 'bytes'>
print(json_data2)

stream2 = BytesIO(json_data2)
data2 = JSONParser().parse(stream2)                      # list of dictionaries
print(data2)

''' Create Obj '''
data = {'user': 1, 'content': 'was ist das?'}
create_obj_serializer = StatusSerializers(data=data)
create_obj_serializer.is_valid()
create_obj = create_obj_serializer.save()
print(create_obj)

''' Update Obj '''
obj = Status.objects.last()
data = {'user': 1, 'content': 'das ist shon'}
update_serializer = StatusSerializers(obj, data=data) 
update_serializer.is_valid()
update_serializer = update_serializer.save()
print(update_serializer.content)

''' Delete Obj '''
obj = Status.objects.first()
print(obj.delete())