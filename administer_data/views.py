from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from administer_data.models import ClassInfo
from administer_data.serializers import ClassInfoSerializer

@csrf_exempt
def classinfo_list(request):
    """
    List all code administer_data, or create a new snippet.
    """
    if request.method == 'GET':
        administer_data = ClassInfo.objects.all()
        serializer = ClassInfoSerializer(administer_data, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ClassInfoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def classinfo_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = ClassInfo.objects.get(pk=pk)
    except ClassInfo.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ClassInfoSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ClassInfoSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)