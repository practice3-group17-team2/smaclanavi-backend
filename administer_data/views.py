from administer_data import models, serializers

from rest_framework import status
from rest_framework import viewsets
from rest_framework.exceptions import APIException
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


class BadRequest(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "bad request"
    default_code = "bad_request"


class UpcomingLecInfoViewSet(viewsets.ModelViewSet):
    queryset = models.UpcomingLecInfos.objects.all()
    serializer_class = serializers.UpcomingLecInfoSerializer

    def create(self, request, *args, **kwargs):
        """
        serializerのcreateから渡されるcreatedを取得して
        新規作成か取得しただけかでhttp responseを場合分けしたかったが、取得出来ず諦めた
        以下はCreateModelMixinをそのままコピペしただけ
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def update(self, request, *args, **kwargs):
        """
        serializerが送出したvalue errorによってステータスコードを変更
        """
        try:
            return super().update(request, *args, **kwargs)
        except ValueError as e:
            raise BadRequest(detail=e.args)


class LecScheduleViewSet(viewsets.ModelViewSet):
    queryset = models.LecSchedule.objects.all()
    serializer_class = serializers.LecScheduleSerializer
