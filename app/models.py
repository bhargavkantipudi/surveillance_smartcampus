from django.db import models

# Create your models here.
"""class StudentInfo(models.Model):
    pinno= models.CharField(max_length=70, blank=False, primary_key=True)
    name = models.CharField(max_length=70, blank=False, default='')
    age = models.CharField(max_length=70, blank=False, default='')
    year = models.CharField(max_length=70, blank=False, default='')


class healthdata(models.Model):
    userid = models.ForeignKey(StudentInfo,on_delete=models.CASCADE)
    datatype=models.CharField(max_length=70, blank=False, default='')
    value=models.IntegerField()"""
class MapData(models.Model):
    CameraID=models.CharField(max_length=70, blank=False, default="")
    Camera_Name=models.CharField(max_length=70, blank=False, default='')
    Latitude = models.DecimalField(max_digits=9, decimal_places=6)
    Longitude = models.DecimalField(max_digits=9, decimal_places=6)
    Src = models.CharField(max_length=200,default="")

    