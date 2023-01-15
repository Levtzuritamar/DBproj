import mysql.connector
import csv 

cnx = mysql.connector.connect(
  host="mysqlsrv1.cs.tau.ac.il",
  port="3306",
  user="levtzur",
  password="levtzu2709",
  database='levtzur'
)

cursor = cnx.cursor()
cursor.execute("DROP TABLE IF EXISTS population, athlete, event, olympic_info, olympic_game_participants, medals")

# First, create a table for population per country with country name as primary key
cursor.execute("CREATE TABLE IF NOT EXISTS population (country VARCHAR(255) PRIMARY KEY, population VARCHAR(255))")

# Now, create a four different tables from the athele_events csv table
cursor.execute("CREATE TABLE IF NOT EXISTS athlete (athlete_id VARCHAR(255), name VARCHAR(255), dob VARCHAR(255), height VARCHAR(255), weight VARCHAR(255), sex VARCHAR(255), country VARCHAR(255), PRIMARY KEY (athlete_id))")

cursor.execute("CREATE TABLE IF NOT EXISTS event (event VARCHAR(255), edition_id VARCHAR(255), \
                sport VARCHAR(255), isTeamSport VARCHAR(255), PRIMARY KEY (event))")

cursor.execute("CREATE TABLE IF NOT EXISTS olympic_info (edition_id VARCHAR(255) PRIMARY KEY, season VARCHAR(255), \
year VARCHAR(255), city VARCHAR(255))")

cursor.execute("CREATE TABLE IF NOT EXISTS olympic_game_participants (edition_id VARCHAR(255), event VARCHAR(255), athlete_id VARCHAR(255), \
                medal VARCHAR(255), PRIMARY KEY (edition_id, event, athlete_id))")

cursor.execute("CREATE TABLE IF NOT EXISTS medals (country VARCHAR(255), edition_id VARCHAR(255), gold VARCHAR(255), \
                silver VARCHAR(255), bronze VARCHAR(255), PRIMARY KEY (country, edition_id))")

# Adding indexes
cursor.execute("CREATE INDEX country ON athlete (country)")
cursor.execute("CREATE INDEX sport ON event (sport)")


# Commit the changes to the database
cnx.commit()

# Close the connection to the database
cnx.close()