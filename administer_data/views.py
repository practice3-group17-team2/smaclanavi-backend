# from administer_data.models import ClassInfo, Review, UpcomingLecInfos
# from administer_data.serializers import ClassInfoSerializer, ReviewSerializer, UpcomingLecInfoSerializer
from administer_data import models, serializers
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'classinfos':
        reverse('classinfo-list', request=request, format=format),
        'reviews':
        reverse('review-list', request=request, format=format),
        'lecinfos':
        reverse('lecinfo-list', request=request, format=format)
    })

class ClassInfoViewSet(viewsets.ModelViewSet):
    queryset = models.ClassInfo.objects.all()
    serializer_class = serializers.ClassInfoSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer


class UpcomingLecInfoViewSet(viewsets.ModelViewSet):
    queryset = models.UpcomingLecInfos.objects.all()
    serializer_class = serializers.UpcomingLecInfoSerializer
