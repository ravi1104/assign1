from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .models import Alldata
from .serializers import AlldataSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser



def api_alldata(request):
    if request.method=="GET":
        ald=Alldata.objects.all()
        serializer=AlldataSerializer(ald,many=True)

        return JsonResponse(serializer.data,safe=False)

    if request.method=="POST":
        data=JSONParser().parse(request)
        serializer=AlldataSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.data,status=400)

def api_listdata(request,pk):
    data=Alldata.objects.get(id=pk)
    serializer=AlldataSerializer(data)


    return JsonResponse(serializer.data)
