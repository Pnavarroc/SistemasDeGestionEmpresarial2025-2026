# -*- coding: utf-8 -*-

from odoo import models, fields, api


class medico(models.Model):
    _name = 'hospital2.medico'
    _description = 'Esto es la descripcion del medico'


    name = fields.Char(string="Nombre", required=True)
    apellidos = fields.Char(string="Apellidos")
    telefono = fields.Char(string="Teléfono")
    especialidad = fields.Char(string="Especialidad")
    numero_colegiado = fields.Char(string="Número de colegiado")

    ingreso_ids = fields.One2many(
        'hospital2.ingreso',
        'medico_id',
        string='Ingresos atendidos'
    )
