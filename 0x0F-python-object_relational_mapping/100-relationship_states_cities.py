#!/usr/bin/python3
"""
Creates the State California with the city San Francisco
from the db hbtn_0e_100_usa
Usage: ./14-model_city_fetch_by_state.py <mysql username>\
                                         <mysql passwd>\
                                         <database name>

"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import Base, City
from relationship_state import State
from sys import argv

if __name__ == "__main__":
    # create database connection
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)
    # create a transaction session
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="California")
    new_city = City(name="San Francisco")
    new_state.cities.append(new_city)

    session.add(new_state)
    session.add(new_city)

    session.commit()
    session.close()
