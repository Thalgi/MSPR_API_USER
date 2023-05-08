import json

import cherrypy


class User:
    def __init__(self, user_data):
        self.created_at = user_data["createdAt"]
        self.name = user_data["name"]
        self.username = user_data["username"]
        self.first_name = user_data["firstName"]
        self.last_name = user_data["lastName"]
        self.address = user_data["address"]
        self.profile = user_data["profile"]
        self.company = user_data["company"]
        self.id = user_data["id"]
        self.orders = user_data["orders"]


class UserApi:
    def __init__(self, user_store):
        self.user_store = user_store

    @cherrypy.expose
    @cherrypy.tools.allow(methods=['POST'])
    @cherrypy.tools.json_out()
    def create(self, user_data_json):
        user_data = json.loads(user_data_json)
        user = self.user_store.create(user_data)
        return vars(user)

    @cherrypy.expose
    @cherrypy.tools.allow(methods=['PUT'])
    @cherrypy.tools.json_out()
    def update(self, user_id, user_data_json):
        user_data = json.loads(user_data_json)
        user = self.user_store.update(user_id, user_data)
        if user:
            return vars(user)
        raise cherrypy.HTTPError(404, "User not found")

    @cherrypy.expose
    @cherrypy.tools.allow(methods=['DELETE'])
    def delete(self, user_id):
        if self.user_store.delete(user_id):
            return "User deleted"
        raise cherrypy.HTTPError(404, "User not found")

    @cherrypy.expose
    @cherrypy.tools.allow(methods=['GET'])
    @cherrypy.tools.json_out()
    def get(self, user_id):
        user = self.user_store.get(user_id)
        if user:
            return vars(user)
        raise cherrypy.HTTPError(404, "User not found")


class UserStore:
    def __init__(self, file_path):
        self.file_path = file_path
        self.users = self.load_users()

    def load_users(self):
        with open(self.file_path, 'r') as f:
            data = json.load(f)
        return {user_data['id']: User(user_data) for user_data in data}

    def create(self, user_data):
        user = User(user_data)
        self.users[user.id] = user
        self.save_users()
        return user

    def update(self, user_id, user_data):
        user = self.users.get(user_id)
        if user:
            for key, value in user_data.items():
                setattr(user, key, value)
            self.save_users()
            return user
        return None

    def delete(self, user_id):
        if user_id in self.users:
            del self.users[user_id]
            self.save_users()
            return True
        return False

    def get(self, user_id):
        return self.users.get(user_id)

    def save_users(self):
        data = [vars(user) for user in self.users.values()]
        with open(self.file_path, 'w') as f:
            json.dump(data, f)
