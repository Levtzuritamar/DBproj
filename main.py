import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  port="3305",
  user="levtzur",
  password="levtzu2709"
)

print(mydb)