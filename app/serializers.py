from rest_framework import serializers

from .models import MapData

class MapDataSeriallizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MapData
        fields = ('CameraID', 'Camera_Name','Latitude','Longitude',"Src")