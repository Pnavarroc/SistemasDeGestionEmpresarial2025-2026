from odoo import http
from odoo.http import request
import json



# Clase del controlador web

class ApiRestTareas(http.Controller):
    # Configura CORS para permitir todos los orígenes, métodos y cabeceras
    
    #Definimos la operacion para metodos POST, PUT y MATCH
    @http.route('/gestion/<model>', auth="none", cors='*', csrf=False,
                methods=["POST", "PUT", "PATCH"], type='http')
    def apiPost(self, **args):
        #Obtenemos el modelo de los argumentos
        model = args['model']

        #Pasamos lo recibido en "data" a un diccionario
        dicDatos=json.loads(args['data'])
        #Si se ha indicado dni, hay busqueda
        if dicDatos["id"]:
            search = [('id', '=', dicDatos["id"])]
        else:
            return "{'estado':'TareaNOINDICADA'}"
        #Si la peticion es de tipo POST,m ejecutamos esto
        #En este caso, crearemos un nuevo registro con los datos indicados en "data"
        if (http.request.httprequest.method == 'POST'):
            #Creamos el nuevo registro
            record = request.env[model].sudo().create(
                #Proporcionamos un diccionario con los datos del registro a crear
                dicDatos
                )
            
            #Devolvemos el registro creado, siguiendo este esquema
            return http.Response(
                json.dumps(
                
                    record.read(), #Lectura del registro
                    default=str #Funcion de conversion por defecto (str, para convertir a String elementos como los datetime)
                    ),
                    status=200, # Respuesta de la aplicación al navegador
                    mimetype='application/json'
                )
        #Si la peticion es de tipo PUT o PATCH, ejecutamos esto
        #En este caso, modificaremos un registro con un numero de DNI concreto, cambiando 
        #a los valores pasados en "data"
        if (http.request.httprequest.method == 'PUT' or http.request.httprequest.method == 'PATCH'):

            record = http.request.env[model].sudo().search(search)
            if record and record[0]:
                record[0].write(dicDatos)
                #Devolvemos el registro creado, siguiendo este esquema
                return http.Response(
                    json.dumps(
                    
                        record.read(), #Lectura del registro
                        default=str #Funcion de conversion por defecto (str, para convertir a String elementos como los datetime)
                        ),
                        status=200, # Respuesta de la aplicación al navegador
                        mimetype='application/json'
                    )
            #Caso de que el registro no sea encontrado
            return "Registro no encontrado"
        #Si no es POST, PUT ni PATCH
        return http.request.env['ir.http'].session_info()
        


    '''

    Probar GET (Consultando DNI 3)
    Valor de data: {"DNI":"3"}
    URL COMPLETA (Enviada con GET): http://localhost:8069/gestion/apirest/DNI?data={"dni":"3"} 

    --------------
    Probar DELETE (Borrando DNI 3)
    Valor de data: {"dni":"3"}

    URL COMPLETA (Enviada con DELETE): http://localhost:8069/gestion/apirest/dni?data={"dni":"3"} 

    '''
    @http.route('/gestion/<model>', auth="none", cors='*', csrf=False, methods=["GET", "DELETE"],
                type='http')
    def apiGet(self, **args):
        #Obtenemos el modelo y si hay dni, hacemos la busqueda
        model = args['model']
        search = []
        #Pasamos lo recibido en "data" a un diccionario
        dicDatos=json.loads(args['data'])
        #Si se ha indicado dni, hay busqueda
        if dicDatos["id"]:
            search = [('id', '=', dicDatos["id"])]
        else:
            return "{'estado':'ESTUDIANTENOINDICADO'}"

        #Si es GET, ddeolvemos el registro de la busqueda
        if (http.request.httprequest.method == 'GET'):
            record = http.request.env[model].sudo().search(search)
            if record and record[0]:
                return http.Response( 
                json.dumps(record[0].read(), default=str), 
                    status=200,
                    mimetype='application/json'
                )

            return "{'estado':'NOTFOUND'}"
        #Si es delete, cogemos el primer elemento de la busqueda
        if (http.request.httprequest.method == 'DELETE'):

            record = http.request.env[ model].sudo().search(search)
            #Si hay algun elemento
            if record and record[0]:
                 #Eliminamos el registro encontrado
                aux= http.Response(
                json.dumps(record[0].read(), #Lectura del registro
                    default=str), #Funcion de conversion por defecto (str, para convertir a String elementos como los datetime)
                    status=200, # Respuesta de la aplicación al navegador
                    mimetype='application/json'
                )
                record[0].unlink()
                #Devolvemos el registro eliminado, siguiendo este esquema
                return aux
            return "{'estado':'NOTFOUND'}"
        #Si no es GET ni DELETE
        return http.request.env['ir.http'].session_info()

