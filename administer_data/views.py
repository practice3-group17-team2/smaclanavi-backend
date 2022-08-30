from administer_data.models import ClassInfo
from administer_data.serializers import ClassInfoSerializer
from rest_framework import generics


class ClassInfoList(generics.ListCreateAPIView):
    queryset = ClassInfo.objects.all()
    serializer_class = ClassInfoSerializer


class ClassInfoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClassInfo.objects.all()
    serializer_class = ClassInfoSerializer