#!/usr/bin/python3

"""
Script connects to a database and gets data from specified table in ASC order

"""
import MySQLdb
import sys


def fetchAll(username, password, database):
    host = 'localhost'
    port = 3306
    db = MySQLdb.connect(
        host=host,
        port=port,
        user=username,
        passwd=password,
        db=database
    )
    cur = db.cursor()
    try:
        cur.execute("SELECT * FROM states")
        states = cur.fetchall()
    except MySQLdb.Error as e:
        print("MySQL error {}".format(str(e)))

    for state in states:
        print(state)


if __name__ == "__main__":
    arguments = sys.argv

    if (len(arguments) != 4):
        print("USAGE: example.py <mysql username> <mysql password>\
                <mysql database>")
    else:
        username = arguments[1]
        password = arguments[2]
        database = arguments[3]

        fetchAll(username, password, database)
