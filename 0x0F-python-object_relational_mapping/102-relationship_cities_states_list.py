#!/usr/bin/python3
"""
Lists all City objects from the db hbtn_0e_101_usa
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

    user = argv[1]
    passwd = argv[2]
    db = argv[3]

    # create database connection
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(user, passwd, db))

    # create a transaction session
    Session = sessionmaker(bind=engine)
    session = Session()

    all_cities = session.query(City).order_by(City.id).all()
    for city in all_cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    session.close()
