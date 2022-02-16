from rest_framework import serializers

from versatileimagefield.serializers import VersatileImageFieldSerializer

from .models import Alldata


class AlldataSerializer(serializers.ModelSerializer):
  
    photo = VersatileImageFieldSerializer(
        sizes='photodata'
    )

    class Meta:
        model = Alldata
        fields = ('name','length','latitude','photo')
