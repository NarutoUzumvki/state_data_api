from database_config import ScopedSession
from models import States

def add_new_state(name, code, description, capital, chief_minister, population, area, is_ut):
    new_state = States(
        name=name,
        code=code,
        description=description,
        capital=capital,
        chief_minister=chief_minister,
        population=population,
        area=area,
        is_ut=is_ut
    )
    with ScopedSession() as session:
        session.add(new_state)
        session.commit()
        print(f"New State/UT {new_state.name} added")
    return new_state

def update_existing_state(code, name, description, capital, chief_minister, population, area, is_ut):
    with ScopedSession() as session:
        state = get_state_by_code(code)
        state.name = name
        state.description = description
        state.capital = capital
        state.chief_minister = chief_minister
        state.population = population
        state.area = area
        state.is_ut = is_ut
        session.commit()
    return state

def get_state_by_code(code):
    with ScopedSession() as session:
        state = session.query(States).filter(States.code==code).first()
    return state

def get_state_by_id(id):
    with ScopedSession() as session:
        state = session.query(States).filter(States.id==id).first()
    return state

def get_state_by_name(name):
    with ScopedSession() as session:
        state = session.query(States).filter(States.name==name).first()
    return state

def delete_state(code, is_ut=False):
    with ScopedSession() as session:
        session.query(States).filter(States.code==code).filter(States.is_ut==is_ut).delete()
        session.commit()

def return_all_states(is_ut=False):
    with ScopedSession() as session:
        if is_ut:
            states = session.query(States).filter(States.is_ut==is_ut).all()
        else:
            states = session.query(States).all()
    return states