#!/usr/bin/python3
from sys import argv
import MySQLdb

the_usa = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
commands = the_usa.cursor()
commands.execute("SELECT * FROM states")
usa = commands.fetchall()
for state in usa:
    print(state)
the_usa.close()
