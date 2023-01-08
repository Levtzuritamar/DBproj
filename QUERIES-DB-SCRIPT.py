import mysql.connector

cnx = mysql.connector.connect(
  host="mysqlsrv1.cs.tau.ac.il",
  port="3306",
  user="levtzur",
  password="levtzu2709",
  database='levtzur'
)

cursor = cnx.cursor(buffered = True)
cursor.execute("SELECT E.sport FROM olympic_game_participants as OGP, event AS E WHERE E.event = OGP.event Group by E.sport ORDER BY SUM(OGP.athlete_id) DESC")
print(cursor.fetchmany(size=10))

cursor.execute("SELECT C.country FROM population as C, olympic_game_participates as OGP, athlete as A WHERE A.country  = C.country AND OGP.athlete_id = A.athlete_id GROUP BY A.country ORDER BY SUM(A.athlete_id)/C.population DESC")
print(cursor.fetchmany(size=10))
