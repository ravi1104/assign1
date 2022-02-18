
from django.http import JsonResponse
from .models import Alldata
from .serializers import AlldataSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets

@csrf_exempt
def api_alldata(request):
    if request.method=="GET":
        ald=Alldata.objects.order_by('-timestamp')
        serializer=AlldataSerializer(ald,many=True)

        return JsonResponse(serializer.data,safe=False)

def api_listdata(request,pk):
    data=Alldata.objects.get(id=pk)
    serializer=AlldataSerializer(data)
    return JsonResponse(serializer.data)

class Imageuploadviewset(viewsets.ModelViewSet):
    queryset =Alldata.objects.all()
    serializer_class = AlldataSerializer

