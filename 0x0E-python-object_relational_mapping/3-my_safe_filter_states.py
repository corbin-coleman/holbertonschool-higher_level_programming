#!/usr/bin/python3
from sys import argv
import MySQLdb

if __name__ == '__main__':
    the_usa = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    commands = the_usa.cursor()
    commands.execute("SELECT * FROM states ORDER BY id ASC")
    usa = commands.fetchall()
    for state in usa:
        if (state[1] == argv[4]):
            print(state)
    commands.close()
    the_usa.close()
