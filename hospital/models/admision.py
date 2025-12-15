
from odoo import models, fields, api


class admision(models.Model):
    _name = 'hospital.admision'
    _description = 'Esta es la descripcion del ingreso'

    #Tenemos: un ingreso pertenece a un paciente
    #un ingreso lo lleva un medico,
    #un paciente puede tener varios ingresos 
    #Un medico puede llevar varios ingresos.
    #De ahi hace Many2one en la tabla intermedia porque pacientes y médicos pueden tener uno o varios ingresos. 
    patient_id=fields.Many2one('hospital.patient',string="Paciente", required=True)
    doctor_id=fields.Many2one('hospital.doctor', string="Médico", required=True)

    bedroom_number=fields.Char(string="Habitación")
    bed_number=fields.Char(string="Cama")
    admision_date=fields.Date(string="Fecha de ingreso")
    symptoms= fields.Char(string="Sintomas")
    discharge_date=fields.Date(string="Fecha de alta")

    
