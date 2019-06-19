from rest_framework import serializers
from status.models import Status


class StatusSerializers(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = [
            'id',
            'user',
            'content',
            'image'
        ]
        read_only_fields = ['user']
        
    # def validate_content(self, value):
    #     if len(value) > 10:
    #         raise serializers.ValidationError("Content is too long")
    #     return value

    def validate(self, data):
        content = data.get('content', None)
        image = data.get('image', None)
        if content == "":
            contect = None
        if content is None and image is None:
            raise serializers.ValidationError('Content or image is required')   
        return data             