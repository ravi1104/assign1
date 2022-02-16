from django.shortcuts import render
from django.http import HttpResponse
from .models import Alldata
from .serializers import AlldataSerializer
from rest_framework.renderers import JSONRenderer



def index(request):
    ald=Alldata.objects.all()
    serializer=AlldataSerializer(ald,many=True)
    json_data=JSONRenderer().render(serializer.data)

    return HttpResponse(json_data,content_type='application/json')
def apidata(request,pk):
    ald=Alldata.objects.get(id=pk)
    serializer=AlldataSerializer(ald)
    json_data=JSONRenderer().render(serializer.data)

    return HttpResponse(json_data,content_type='application/json')