import mysql.connector

cnx = mysql.connector.connect(
  host="mysqlsrv1.cs.tau.ac.il",
  port="3306",
  user="levtzur",
  password="levtzu2709",
  database='levtzur'
)

cursor = cnx.cursor(buffered = True)


# First query: Countries with the highest particiants and population ratio
cursor.execute("SELECT athlete.country, FORMAT((COUNT(olympic_game_participants.athlete_id) / population.population)*100,3) AS participants_population_ratio FROM olympic_game_participants JOIN athlete ON olympic_game_participants.athlete_id = athlete.athlete_id JOIN population ON athlete.country = population.country GROUP BY athlete.country, population.population ORDER BY participants_population_ratio DESC LIMIT 10")
print(cursor.fetchmany(size=10))

# Second query: Sports by number of participants. We display the top and bottom 5. 
cursor.execute("SELECT E.sport FROM olympic_game_participants as OGP, event AS E WHERE E.event = OGP.event Group by E.sport ORDER BY SUM(OGP.athlete_id) DESC LIMIT 10")
print(cursor.fetchmany(size=10))

# Third query: 
cursor.execute("WITH medals_count AS (SELECT country, SUM(gold + silver + bronze) AS total_medals, population FROM medals JOIN population ON medals.country = population.country GROUP BY country, population) SELECT country, (total_medals / population) AS medals_population_ratio FROM medals_count ORDER BY medals_population_ratio DESC LIMIT 10")
print(cursor.fetchmany(size=10))