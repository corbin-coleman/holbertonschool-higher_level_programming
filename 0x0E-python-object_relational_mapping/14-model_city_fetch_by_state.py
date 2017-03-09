#!/usr/bin/python3
from sys import argv
import sqlalchemy
from model_state import State, Base
from model_city import City
import MySQLdb


if __name__ == '__main__':
    mysql = "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2],
                                                        argv[3])
    database = sqlalchemy.create_engine(mysql)
    Base.metadata.create_all(database)
    session_fake = sqlalchemy.orm.sessionmaker(bind=database)
    session = session_fake()
    for state, city in session.query(State, City).join(City).order_by(City.id):
        print("{}: ({}) {}".format(state.name, city.id, city.name))
