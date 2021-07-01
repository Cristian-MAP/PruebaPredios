from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, TemplateView, DetailView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView

from .models import Predio,Propietario
from .forms import ActualizarPredioForm, ActualizarPropietarioForm, PredioForm, PropietarioForm
from .filters import *

class Inicio(TemplateView):
    """Clase para mostrar el template de inicio"""
    template_name = 'index.html'

class ListarPredios(ListView):
    """Clase para lista de predios"""
    model = Predio
    template_name = 'predios/listar_predios.html'

    def get_context_data(self, **kwargs):
        """Método que filtra y envía los predios según se haya especificado"""
        context = super().get_context_data(**kwargs)
        context['filter'] = PredioFilter(self.request.GET, queryset=self.get_queryset())
        return context

class AgregarPredio(SuccessMessageMixin, CreateView):
    """Clase para Agregar predio. Envía un mensaje si se agrega un predio"""
    model = Predio
    form_class = PredioForm
    template_name = 'predios/agregar_predio.html'
    success_url = reverse_lazy('predios:listar_predios')
    success_message = "El predio ha sido agregado"

class ActualizarPredio(SuccessMessageMixin,UpdateView):
    """Clase para actualizar un predio. Envía un mensaje si actualiza un predio"""
    model = Predio
    form_class = ActualizarPredioForm
    template_name = 'predios/actualizar_predio.html'
    success_url = reverse_lazy('predios:listar_predios')
    success_message = "El predio ha sido actualizado"

class EliminarPredio(DeleteView):
    """Clase que eliminar un predio"""
    model = Predio
    success_url = reverse_lazy('predios:listar_predios')

class PredioDetalle(DetailView):
    """Clase que muestra los detalles de un predio"""
    model = Predio
    template_name = 'predios/predio_detalle.html'

class ListarPropietarios(ListView):
    """Clase que enlista los propietarios"""
    model = Propietario
    template_name = 'propietarios/listar_propietarios.html'
   
    def get_context_data(self, **kwargs):
        """Método que envía y filtra los propietarios según se haya especificado"""
        context = super().get_context_data(**kwargs)
        context['filter'] = PropietarioFilter(self.request.GET, queryset=self.get_queryset())
        return context

class AgregarPropietario(SuccessMessageMixin, CreateView):
    """Clase que agrega propietarios. Envía mensajes si se agrega un propietario"""
    model = Propietario
    form_class = PropietarioForm
    template_name = 'propietarios/agregar_propietario.html'
    success_url = reverse_lazy('predios:listar_propietarios')
    success_message = 'El propietario ha sido agregado'

class ActualizarPropietario(SuccessMessageMixin,UpdateView):
    """Clase que actualiza propietarios. Envía mensaje si se actualiza un propietario"""
    model = Propietario
    form_class = ActualizarPropietarioForm
    template_name = 'propietarios/actualizar_propietario.html'
    success_url = reverse_lazy('predios:listar_propietarios')
    success_message = 'El propietario ha sido actualizado'

class EliminarPropietario(DeleteView):
    """Clase que Elimina un propietario"""
    model = Propietario
    success_url = reverse_lazy('predios:listar_propietarios')

class PropietarioDetalle(DetailView):
    """Clase que muestra los detalles de un propietario"""
    model = Propietario
    template_name = 'propietarios/propietario_detalle.html'