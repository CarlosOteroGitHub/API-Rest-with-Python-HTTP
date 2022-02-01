import json
import requests

class API:

    #Función que realiza una petición HTTP - GET a la URL de una página de internet, para guardar el contenido HTML en un archivo binario.
    def get_file(self, url):
        response = requests.get(url)

        if(response.status_code == 200):
            contenido_pagina = response.content
            file = open('google.html', 'wb')
            file.write(contenido_pagina)
            file.close()

    #Función que realiza una petición HTTP - GET a la URL de una página de internet, para descargar un archivo remoto, que puede ser una imagen.
    def get_big_file(self, url):
        response = requests.get(url, stream=True)

        if(response.status_code == 200):
            with open('image.jpg', 'wb') as file:
                for chunk in response.iter_content():
                    file.write(chunk)
            response.close()

    #Función que realiza una petición HTTP - GET y almacena los parámetros especificados a la URL.
    def get_params(self, url):
        params = {'nombre': 'Carlos', 'Edad': '26'}
        response = requests.get(url, params = params)

        if(response.status_code == 200):
            contenido_pagina = response.json()
            print(contenido_pagina)

    #Función que realiza una petición HTTP - GET y guarda el valor de un atributo de un documento JSON.
    def get_json(self, url):
        response = requests.get(url)
        if(response.status_code == 200):
            response_json = response.json()
            origin = response_json['origin']
            print(origin)

    #Función que realiza una petición HTTP - GET y guarda todos los valores de un atributo de un documento JSON.
    def get_attrs_json(self, url):
        response = requests.get(url)
        if(response.status_code == 200):
            response_json = response.json()
            for data in response_json:
                simbolo = data["symbol"]
                precio = data["price"]
                print("Simbolo: ", simbolo, " - Precio: ", precio)

    #Función que realiza una petición HTTP - POST que envia parametros mediante URL para ser almacenados en el atributo "data" de un documento JSON.
    def post_params(self, url):
        params = {'nombre': 'Carlos', 'Edad': '26'}
        response = requests.post(url, data=json.dumps(params))
        if(response.status_code == 200):
            response_json = response.json()
            print(response_json)

   	#Función que realiza una petición HTTP - POST y agrega encabezados mediante parámetros especificados en un documento JSON.
    def post_headers(self, url):
        params = {'nombre': 'Carlos', 'Edad': '26'}
        headers = {'Conten-Type': 'application/json', 'access-token': '12131'}
        response = requests.post(url, data=json.dumps(params), headers=headers)

        if(response.status_code == 200):
            headers_response = response.headers
            print(headers_response)


class MainClass:

    objeto = API()

    print("Selecciona una Opción API HTTP:" 
        + "\n" +  "1. Petición GET a página para guardar el contenido en un archivo HTML." 
        + "\n" + "2. Petición GET para descargar archivos grandes remotos mediante su URL."
        + "\n" + "3. Petición GET para obtener los parametros especificados en una URL."
        + "\n" + "4. Petición GET que obtiene el valor de un atributo dentro de un documento JSON."
        + "\n" + "5. Petición GET que obtiene todos los valores de un atributo dentro de un documento JSON."
        + "\n" + "6. Petición POST que manda parametros a una URL dentro de un documento JSON."
        + "\n" + "7. Petición POST que manda parametros y encabezados a una URL dentro de un documento JSON.")
    opcion = int(input())

    if opcion == 1:
       objeto.get_file("https://www.google.com.mx/")
    elif opcion == 2:
       objeto.get_big_file("https://tec.mx/sites/default/files/inline-images/arbol-de-navidad_0.jpg")
    elif opcion == 3:
       objeto.get_params("http://httpbin.org/get")
    elif opcion == 4:
       objeto.get_json("http://httpbin.org/get")
    elif opcion == 5:
       objeto.get_attrs_json("https://api.binance.com/api/v3/ticker/price")
    elif opcion == 6:
       objeto.post_params("http://httpbin.org/post")
    elif opcion == 7:
       objeto.post_headers("http://httpbin.org/post")

"""

Programa que realiza una serie de peticiones HTTP a diferentes API con Python. 

NOTA: Instale la libreria requests con el siguiente comando: "pip install requests" y ejecute la aplicación mediante el comando "python main.py"

"""