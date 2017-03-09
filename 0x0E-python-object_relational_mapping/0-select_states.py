#!/usr/bin/python3
from sys import argv
import MySQLdb

if __name__ == '__main__':
    the_usa = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2], db=argv[3])
    commands = the_usa.cursor()
    commands.execute("SELECT * FROM states")
    usa = commands.fetchall()
    for state in usa:
        print(state)
    comands.close()
    the_usa.close()
