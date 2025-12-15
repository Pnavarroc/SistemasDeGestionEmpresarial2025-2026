
from odoo import models, fields, api


class patient(models.Model):
    _name = 'hospital.patient'
    _description = 'Esta es la descripcion del paciente'

    name = fields.Char(string="Nombre", required=True)
    surname = fields.Char(string="Apellidos", required=True)

    adress = fields.Char(string="Dirección" )
    city= fields.Char(string="Ciudad")
    province= fields.Char(string="Provincia")
    zip_code=fields.Char(string="Código postal")
    phone = fields.Char(string="Teléfono")
    birthday= fields.Date("Fecha de cumpleaños")

    admision_ids=fields.One2many('hospital.admision','patient_id', string="Ingreso")



    

    