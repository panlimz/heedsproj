from django.contrib import admin
from whereapp.models import Place, Search, Searchdate

# Register your models here.
admin.site.register(Place)
admin.site.register(Search)
admin.site.register(Searchdate)