from administer_data import models, serializers

from rest_framework import status
from rest_framework import viewsets
from rest_framework.exceptions import APIException
from rest_framework.exceptions import NotFound
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


class BadRequest(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "bad request"
    default_code = "bad_request"


class CatchExceptionViewSet(viewsets.ModelViewSet):

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except Exception as e:
            raise BadRequest(detail=e.args)

    def update(self, request, *args, **kwargs):
        try:
            return super().update(request, *args, **kwargs)

        # except models.Lecture.DoesNotExist as e:
        #     raise NotFound(detail=e.args)
        except Exception as e:
            raise BadRequest(detail=e.args)


class ClassInfoViewSet(CatchExceptionViewSet):
    queryset = models.ClassInfo.objects.all()
    serializer_class = serializers.ClassInfoSerializer


class ReviewViewSet(CatchExceptionViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer


class UpcomingLecInfoViewSet(CatchExceptionViewSet):
    queryset = models.UpcomingLecInfos.objects.all()
    serializer_class = serializers.UpcomingLecInfoSerializer


class LecScheduleViewSet(CatchExceptionViewSet):
    queryset = models.LecSchedule.objects.all()
    serializer_class = serializers.LecScheduleSerializer
