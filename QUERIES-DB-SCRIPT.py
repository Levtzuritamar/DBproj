import mysql.connector

cnx = mysql.connector.connect(
  host="mysqlsrv1.cs.tau.ac.il",
  port="3306",
  user="levtzur",
  password="levtzu2709",
  database='levtzur'
)

cursor = cnx.cursor()
cursor.execute("SELECT E.sport FROM olympic_game_participants as OGP, event AS E WHERE E.event = OGP.event Group by E.sport ORDER BY SUM(OGP.athlete_id) DESC")
print(cursor.fetchmany(size=10))
