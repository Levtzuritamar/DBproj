import mysql.connector

cnx = mysql.connector.connect(
  host="mysqlsrv1.cs.tau.ac.il",
  port="3306",
  user="levtzur",
  password="levtzu2709",
  database='levtzur'
)

cursor = cnx.cursor(buffered = True)

# First query: Countries with highest amount of participants
cursor.execute("SELECT athlete.country, COUNT(DISTINCT olympic_game_participants.athlete_id) AS total_participants FROM olympic_game_participants JOIN athlete ON olympic_game_participants.athlete_id = athlete.athlete_id  GROUP BY athlete.country ORDER BY total_participants DESC LIMIT 10")
print(cursor.fetchmany(size=10))

# Second query: Countries with the highest particiants and population ratio
cursor.execute("SELECT athlete.country, FORMAT((COUNT(DISTINCT olympic_game_participants.athlete_id) / population.population)*100,3) AS participants_population_ratio FROM olympic_game_participants JOIN athlete ON olympic_game_participants.athlete_id = athlete.athlete_id JOIN population ON athlete.country = population.country GROUP BY athlete.country, population.population ORDER BY participants_population_ratio DESC LIMIT 10")
print(cursor.fetchmany(size=10))

# Third query: Sports by number of participants
cursor.execute("SELECT E.sport, SUM(DISTINCT OGP.athlete_id) as total_athletes FROM olympic_game_participants as OGP, event AS E WHERE E.event = OGP.event Group by E.sport ORDER BY total_athletes ASC LIMIT 10")
print(cursor.fetchmany(size=10))

# Fourth query: Countries with the highest medal winnings and population ratio
cursor.execute("WITH medals_count AS (SELECT medals.country, SUM(medals.gold + medals.silver + medals.bronze) AS total_medals, population FROM medals JOIN population ON medals.country = population.country GROUP BY country, population) SELECT country, FORMAT((total_medals / population)*100,4) AS medals_population_ratio FROM medals_count ORDER BY medals_population_ratio DESC LIMIT 10")
print(cursor.fetchmany(size=10))

# Fifth query: Countries with higest medal winnings and participants ratio
cursor.execute("WITH medals_count AS (SELECT medals.country, SUM(medals.gold + medals.silver + medals.bronze) AS total_medals FROM medals GROUP BY country), total_participants_count AS (SELECT athlete.country, COUNT(DISTINCT athlete.athlete_id) as total_participants FROM olympic_game_participants JOIN athlete ON olympic_game_participants.athlete_id = athlete.athlete_id GROUP BY athlete.country) SELECT medals_count.country, (medals_count.total_medals / total_participants_count.total_participants) AS medals_participants_ratio FROM medals_count JOIN total_participants_count ON medals_count.country = total_participants_count.country ORDER BY medals_participants_ratio DESC LIMIT 10")
print(cursor.fetchmany(size=10))