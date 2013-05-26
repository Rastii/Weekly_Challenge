import datetime as dt
from sqlalchemy import Table, Column, ForeignKey, Integer, String,\
Boolean, Text, DateTime
from sqlalchemy.orm import relationship, backref, deferred
from weeklyc.database import Base, db_session
from sqlalchemy.orm.collections import attribute_mapped_collection
import datetime

def now():
    return datetime.datetime.now()

'''
user_submissions = Table('submissions', Base.metadata,
    Column('challenge_id', Integer, ForeignKey('challenges.id')),
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('submission_time', DateTime, default=now()))
'''
class User(Base):
    __tablename__ = 'users'
    id          = Column(Integer, primary_key=True)
    login       = Column(String(64), unique=True)
    password    = deferred(Column(String(60)))
    enabled     = deferred(Column(Boolean, default=True))
    submissions = relationship("Challenge", secondary="submissions",
        backref="users")

    def __repr__(self):
        return '< User(login: %s, enabled: %s) >' %\
            (self.login, self.enabled)


    def enable(self):
        self.enabled = True

    # These four are required helpers for flask user login
    def get_id(self):
        return unicode(self.id)

    def is_active(self):
        return self.enabled

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

class Challenge(Base):
    __tablename__ = 'challenges'
    id              = Column(Integer, primary_key=True)
    name            = Column(String(128), unique=True)
    link            = Column(String(256))
    flag            = Column(String(32))
    submissions     = relationship("Submission", backref="challenges")
    
    def __repr__(self):
        return '< Challenge(id: %s, name: %s, flag: %s) >' %\
            (self.id, self.name, self.flag)

class Submission(Base):
    __tablename__ = 'submissions'
    id              = Column(Integer, primary_key=True)
    name            = Column(Integer, ForeignKey('challenges.id'))
    user_id         = Column(Integer, ForeignKey('users.id'))
    submission_time = Column(DateTime, default=now()) 
