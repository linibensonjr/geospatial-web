from django.contrib.gis.db import models

# Create your models here.

class  points(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField()
    address = models.CharField(max_length=100)
    description=models.CharField(max_length=200,blank=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'points'