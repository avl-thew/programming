from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.orm import declarative_base
import random
import os
from faker import Faker

if os.path.exists('sqlalchemy_example.db'):
    os.remove('sqlalchemy_example.db')

Base = declarative_base()

class Project(Base):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    manager_id = Column(Integer, ForeignKey('managers.id'))
    manager = relationship("Manager", back_populates="project", uselist=False)

class Manager(Base):
    __tablename__ = 'managers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    project = relationship("Project", back_populates="manager")

class Developer(Base):
    __tablename__ = 'developers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    team_id = Column(Integer, ForeignKey('teams.id'))
    team = relationship("Team", back_populates="developers", uselist=False)

class Team(Base):
    __tablename__ = 'teams'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    developers = relationship("Developer", back_populates="team")

engine = create_engine('sqlite:///sqlalchemy_example.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

fake = Faker()

# тимлиды
for _ in range(5):
    manager = Manager(
        name=fake.name(),
        email=fake.email()
    )
    session.add(manager)

# тимс
for _ in range(3):
    team = Team(
        name=fake.company()
    )
    session.add(team)

# разрабы
for _ in range(20):
    developer = Developer(
        name=fake.name(),
        email=fake.email(),
        team_id=random.randint(1, 3)
    )
    session.add(developer)

# проекты
for _ in range(10):
    project = Project(
        name=fake.catch_phrase(),
        description=fake.text(),
        manager_id=random.randint(1, 5)
    )
    session.add(project)

session.commit()



