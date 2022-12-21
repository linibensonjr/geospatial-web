from django.shortcuts import render

from .models import points
from django.contrib.gis.geos import Point

from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.contrib.gis.db.models.functions import Distance


@csrf_exempt
def addpoint(request):
    if request.method =='POST':
        name=request.POST['name']
        lat=float(request.POST['latitude'])
        long=float(request.POST['longitude'])
        desc=request.POST['description']
        location=Point(long,lat,srid=4326)
        newpoint = points(name=name,location=location,description=desc)
        newpoint.save()
        
    return render(request,'addpoint.html')

@csrf_exempt
def viewpoints(request):
    if request.method=='POST':
        lat1=float(request.POST['latitude'])
        long1=float(request.POST['longitude'])
        user_location = Point(long1,lat1,srid=4326)
        queryset = points.objects.annotate(distance=Distance("location", user_location)).order_by("distance")[0:1] 
        print('Query Set', queryset)
        names=[i for i in queryset]
        name=[i.name for i in names]
        lo=[i.location for i in names]
        xy=[[j for j in i] for i in lo]
        lat=[i[1] for i in xy]
        long=[i[0] for i in xy]
        return render(request,'showpoints.html',{'allpoints':queryset,'name':name,'lat':lat,'long':long})
    return render(request,'map.html')


def allpoints(request):
    allpoints=points.objects.all()
    names=[i for i in allpoints]
    name=[i.name for i in names]
    lo=[i.location for i in names]
    xy=[[j for j in i] for i in lo]
    lat=[i[1] for i in xy]
    long=[i[0] for i in xy]
    return render(request,'allpoints.html',{'allpoints':allpoints,'name':name,'lat':lat,'long':long})