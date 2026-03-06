
users = {}

def save_user_preference(user_id, data):
    users[user_id] = data

def get_user_preference(user_id):
    return users.get(user_id, {})
