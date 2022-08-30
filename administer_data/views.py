from administer_data.models import ClassInfo
from administer_data.serializers import ClassInfoSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ClassInfoList(APIView):
    """
    List all code classInfos, or create a new classInfo.
    """
    def get(self, request, format=None):
        all_class_info = ClassInfo.objects.all()
        serializer = ClassInfoSerializer(all_class_info, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ClassInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ClassInfoDetail(APIView):
    """
    Retrieve, update or delete a class_info instance.
    """
    def get_object(self, pk):
        try:
            return ClassInfo.objects.get(pk=pk)
        except ClassInfo.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        class_info = self.get_object(pk)
        serializer = ClassInfoSerializer(class_info)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        class_info = self.get_object(pk)
        serializer = ClassInfoSerializer(class_info, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        class_info = self.get_object(pk)
        class_info.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)