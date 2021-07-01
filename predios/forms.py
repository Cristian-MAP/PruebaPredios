from django import forms
from .models import Predio, Propietario

class PredioForm(forms.ModelForm):
    """Clase que se encarga del form de agregar predio"""
    class Meta:
        model = Predio
        fields = '__all__'

class ActualizarPredioForm(forms.ModelForm):
    """Clase que se encarga del form de actualizar predio """
    class Meta:
        model = Predio
        fields = 'direccion','cedula_catastral','tipo_predio'

class PropietarioForm(forms.ModelForm):
    """Clase que se encarga del form de agregar proppietario"""
    class Meta:
        model = Propietario
        fields = '__all__'

class ActualizarPropietarioForm(forms.ModelForm):
    """Clase que se encarga del form de actualizar propietario"""
    class Meta:
        model = Propietario
        fields = 'nombre','role','predios'