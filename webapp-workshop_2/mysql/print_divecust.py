#!/usr/bin/python
import MySQLdb
import ConfigParser

# load db config
config = ConfigParser.ConfigParser()
config.read('dbcreds.ini')
username = config.get("mysql", "user")
password = config.get("mysql", "pass")


db = MySQLdb.connect("localhost", username, password,"luis" )
cursor = db.cursor()
# Make a string of SQL commands
sql = "SELECT * FROM DIVECUST"

try:
   # Execute the SQL command in a try/except in case of failure
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
      custno = row[0]
      custname = row[1]
      street = row[2]
      city = row[3]
      state = row[4]
      zip = row[5]
      country = row[6]
      # Now print fetched result
      print "%s : %s, %s, %s, %s %s" % \
             (custname, street, city, state, zip, country)
except:
   print "Error: unable to fetch data"


# disconnect from server
db.close()
