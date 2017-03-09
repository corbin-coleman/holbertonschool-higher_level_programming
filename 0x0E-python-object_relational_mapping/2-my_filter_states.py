#!/usr/bin/python3
from sys import argv
import MySQLdb

if __name__ == '__main__':
    the_usa = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    commands = the_usa.cursor()
    select_command = "SELECT * FROM states WHERE name = '{:s}'".format(argv[4])
    commands.execute(select_command)
    usa = commands.fetchall()
    for state in usa:
        print(state)
    commands.close()
    the_usa.close()
