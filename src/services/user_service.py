from models import User, db

def get_all_users():
    users = User.query.all()
    return [user.serialize() for user in users]

def get_user_by_id(user_id):
    user = User.query.get(user_id)
    if user:
        return user.serialize()
    return None