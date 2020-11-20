from .models import MapData
from .serializers import MapDataSeriallizer
from rest_framework import viewsets
from django.shortcuts import render
from json import dumps
# Create your views here.
class MapDataViewSet(viewsets.ModelViewSet):
    queryset = MapData.objects.all().order_by('CameraID')
    serializer_class = MapDataSeriallizer


def home(request):
    alldetails=MapData.objects.all()
    serializer = MapDataSeriallizer(alldetails, many=True)
    #print(serializer.data) 
    #dataJSON = dumps(alldetails)
    l=[] 
    for x in serializer.data:
        tmp=dict(x)
        l.append(tmp)
    dataJSON = dumps(l)
    return render(request, 'app/home.html',{"data":alldetails,"dataJson":dataJSON})


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
 