#!/usr/bin/python3
from sys import argv
import MySQLdb

if __name__ == '__main__':
    the_usa = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    commands = the_usa.cursor()
    commands.execute("SELECT cities.id, cities.name, states.name FROM\
    cities JOIN states ON cities.state_id = states.id\
    ORDER BY cities.id ASC")
    usa = commands.fetchall()
    comma_print = 0;
    for state in usa:
        if state[2] == argv[4]:
            if comma_print > 0:
                print(", ", end="")
            print("{:s}".format(state[1]), end="")
            comma_print += 1;
    print("")
    commands.close()
    the_usa.close()
