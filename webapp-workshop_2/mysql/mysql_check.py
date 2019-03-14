#!/usr/bin/python
import ConfigParser
import MySQLdb

# load db config
config = ConfigParser.ConfigParser()
config.read('dbcreds.ini')
username = config.get("mysql", "user")
password = config.get("mysql", "pass")

# Open database connection
db = MySQLdb.connect("localhost", username, password, "luis" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print("Database version : %s " % data)

# disconnect from server
db.close()