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
    found = 0
    for element in session.query(State).order_by(State.id):
        if element.name == argv[4]:
            print("{}".format(element.id))
            found = 1
    if not found:
        print("Not found")
