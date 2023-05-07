import cherrypy
import json
import os
from Products.products import Products
from constants import URL,PORT,MS_NAME

class ProductsMicroservice:
    @cherrypy.expose
    @cherrypy.tools.allow(methods=['GET'])
    def is_alive(self):
        return "The microservice |" + MS_NAME + "| is alive"


# Add this function to your app.py file.
def main():
    cherrypy.config.update({'server.socket_host': URL,
                            'server.socket_port': PORT,
                            'engine.autoreload.on': False})
    cherrypy.quickstart(ProductsMicroservice())


if __name__ == '__main__':
    main()