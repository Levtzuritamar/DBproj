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

with open('population_by_country.csv', 'r') as file:
    reader = csv.DictReader(file)
    
    # Iterate through the rows of the CSV
    for row in reader:
        country = row['name']
        population = row['population']
        
        # Insert the data into the MySQL table
        cursor.execute('INSERT INTO population (country, population) VALUES (%s, %s)', (country, population))



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
        country = row['country'].strip()

        cursor.execute('INSERT INTO athlete (athlete_id, name, dob, height, weight, sex, country) VALUES (%s, %s, %s, %s, %s, %s, %s)', (athlete_id, name, dob, height, weight, sex, country))


with open('Olympic_Athlete_Event_Results.csv', 'r') as file:
    reader = csv.DictReader(file)
    
    # Iterate through the rows of the CSV
    for row in reader:
        event = row['event']
        edition_id = row['edition_id']
        sport = row['sport']
        isTeamSport = row['isTeamSport']

        cursor.execute('INSERT IGNORE INTO event (event, edition_id, sport, isTeamSport) VALUES (%s, %s, %s, %s)', (event, edition_id, sport, isTeamSport))


with open('Olympics_Games.csv', 'r') as file:
    reader = csv.DictReader(file)
    
    # Iterate through the rows of the CSV
    for row in reader:
        edition_id = row['edition_id']
        season = row['season']
        year = row['year']
        city = row['city']

        cursor.execute('INSERT INTO olympic_info (edition_id, season, year, city) VALUES (%s, %s, %s, %s)', (edition_id, season, year, city))


with open('Olympic_Athlete_Event_Results.csv', 'r') as file:
    reader = csv.DictReader(file)
    
    # Iterate through the rows of the CSV
    for row in reader:
        edition_id = row['edition_id']
        event = row['event']
        athlete_id = row['athlete_id']
        medal = row['medal']


        cursor.execute('INSERT IGNORE INTO olympic_game_participants (edition_id, event, athlete_id, medal) VALUES (%s, %s, %s, %s)', (edition_id, event, athlete_id, medal))


with open('Olympic_Games_Medal_Tally.csv', 'r') as file:
    reader = csv.DictReader(file)
    
    # Iterate through the rows of the CSV
    for row in reader:
        country = row['country'].strip()
        edition_id = row['edition_id']
        gold = row['gold']
        silver = row['silver']
        bronze = row['bronze']

        cursor.execute('INSERT IGNORE INTO medals (country, edition_id, gold, silver, bronze) VALUES (%s, %s, %s, %s, %s)', (country, edition_id, gold, silver, bronze))

# Commit the changes to the database
cnx.commit()

# Close the connection to the database
cnx.close()
