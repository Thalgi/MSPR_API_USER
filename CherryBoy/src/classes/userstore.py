import json
from user import User
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
