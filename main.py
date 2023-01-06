import weakref
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
cursor.execute("CREATE TABLE IF NOT EXISTS athlete (athlete_id VARCHAR(255), olympics_game VARCHAR(255), name VARCHAR(255), \
                height VARCHAR(255), weight VARCHAR(255), age VARCHAR(255), \
                    sex VARCHAR(255), country VARCHAR(255), PRIMARY KEY (athlete_id, olympics_game))")

cursor.execute("CREATE TABLE IF NOT EXISTS event (olympics_game VARCHAR(255), event VARCHAR(255), \
                sport VARCHAR(255), PRIMARY KEY (olympics_game, event))")

cursor.execute("CREATE TABLE IF NOT EXISTS olympic_info (olympics_game VARCHAR(255) PRIMARY KEY, season VARCHAR(255), \
                year VARCHAR(255), city VARCHAR(255))")

cursor.execute("CREATE TABLE IF NOT EXISTS olympic_events (olympics_game VARCHAR(255) PRIMARY KEY, event VARCHAR(255))")

cursor.execute("CREATE TABLE IF NOT EXISTS results (olympics_game VARCHAR(255), event VARCHAR(255), \
                athlete_id VARCHAR(255), medal VARCHAR(255), PRIMARY KEY (olympics_game, event, athlete_id))")     

with open('athlete_events.csv', 'r') as file:
    reader = csv.DictReader(file)
    
    # Iterate through the rows of the CSV
    for row in reader:
        athlete_id = row['ID']
        name = row['Name']
        age = row['Age']
        height = row['Height']
        weight = row['Weight']
        sex = row['Sex']
        country = row['Team']
        olympics_game = row['Games']
        year = row['Year']
        city = row['City']
        event = row['Event']
        medal = row['Medal']
        sport = row['Sport']
        season = row['Season']

        
        # Insert the data into the MySQL table
        cursor.execute('INSERT INTO athlete (athlete_id, olympics_game, name, height, weight, age, sex, country) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)', (athlete_id, olympics_game, name, height, weight, age, sex, country))
        cursor.execute('INSERT INTO event (olympics_game, event, sport) VALUES (%s, %s, %s)', (olympics_game, event, sport))
        cursor.execute('INSERT INTO olympic_info (olympics_game, season, year, city) VALUES (%s, %s, %s, %s)', (olympics_game, season, year, city))
        cursor.execute('INSERT INTO olympic_events (olympics_game, event) VALUES (%s, %s)', (olympics_game, event))
        cursor.execute('INSERT INTO results (olympics_game, event, athlete_id, medal) VALUES (%s, %s, %s, %s)', (olympics_game, event, athlete_id, medal))


# Commit the changes to the database
cnx.commit()

# Close the connection to the database
cnx.close()