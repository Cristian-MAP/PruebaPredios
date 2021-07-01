from django.db import models

"""Un diccionario para diferenciar si un propietario es persona o empresa"""
PERSONA = 1
EMPRESA = 2

ROLE_CHOICES = (
    (PERSONA, 'Persona'),
    (EMPRESA, 'Empresa')
    ) 


"""Diccionario para diferenciar si un predio es urbano o rural"""
URBANO = 1
RURAL = 2

TIPO_PREDIO_CHOICES = (
    (URBANO, 'Urbano'),
    (RURAL, 'Rural')
    )

class Predio(models.Model):
    """Clase que representa un predio y tiene los datos de un predio"""
    matricula_mobiliaria = models.CharField('Matrícula inmobiliaria', primary_key=True, max_length=150, unique=True)
    cedula_catastral = models.CharField('Cédula catastral', max_length=100,unique=True)
    direccion = models.CharField('Dirección', null= False, max_length=150)
    tipo_predio = models.PositiveSmallIntegerField('Tipo de predio',choices = TIPO_PREDIO_CHOICES, blank=True, null=True, default=3)

    class Meta:
        verbose_name = ("Predio")
        verbose_name_plural = ("Predios")

    def __str__(self):
        return self.direccion

class Propietario(models.Model):
    """Clase que representa un propietario y tiene los datos de un propietario"""
    identificacion = models.CharField('Identificación', primary_key=True, max_length=50)
    nombre = models.CharField('Nombre del propietario',null=False,max_length=150)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True, default=3)
    predios = models.ManyToManyField(Predio)

    class Meta:
       verbose_name = ("Propietario")
       verbose_name_plural = ("Propietarios")

    def __str__(self):
        return self.nombre