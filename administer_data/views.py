from administer_data import models, serializers
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'class_infos':
        reverse('classinfo-list', request=request, format=format),
        'reviews':
        reverse('review-list', request=request, format=format),
        'lecinfos':
        reverse('lec_info-list', request=request, format=format),
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


class LecScheduleViewSet(viewsets.ModelViewSet):
    queryset = models.LecSchedule.objects.all()
    serializer_class = serializers.LecScheduleSerializer
