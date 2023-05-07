import cherrypy
import json
import os


class Products:
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def index(self, token=None):
        if not verify_token(token):
            raise cherrypy.HTTPError(401, "Unauthorized")

        return data

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def create(self, item, token=None):
        if not verify_token(token):
            raise cherrypy.HTTPError(401, "Unauthorized")

        new_id = str(len(data) + 1)
        item["id"] = new_id
        data.append(item)

        return {"status": "success", "message": "Item created"}

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def update(self, id, item, token=None):
        if not verify_token(token):
            raise cherrypy.HTTPError(401, "Unauthorized")

        for index, existing_item in enumerate(data):
            if existing_item["id"] == id:
                data[index] = item
                return {"status": "success", "message": "Item updated"}

        raise cherrypy.HTTPError(404, "Item not found")

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def delete(self, id, token=None):
        if not verify_token(token):
            raise cherrypy.HTTPError(401, "Unauthorized")

        for index, existing_item in enumerate(data):
            if existing_item["id"] == id:
                del data[index]
                return {"status": "success", "message": "Item deleted"}

        raise cherrypy.HTTPError(404, "Item not found")
