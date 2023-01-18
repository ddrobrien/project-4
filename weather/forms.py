from django.forms import ModelForm, TextInput
from .models import City


class CityForm(Model):
    class Meta:
        model = City
        fields = ['name']