from .models import *
import django_filters

class VideoFilter(django_filters.FilterSet):

    class Meta:
        model = Video
        fields = ['type','duration','category']