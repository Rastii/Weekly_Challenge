from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///weeklyc.db', echo=True)
db_session = scoped_session(sessionmaker(autocommit=False, 
                                        autoflush=False,
                                        bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

from weeklyc.models import *

def init_db():
    Base.metadata.create_all(engine)

def kill_db():
    Base.metadata.drop_all(engine)

def setup_db():
    from weeklyc.models import *
    from weeklyc.views import bcrypt

    """ User Creation
    """
    dennis = User(login='skinner927',
            password = bcrypt.generate_password_hash('asdfqwer'))
    db_session.add(dennis)
    luke = User(login='rastii',
            password = bcrypt.generate_password_hash('asdfqwer'))
    db_session.add(luke)
    db_session.commit()

    """ Challenge Creation
    """
    pwnme = Challenge(name="Pwnme",
                        link="/static/files/pwnme",
                        flag="butthurt")
    banana = Challenge(name="Banana",
                        link="/static/files/banana",
                        flag="rotten")
    db_session.add(pwnme)
    db_session.add(banana)
    db_session.commit()

    """ Challenge Submissions
    """
    dennis.submissions.append(pwnme)
    luke.submissions.append(banana)
    db_session.commit()
