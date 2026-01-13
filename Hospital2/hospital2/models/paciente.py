# -*- coding: utf-8 -*-

from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from datetime import datetime


class paciente(models.Model):
    _name = 'hospital2.paciente'
    _description = 'Esto es la descripcion del paciente'

    name = fields.Char(string="Nombre", required=True)
    apellidos = fields.Char(string="Apellidos")
    direccion = fields.Char(string="Dirección")
    poblacion = fields.Char(string="Población")
    provincia = fields.Char(string="Provincia")
    codigo_postal = fields.Char(string="Código Postal")
    telefono = fields.Char(string="Teléfono")
    fecha_nacimiento = fields.Date(string="Fecha de nacimiento")
    edad = fields.Integer(compute = '_age_calculate', store=True)

    ingreso_ids = fields.One2many(
        'hospital2.ingreso',
        'paciente_id',
        string='Ingresos'
    )


    @api.depends('fecha_nacimiento')
    def _age_calculate(self):
        today = fields.Date.today()
        for paciente in self:
            if paciente.fecha_nacimiento:
                paciente.edad = relativedelta(today, paciente.fecha_nacimiento).years
            else:
                paciente.edad=0




   
    
