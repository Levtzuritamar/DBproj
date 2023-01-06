import mysql.connector

mydb = mysql.connector.connect(
  host="mysqlsrv1.cs.tau.ac.il",
  port="3306",
  user="levtzur",
  password="levtzu2709",
  database='levtzr'
)

cursor = mydb.cursor()
cursor.execute("CREATE TABLE population (Country VARCHAR(255), Population VARCHAR(255))")

