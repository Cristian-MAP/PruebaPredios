from django.db.models import fields
import django_filters
from django_filters import filters
from .models import *

class PropietarioFilter(django_filters.FilterSet):
    class Meta:
        model = Propietario
        fields = {
            'nombre':['iexact'],
            'identificacion':['exact'],
        }

class PredioFilter(django_filters.FilterSet):
    class Meta:
        model = Predio
        exclude = ('matricula_mobiliaria')