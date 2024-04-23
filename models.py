from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, nullable=False)
    hashed_password = Column(String(100))
    email = Column(String(100))
    api_key = Column(String(50))
    is_active = Column(Boolean, default=True)
    role = Column(String(15), default="user")


class States(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(5), unique=True, nullable=False)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(String(2500))
    capital = Column(String(50))
    chief_minister = Column(String(50))
    population = Column(String(20))
    area = Column(String(20))
    is_ut = Column(Boolean)


class Cities(Base):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(5), unique=True, nullable=False)
    name = Column(String(50))
    state_code = Column(String(5), ForeignKey("states.code"))