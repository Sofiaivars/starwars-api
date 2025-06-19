
def people_serializer(person):
    return {
        "id": person.id,
        "name": person.name,
        "birth_year": person.birth_year,
        "gender": person.gender
    }

def planet_serializer(planet):
    return {
        "id": planet.id,
        "name": planet.name,
        "climate": planet.climate,
        "terrain": planet.terrain
    }

def vehicle_serializer(vehicle):
    return {
        "id": vehicle.id,
        "name": vehicle.name,
        "model": vehicle.model,
        "manufacturer": vehicle.manufacturer,
    }

def user_serializer(user):
    return {
        "id": user.id,
        "username": user.username,
        "firstname": user.firstname,
        "lastname": user.lastname,
        "email": user.email,        
    }