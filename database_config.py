import redis
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from params import username, password, host, database, redis_host, redis_port, redis_pw

# Rdids Config
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_pw)

# SQLAlchemy Config
SQLALCHEMY_DATABASE_URL = f'mysql+pymysql://{username}:{password}@{host}/{database}'
engine = create_engine(SQLALCHEMY_DATABASE_URL)     # , echo=True
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
ScopedSession = scoped_session(SessionLocal)