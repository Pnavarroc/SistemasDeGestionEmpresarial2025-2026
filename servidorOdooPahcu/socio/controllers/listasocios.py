# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json

# Clase del controlador web



class ListaSocios(http.Controller):
    
    '''
    LLamada web para obtener lista completa de socios. No es parte de la API REST.
    
    
    Decorador que indica que la url "/gestion/<modelo>" atendera por HTTP, sin autentificacion
    Devolvera texto que estará en formato JSON
    Se puede probar accediendo a http://localhost:8069/socios/socio
    Y nos devolvera informacion sobre cada socio

    '''

    @http.route('/socios/<modelo>', auth='public', cors='*', type='http')
    def obtenerDatosSocios(self, modelo, **kw):
        # Obtenemos la referencia del modelo (pensado en este programa para ser "socios")
        socios = request.env[modelo].sudo().search([])

        #Generamos la lista de socios)
        listaSocios=[]
        for s in socios:
                listaSocios.append([s.dni,s.nombre, s.apellidos])
        json_result=json.dumps(listaSocios, default=str, ensure_ascii=False)
        return json_result
