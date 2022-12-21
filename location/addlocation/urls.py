from addlocation.views import addpoint,viewpoints,allpoints
from django.urls import path

urlpatterns = [
    path('addlocation',addpoint,name='addpoint'),
    path('viewpoints',viewpoints,name='viewpoints'),
    path('allpoints',allpoints,name='allpoints'),
]
