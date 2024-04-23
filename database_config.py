import redis
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from params import username, password, host, database, redis_host, redis_pw

# Rdids Config
redis_client = redis.StrictRedis(host=redis_host, port=16129, password=redis_pw)

# SQLAlchemy Config
SQLALCHEMY_DATABASE_URL = f'mysql://{username}:{password}@{host}/{database}'
engine = create_engine(SQLALCHEMY_DATABASE_URL)     # , echo=True
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
ScopedSession = scoped_session(SessionLocal)