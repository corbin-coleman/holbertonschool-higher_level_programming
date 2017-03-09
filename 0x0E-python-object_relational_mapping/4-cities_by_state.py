#!/usr/bin/python3
from sys import argv
import MySQLdb

if __name__ == '__main__':
    the_usa = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    commands = the_usa.cursor()
    commands.execute("SELECT cities.id, cities.name, states.name FROM\
    cities JOIN states ON cities.state_id = states.id")
    usa = commands.fetchall()
    for state in usa:
        print(state)
    commands.close()
    the_usa.close()
