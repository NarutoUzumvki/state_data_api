from database_config import ScopedSession
from models import Cities

def add_new_city(name, state_code, code=None):
    new_city = Cities(
        name=name,
        code=code if code else generate_city_code(state_code),
        state_code=state_code,
    )
    with ScopedSession() as session:
        session.add(new_city)
        session.commit()
        print(f"New City {new_city.name} added")
    return new_city

def update_existing_city(code, name, state_code):
    with ScopedSession() as session:
        city = get_city_by_code(code)
        city.name = name
        city.state_code = state_code
        session.commit()
    return city

def get_city_by_id(id):
    with ScopedSession() as session:
        city = session.query(Cities).filter(Cities.id==id).first()
    return city

def get_city_by_code(code):
    with ScopedSession() as session:
        city = session.query(Cities).filter(Cities.code==code).first()
    return city

def return_all_cities_by_state_code(state_code):
    with ScopedSession() as session:
        cities = session.query(Cities).filter(Cities.state_code==state_code).all()
    return cities

def delete_city(code):
    with ScopedSession() as session:
        session.query(Cities).filter(Cities.code==code).delete()
        session.commit()

def return_all_cities():
    with ScopedSession() as session:
        cities = session.query(Cities).all()
    return cities

def generate_city_code(state_code):
    with ScopedSession() as session:
        last_city_code = session.query(Cities.code).filter(Cities.state_code==state_code).order_by(Cities.code.desc()).first()
    if not last_city_code:
        new_city_code = f'{state_code}001'
    else:
        last_city_code = last_city_code[0]
        int_code = last_city_code[-3:]
        new_int_code = str(int(int_code)+1)
        new_int_code = "0"*(3-len(new_int_code)) + new_int_code
        new_city_code = last_city_code[:2] + new_int_code
    return new_city_code