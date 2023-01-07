from rest_framework import serializers
from .models import posts


class GetAllInfo(serializers.ModelSerializer):
    class Meta:
        model = posts
        fields = ('__all__')


class PostSerializer(serializers.Serializer):
    title1 = serializers.CharField(max_length=255)
    desciption1 = serializers.CharField(max_length=255)
