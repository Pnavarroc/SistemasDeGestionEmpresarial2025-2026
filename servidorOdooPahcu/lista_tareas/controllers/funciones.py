# -*- coding: utf-8 -*-
import json
import random
import time
from urllib import request
from odoo import http


class funciones(http.Controller):
     #http://192.168.1.80:8069/hola
    @http.route('/hola', auth='public',cors='*',type='http')
    def index(self, **kw):
        return "Hello, world"
    #http://192.168.1.80:8069/listartareas
    @http.route('/listartareas', auth='public', cors='*',type='http')
    def devolvertareas(self, **kw):
        #Obtengo los estudiantes
        tareas=http.request.env['lista_tareas.lista_tareas'].sudo().search([])
        lista_tareas=[]
        for tarea in tareas:
            lista_tareas.append([tarea.id,
                                tarea.task,
                                tarea.prioridad,
                                tarea.urgente,
                                tarea.realizada,
                                tarea.responsable.name
                                ])

        json_result=json.dumps(lista_tareas, default=str)
        return json_result

    #http://192.168.1.80:8069/aleatorioretardo
    @http.route('/aleatorioretardo', auth='public',cors='*',type='http')
    def aleatorio(self, **kw):
        numero = random.randint(10, 500)
        retraso= random.randint(1,10)
        time.sleep(retraso)
        return str(numero)

    # http://192.168.1.80:8069/aleatorioretardoJSON
    @http.route('/aleatorioretardoJSON', auth='public',cors='*',type='http')
    def aleatorio2(self, **kw):
        numero = random.randint(10, 500)
        retraso= random.randint(1,10)
        time.sleep(retraso)
        json_result=json.dumps(numero,default=str)
        return str(json_result)



