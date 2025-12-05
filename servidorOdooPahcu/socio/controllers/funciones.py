# -*- coding: utf-8 -*-
import json
import random
import time
from urllib import request
from odoo import http
import math


class funciones(http.Controller):
 
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
        numero = random.randint(1, 100)
        retraso= random.randint(1,2)
        time.sleep(retraso)
        return str(numero)

    # http://192.168.1.80:8069/aleatorioretardoJSON
    @http.route('/aleatorioretardoJSON', auth='public',cors='*',type='http')
    def aleatorio2(self, **kw):
        numero = random.randint(1,100)
        retraso= random.randint(1,2)
        time.sleep(retraso)
        json_result=json.dumps(numero,default=str)
        return str(json_result)


    @http.route('/EsPrimo', auth="none", cors='*', csrf=False, methods=["GET"],
                type='http')
    def esPrimo(self, **args):
        #Pasamos lo recibido en "data" a un diccionario
        dicDatos=json.loads(args['data'])
        numero = int(dicDatos["num"])    
        def es_primo(num):
            if num <= 1:
                return 'false'
            #    return "{'ESPRIMO':'False'}"
            # Solo necesitamos verificar hasta la raíz cuadrada del número

            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    return 'false'
                #    return "{'ESPRIMO':'False'}"
            #return "{'ESPRIMO':'True'}"
            return 'true'

        
        #Si es GET, devolvemos el registro de la busqueda
        if (http.request.httprequest.method == 'GET'):
            return http.Response( 
                json.dumps(es_primo(numero), default=str), 
                    status=200,
                    mimetype='application/json'

                )

                


