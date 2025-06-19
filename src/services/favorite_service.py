from models import Favorites, db

def get_favorites_by_user(user_id):
    favorites = Favorites.query.filter_by(user_id=user_id).all()
    return [fav.serialize() for fav in favorites]

def add_favorite_planet(user_id, planet_id):    
    exists = Favorites.query.filter_by(user_id=user_id, planet_id=planet_id).first()
    if exists:
        return None
    fav = Favorites(user_id=user_id, planet_id=planet_id)
    db.session.add(fav)
    db.session.commit()
    return fav.serialize()

def add_favorite_people(user_id, people_id):
    exists = Favorites.query.filter_by(user_id=user_id, character_id=people_id).first()
    if exists:
        return None
    fav = Favorites(user_id=user_id, character_id=people_id)
    db.session.add(fav)
    db.session.commit()
    return fav.serialize()

def remove_favorite_planet(user_id, planet_id):
    fav = Favorites.query.filter_by(user_id=user_id, planet_id=planet_id).first()
    if fav:
        db.session.delete(fav)
        db.session.commit()
        return True
    return False

def remove_favorite_people(user_id, people_id):
    fav = Favorites.query.filter_by(user_id=user_id, character_id=people_id).first()
    if fav:
        db.session.delete(fav)
        db.session.commit()
        return True
    return False