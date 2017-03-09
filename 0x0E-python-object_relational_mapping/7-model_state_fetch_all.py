#!/usr/bin/python3
from sys import argv
import sqlalchemy
from model_state import State, Base
import MySQLdb


if __name__ == '__main__':
    mysql = "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2],
                                                        argv[3])
    database = sqlalchemy.create_engine(mysql)
    Base.metadata.create_all(database)
    session_fake = sqlalchemy.orm.sessionmaker(bind=database)
    session = session_fake()
    for element in session.query(State).order_by(State.id):
        print("{}: {}".format(element.id, element.name))
