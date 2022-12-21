from django.contrib import admin
from django.contrib.gis import admin
from .models import points

# Register your models here.
class AddPointAdmin(admin.GISModelAdmin):
    default_zoom = 14
admin.site.register(points, AddPointAdmin)