from models import People

def get_all_people():
    return People.query.all()

def get_person_by_id(person_id):
    return People.query.get(person_id)