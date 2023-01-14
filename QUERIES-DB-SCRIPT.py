import mysql.connector

cnx = mysql.connector.connect(
  host="mysqlsrv1.cs.tau.ac.il",
  port="3306",
  user="levtzur",
  password="levtzu2709",
  database='levtzur'
)

cursor = cnx.cursor(buffered = True)


# First query 
cursor.execute("SELECT athlete.country, COUNT(olympic_game_participants.athlete_id) / population.population AS participants_population_ratio FROM olympic_game_participants JOIN athlete ON olympic_game_participants.athlete_id = athlete.athlete_id JOIN population ON athlete.country = population.country GROUP BY athlete.country, population.population ORDER BY participants_population_ratio DESC")
print(cursor.fetchmany(size=10))


#cursor.execute("SELECT C.country FROM population as C, olympic_game_participants as OGP, athlete as A WHERE A.country LIKE C.country AND OGP.athlete_id = A.athlete_id")


# Second query: Sports by number of participants. We display the top and bottom 5. 
cursor.execute("SELECT E.sport FROM olympic_game_participants as OGP, event AS E WHERE E.event = OGP.event Group by E.sport ORDER BY SUM(OGP.athlete_id) ASC")

print(cursor.fetchmany(size=10))
