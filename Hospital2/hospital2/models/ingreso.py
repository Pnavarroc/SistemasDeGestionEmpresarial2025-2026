# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date


class ingreso(models.Model):
    _name = 'hospital2.ingreso'
    _description = 'Esto es la descripcion del ingreso'
    _rec_name = 'paciente_id'

    paciente_id = fields.Many2one(
        'hospital2.paciente',
        string="Paciente",
        required=True
    )
    #campos related importantes . Sirve para mostrar informacion de modelos relacionados sin duplicar datos.
    #Ejemplo
    especialidad_medico = fields.Char(
    string="Especialidad médico",
    related='medico_id.especialidad',
    store=True
)
    #Asi esa informacion la podemos poner en la vista de ingreso si sin necesidad de duplicar datos.


    medico_id = fields.Many2one(
        'hospital2.medico',
        string="Médico",
        required=True
    )

    numero_habitacion = fields.Char(string="Habitación", required=True)
    fecha_ingreso = fields.Date(string="Fecha de ingreso", default=fields.Date.context_today)
    fecha_alta = fields.Date(string="Fecha de alta")
    sintomas = fields.Text(string="Síntomas")

    dias_ingresado = fields.Integer(compute="_compute_dias_ingresado", store=True)

    @api.depends('fecha_ingreso','fecha_alta')
    def _compute_dias_ingresado(self):
        today = fields.Date.today()
        for ingreso in self:
            if ingreso.fecha_ingreso :
                fin = ingreso.fecha_alta or today
                ingreso.dias_ingresado = (fin - ingreso.fecha_ingreso).days
            else:
                ingreso.dias_ingresado = 0
                

