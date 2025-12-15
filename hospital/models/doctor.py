
from odoo import models, fields, api


class doctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Esta es la descripcion del doctor'

    name = fields.Char(string="Nombre")
    surname = fields.Char(string="Apellidos")

    phone = fields.Char(string="Numero de teléfono")
    specialty= fields.Char(string="Especialidad")
    registration_number= fields.Char(string="Numero de identificación")
    
    admision_ids=fields.One2many('hospital.admision','doctor_id', string="Ingreso")
    
    
