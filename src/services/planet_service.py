from models import Planet

def get_all_planets():
    return Planet.query.all()

def get_planet_by_id(planet_id):
    return Planet.query.get(planet_id)