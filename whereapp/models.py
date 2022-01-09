from django.db import models
from datetime import datetime

#Creating the place model
class Place(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    date = models.DateField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name

#Creating search model
class Search(models.Model):
    region = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.region 

#Creating date search model
class Searchdate(models.Model):
    searchdate = models.DateField(default=datetime.now, blank=True)

    def __str__(self) -> str:
        return self.searchdate 
    
