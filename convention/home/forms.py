from django import forms
from searchableselect.widgets import SearchableSelect
from models import Traveler

class TravelerForm(forms.ModelForm):
    class Meta:
        model = Traveler
        exclude = ()
        widgets = {
            'cities_visited': SearchableSelect(model='cities.City', search_field='name', limit=10)
        }