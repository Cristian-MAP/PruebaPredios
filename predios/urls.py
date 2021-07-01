from django.urls import path
from .views import *

urlpatterns = [
    path('agregar_predio/', AgregarPredio.as_view(), name='agregar_predio'),
    path('listar_predios/', ListarPredios.as_view(), name='listar_predios'),
    path('actualizar_predio/<int:pk>', ActualizarPredio.as_view(), name='actualizar_predio'),
    path('eliminar_predio/<int:pk>', EliminarPredio.as_view(), name='eliminar_predio'),
    path('detalle_predio/<int:pk>', PredioDetalle.as_view(), name='detalle_predio'),

    path('agregar_propietario/', AgregarPropietario.as_view(), name='agregar_propietario'),
    path('listar_propietarios/', ListarPropietarios.as_view(), name='listar_propietarios'),
    path('actualizar_propietario/<int:pk>', ActualizarPropietario.as_view(), name='actualizar_propietario'),
    path('eliminar_propietario/<int:pk>', EliminarPropietario.as_view(), name='eliminar_propietario'),
    path('detalle_propietario/<int:pk>', PropietarioDetalle.as_view(), name='detalle_propietario'),

    path('', Inicio.as_view(), name='inicio')
]
