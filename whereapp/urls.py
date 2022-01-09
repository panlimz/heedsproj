from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addplaces', views.addplaces, name='addplaces'),
    path('editplace/<place_id>', views.editplace, name='editplace'),
    path('deleteplace/<place_id>', views.deleteplace, name='deleteplace'),
    path('placeslist', views.placeslist, name='placeslist'), 
    path('place/<place_id>', views.place, name='place'),
    path('findplacesregion', views.findplacesregion, name='findplacesregion'),
    path('findplacesdate', views.findplacesdate, name='findplacesdate'),
]
