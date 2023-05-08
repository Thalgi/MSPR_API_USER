import cherrypy
import json

from classes.user import UserStore
from classes.user import UserApi
from constants import URL, PORT, MS_NAME


class UserMicroservice:
    @cherrypy.expose
    @cherrypy.tools.allow(methods=['GET'])
    def is_alive(self):
        return "The microservice |" + MS_NAME + "| is alive"

class EchoApi:
    @cherrypy.expose
    @cherrypy.tools.allow(methods=['GET'])
    def echo(self, message):
        return f"Echo: {message}"

def main():
    cherrypy.config.update({'server.socket_host': URL,
                            'server.socket_port': PORT,
                            'engine.autoreload.on': False})
    # user_store = UserStore('resources\\users.json')
    # user_api = UserApi(user_store)
    # print(user_store.users)

    user_store = UserStore('resources\\users.json')
    user_api = UserApi(user_store)
    vibe_check = UserMicroservice()
    echo_api = EchoApi()
    app_config = {
        '/': {
            'tools.trailing_slash.on': False,
            'tools.staticdir.root': '/'
        },
        'vibe_check': {'tools.trailing_slash.on': False},
        '/echo': {'tools.trailing_slash.on': False}
    }


    cherrypy.tree.mount(user_api, '/us', config=app_config)
    cherrypy.tree.mount(vibe_check, '/vibe_check', config=app_config)
    cherrypy.tree.mount(echo_api, '/echo', config=app_config)
    cherrypy.engine.start()
    cherrypy.engine.block()
    #
    # ms = UserMicroservice()
    #
    #
    # # cherrypy.tree.mount(user_api, '/users', config=app_config)
    # cherrypy.tree.mount(ms, '/ms')
    # cherrypy.engine.start()


if __name__ == '__main__':
    main()
