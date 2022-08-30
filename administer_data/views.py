from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from administer_data.models import ClassInfo
from administer_data.serializers import ClassInfoSerializer


@api_view(['GET', 'POST'])
def classInfo_list(request, format=None):
    """
    List all code classInfos, or create a new classInfo.
    """
    if request.method == 'GET':
        classInfos = ClassInfo.objects.all()
        serializer = ClassInfoSerializer(classInfos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ClassInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def classInfo_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code classInfo.
    """
    try:
        classInfo = ClassInfo.objects.get(pk=pk)
    except ClassInfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ClassInfoSerializer(classInfo)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ClassInfoSerializer(classInfo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        classInfo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)