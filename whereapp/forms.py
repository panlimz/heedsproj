from django import forms
from whereapp.models import Place, Search, Searchdate

#Creating the place form using the place model 
class PlaceForm(forms.ModelForm):

    class Meta:
        model = Place
        fields = ['name', 'latitude', 'longitude', 'date']
        labels = {
            'name': '',
            'latitude': '',
            'longitude': '',
            'date': 'Visit Date (mm/dd/aaaa)',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Place Name'}),
            'latitude': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Place Latitude'}),
            'longitude': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Place Longitude'}),
            'date': forms.DateInput(format='%m/%d/%Y', attrs={'class':'form-control'}),
        }

class SearchForm(forms.ModelForm):
    
    class Meta:
        model = Search
        fields = ('region',)
        labels = {
            'region': '',
        }
        widgets = {
            'region': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Region'}),
        }
class SearchdateForm(forms.ModelForm):

    class Meta:
        model = Searchdate
        fields = ('searchdate',)
        labels = {
            'searchdate': '',
        }
        widgets = {
            'searchdate': forms.DateInput(format='%m/%d/%Y', attrs={'class':'form-control', 'placeholder': 'Date'}),
        }