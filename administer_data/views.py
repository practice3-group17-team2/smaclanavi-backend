from administer_data.models import ClassInfo, Review
from administer_data.serializers import ClassInfoSerializer, ReviewSerializer
from rest_framework import generics


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
