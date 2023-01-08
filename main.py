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

with open('population_by_country.csv', 'r') as file:
    reader = csv.DictReader(file)
    
    # Iterate through the rows of the CSV
    for row in reader:
        country = row['name']
        population = row['population']
        
        # Insert the data into the MySQL table
        cursor.execute('INSERT INTO population (country, population) VALUES (%s, %s)', (country, population))


# Now, create a four different tables from the athele_events csv table
cursor.execute("CREATE TABLE IF NOT EXISTS athlete (athlete_id VARCHAR(255), name VARCHAR(255), dob VARCHAR(255, height VARCHAR(255), weight VARCHAR(255), sex VARCHAR(255), country VARCHAR(255), PRIMARY KEY (athlete_id))")

with open('Olympic_Athlete_Bio.csv', 'r') as file:
    reader = csv.DictReader(file)
    
    # Iterate through the rows of the CSV
    for row in reader:
        athlete_id = row['athlete_id']
        name = row['name']
        dob = row['born']
        height = row['height']
        weight = row['weight']
        sex = row['sex']
        country = row['team']

        cursor.execute('INSERT INTO athlete (athlete_id, name, dob, height, weight, sex, country) VALUES (%s, %s, %s, %s, %s, %s, %s)', (athlete_id, name, dob, height, weight, sex, country))

cursor.execute("CREATE TABLE IF NOT EXISTS event (event VARCHAR(255), edition_id VARCHAR(255), \
                sport VARCHAR(255), isTeamSport VARCHAR(255), PRIMARY KEY (event))")

with open('Olympic_Athlete_Event_Results.csv', 'r') as file:
    reader = csv.DictReader(file)
    
    # Iterate through the rows of the CSV
    for row in reader:
        event = row['event']
        edition_id = row['edition_id']
        sport = row['sport']
        isTeamSport = row['isTeamSport']

        cursor.execute('INSERT INTO event (event, edition_id, sport, isTeamSport) VALUES (%s, %s, %s, %s)', (event, edition_id, sport, isTeamSport))


cursor.execute("CREATE TABLE IF NOT EXISTS olympic_info (edition_id VARCHAR(255) PRIMARY KEY, season VARCHAR(255), \
                year VARCHAR(255), city VARCHAR(255))")

with open('Olympics_Games.csv', 'r') as file:
    reader = csv.DictReader(file)
    
    # Iterate through the rows of the CSV
    for row in reader:
        edition_id = row['edition_id']
        season = row['season']
        year = row['year']
        city = row['city']

        cursor.execute('INSERT INTO olympic_info (edition_id, season, year, city) VALUES (%s, %s, %s, %s)', (edition_id, season, year, city))


cursor.execute("CREATE TABLE IF NOT EXISTS olympic_game_participants (edition_id VARCHAR(255), event VARCHAR(255), athlete_id VARCHAR(255), \
                medal VARCHAR(255), PRIMARY KEY (edition_id, event, athlete_id))")

with open('Olympic_Athlete_Event_Results.csv', 'r') as file:
    reader = csv.DictReader(file)
    
    # Iterate through the rows of the CSV
    for row in reader:
        edition_id = row['edition_id']
        event = row['event']
        athlete_id = row['athlete_id']
        medal = row['medal']


        cursor.execute('INSERT INTO olympic_game_participants (edition_id, event, athlete_id, medal) VALUES (%s, %s, %s, %s)', (edition_id, event, athlete_id, medal))

cursor.execute("CREATE TABLE IF NOT EXISTS medals (country VARCHAR(255), edition_id VARCHAR(255), gold VARCHAR(255), \
                silver VARCHAR(255), bronze VARCHAR(255), PRIMARY KEY (country, edition_id))")

with open('Olympic_Games_Medal_Tally.csv', 'r') as file:
    reader = csv.DictReader(file)
    
    # Iterate through the rows of the CSV
    for row in reader:
        country = row['country']
        edition_id = row['edition_id']
        gold = row['gold']
        silver = row['silver']
        bronze = row['bronze']

        cursor.execute('INSERT INTO olympic_game_participants (country, edition_id, gold, silver, bronze) VALUES (%s, %s, %s, %s, %s)', (country, edition_id, gold, silver, bronze))



# Commit the changes to the database
cnx.commit()

# Close the connection to the database
cnx.close()