import connection
import mysql.connector

# Create the connection object
myconn = mysql.connector.connect(host="localhost", user="root", passwd="google", database="mydb")

# printing the connection object
print(myconn)

myconn.close(

from mysql.connector import connection

# Connecting to the server
conn = connection.MySQLConnection(user='username',
                                  host='localhost',
                                  database='database_name')

print(conn)

# Disconnecting from the server
conn.close()