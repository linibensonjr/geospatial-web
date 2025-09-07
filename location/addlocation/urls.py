from addlocation.views import addpoint,viewpoints,allpoints, home
from django.urls import path

urlpatterns = [
    path('', home, name='home'),
    path('addlocation',addpoint,name='addpoint'),
    path('viewpoints',viewpoints,name='viewpoints'),
    path('allpoints',allpoints,name='allpoints'),
]
