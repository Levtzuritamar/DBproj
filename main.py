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
cursor.execute("CREATE TABLE IF NOT EXISTS population (country VARCHAR(255) PRIMARY KEY, population VARCHAR(255))")

with open('population_by_country.csv', 'r') as file:
    reader = csv.DictReader(file)
    
    # Iterate through the rows of the CSV
    for row in reader:
        country = row['country']
        population = row['population']
        
        # Insert the data into the MySQL table
        cursor.execute('INSERT INTO table (country, population) VALUES (%s, %s)', (country, population))

# Commit the changes to the database
cnx.commit()

# Close the connection to the database
cnx.close()