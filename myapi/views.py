from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .models import Alldata
from .serializers import AlldataSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from rest_flex_fields.views import FlexFieldsModelViewSet

@csrf_exempt
def api_alldata(request):
    if request.method=="GET":
        ald=Alldata.objects.all()
        serializer=AlldataSerializer(ald,many=True)

        return JsonResponse(serializer.data,safe=False)

    if request.method=="POST":
        class ImageViewSet(FlexFieldsModelViewSet):
            serializer_class = AlldataSerializer

            queryset = Alldata.objects.all()

        return HttpResponse(status=201)


def api_listdata(request,pk):
    data=Alldata.objects.get(id=pk)
    serializer=AlldataSerializer(data)


    return JsonResponse(serializer.data)
