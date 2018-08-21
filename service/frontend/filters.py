import django_filters
from rest_framework import serializers

from service.backends.resource.models.channel import Video


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'


class VideoFilter(django_filters.FilterSet):
    sort = django_filters.OrderingFilter(fields=('created_at',))

    class Meta:
        model = Video
        fields = ['name', ]
