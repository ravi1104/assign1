from rest_framework import serializers

from versatileimagefield.serializers import VersatileImageFieldSerializer

from .models import Alldata


class AlldataSerializer(serializers.ModelSerializer):
  
    photo = VersatileImageFieldSerializer(
        sizes='photodata'
    )

    class Meta:
        model = Alldata
        fields = ('name','species','weight','length','latitude','longitude','timestamp','photo')
    def create(self, validated_data):
        return Alldata.objects.create(**validated_data)