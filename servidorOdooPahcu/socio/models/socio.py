# -*- coding: utf-8 -*-
from datetime import timedelta

from odoo import models, fields, api
from odoo.exceptions import ValidationError



#Definimos modelo Liga Equipo, que almacenara información de cada equipo
class Socio(models.Model):

    #Nombre y descripcion del modelo
    _name = 'socio'

    _description = 'Modelo par almacenar socios'

    #Parametros de ordenacion por defecto
    _order = 'nombre'

    #ATRIBUTOS

    #PARA CUANDO NO HAY UN ATRIBUTO LLAMADO NAME PARA MOSTRAR NOMBRE DE UN REGISTRO
    # https://www.odoo.com/es_ES/forum/ayuda-1/how-defined-display-name-in-custom-many2one-91657
    
    #Indicamos que atributo sera el que se usara para mostrar nombre.
    #Por defecto es "name", pero si no hay un atributo que se llama name, aqui lo indicamos
    #Aqui indicamos que se use el atributo "nombre"
    _rec_name = 'nombre'



    dni=fields.Char('DNI socio', required=True) 
    #Atributo nombre
    nombre = fields.Char('Nombre socio', required=True)
    apellidos = fields.Char('Apellidos socio', required=True)

    #Constraints de SQL del modelo
    _sql_constraints = [
        ('socio_uniq', 'UNIQUE (dni)', 'El dni de socio debe ser unico.')
    ]
