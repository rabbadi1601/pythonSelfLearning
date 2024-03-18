import mysql.connector

mydbconnect = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database = 'sample_rajudb'


)
mydbconnect.is_connected()

#print(mydb)
mycursor = mydbconnect.cursor()

mycursor.execute("select Data_value,Subject,series_title_2 from samplemachine_db limit 10")
myresult = mycursor.fetchall()
print(type(myresult))  # <class 'list'>

for x in myresult:
  print(x)

for Data_value,Subject,series_title_2 in myresult:
  print("Date Value :{} ,Subject : {} , series_title_2 : {}".format(Data_value,Subject,series_title_2))

mycursor.close()
mydbconnect.close()