from administer_data.models import ClassInfo, Review
from administer_data.serializers import ClassInfoSerializer, ReviewSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'classinfo': reverse('classinfo-list', request=request, format=format),
        'reviews': reverse('review-list', request=request, format=format)
    })

class ClassInfoList(generics.ListCreateAPIView):
    queryset = ClassInfo.objects.all()
    serializer_class = ClassInfoSerializer

class ClassInfoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClassInfo.objects.all()
    serializer_class = ClassInfoSerializer


class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
