from models import Vehicle

def get_all_vehicles():
    return Vehicle.query.all()

def get_vehicle_by_id(vehicle_id):
    return Vehicle.query.get(vehicle_id)