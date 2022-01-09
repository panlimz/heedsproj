from datetime import datetime
from django.shortcuts import render, redirect
from whereapp.forms import PlaceForm, SearchForm, SearchdateForm
from whereapp.models import Place, Search, Searchdate
from django.http import HttpResponseRedirect
import folium
import geocoder

def index(request):
    
    placemap = folium.Map(location=[10, -12], zoom_start=2)
    placemap = placemap._repr_html_()
    context = {
        'placemap': placemap
    }
    return render(request, 'index.html', context)

def findplacesregion(request):
    #Searching for a region
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('findplacesregion')
    else:
        form = SearchForm()
    region = Search.objects.all().last()
    location = geocoder.osm(region)
    lat = location.lat
    lng = location.lng

    #Getting coordinate and name places
    placesname = Place.objects.values_list('name')
    placesnamelist = list(placesname)
    namelist = []
    for i in range(0, len(placesnamelist)):
        name_x = placesnamelist[i][0]
        namelist.append(name_x)

    placeslat = Place.objects.values_list('latitude')
    placeslatlist = list(placeslat)
    latlist = []
    for i in range(0, len(placeslatlist)):
        latp = float(placeslatlist[i][0])
        latlist.append(latp)
    
    placeslng = Place.objects.values_list('longitude')
    placeslnglist = list(placeslng)
    lnglist = []
    for i in range(0, len(placeslnglist)):
        lngp = float(placeslnglist[i][0])
        lnglist.append(lngp)

    #Creating the map
    placemap = folium.Map(location=[lat,lng], zoom_start=4)
    #Creating map markers
    for i in range(0, len(placesname)):
        folium.Marker([latlist[i],lnglist[i]], radius=20, tooltip='click for more', popup=namelist[i]).add_to(placemap)
    placemap = placemap._repr_html_()
    context = {
        'placemap': placemap,
        'form': form,
    }

    return render(request, 'findplacesregion.html', context)

#Searching according to a specific date
def findplacesdate(request):
    if request.method == 'POST':
        form = SearchdateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('findplacesdate')
    else:
        form = SearchdateForm()
    getsearchdate = Searchdate.objects.values_list('searchdate')
    searchdatelist = list(getsearchdate)
    placelist = Place.objects.all()
    
    print(searchdate)
    
    return render(request, 'findplacesdate.html', {'form': form, 'placelist': placelist, })

#Adding a Place
def addplaces(request):
    submitted = False
    if request.method == 'POST':
        form = PlaceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/addplaces?submitted=True')
    else:
        form = PlaceForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'addplaces.html', {'form': form, 'submitted': submitted})

#Editing a Place name
def editplace(request, place_id):
    place = Place.objects.get(pk=place_id)
    form = PlaceForm(request.POST or None, instance=place)
    form.fields['latitude'].widget.attrs['readonly']=True
    form.fields['longitude'].widget.attrs['readonly']=True
    form.fields['date'].widget.attrs['readonly']=True
    if form.is_valid():
        form.save()
        return redirect('placeslist')
    return render(request, 'editplace.html', {'place': place, 'form': form})

#Deleting a Place
def deleteplace(request, place_id):
    place = Place.objects.get(pk=place_id)
    place.delete()
    return redirect('placeslist')

#Listing the existent places
def placeslist(request):
    placeslist = Place.objects.order_by('pk')
    return render(request, 'placeslist.html', {'placeslist': placeslist})

#Showing a single place
def place(request, place_id):
    place = Place.objects.get(pk=place_id)
    return render(request, 'place.html', {'place': place}) 