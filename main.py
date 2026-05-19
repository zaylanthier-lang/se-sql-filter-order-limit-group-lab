import pandas as pd
import sqlite3

##### Part I: Basic Filtering #####

# Create the connection
# Note the connect is 'conn1' since there will be multiple .db used
conn1 = sqlite3.connect('planets.db')

# Select all
pd.read_sql("""SELECT * FROM planets; """, conn1)

# STEP 1
df_no_moons = pd.read_sql("""
SELECT *
FROM planets
WHERE number_of_moons = 0;
""", conn1)

# STEP 2
df_name_seven = pd.read_sql("""
SELECT name, mass
FROM planets
WHERE LENGTH(name) = 7;
""", conn1)

##### Part 2: Advanced Filtering #####

# STEP 3
df_mass = pd.read_sql("""
SELECT name, mass
FROM planets
WHERE mass <= 1.00;
""", conn1)

# STEP 4
df_mass_moon = pd.read_sql("""
SELECT *
FROM planets
WHERE number_of_moons >= 1
AND mass < 1.00;
""", conn1)

# STEP 5
df_blue = pd.read_sql("""
SELECT name, color
FROM planets
WHERE color LIKE '%blue%';
""", conn1)

##### Part 3: Ordering and Limiting #####

# STEP 0

# Create a connection
# Note the connect is 'conn2' since they will be multiple .db used
conn2 = sqlite3.connect('dogs.db')

# Select all
pd.read_sql("SELECT * FROM dogs;", conn2)

# STEP 6
df_hungry = pd.read_sql("""
SELECT name, age, breed
FROM dogs
WHERE hungry = 1
ORDER BY age ASC;
""", conn2)

# STEP 7
df_hungry_ages = pd.read_sql("""
SELECT name, age, hungry
FROM dogs
WHERE hungry = 1
AND age BETWEEN 2 AND 7
ORDER BY name ASC;
""", conn2)

# STEP 8
df_4_oldest = pd.read_sql("""
SELECT name, age, breed
FROM dogs
ORDER BY age DESC
LIMIT 4;
""", conn2)

df_4_oldest = df_4_oldest.sort_values(by="breed")

##### Part 4: Aggregation #####

# STEP 0

# Create a connection
# Note the connect is 'conn3' since they will be multiple .db used
conn3 = sqlite3.connect('babe_ruth.db')

# Select all
pd.read_sql("""
SELECT * FROM babe_ruth_stats; """, conn3)

# STEP 9
df_ruth_years = pd.read_sql("""
SELECT COUNT(*) AS total_years
FROM babe_ruth_stats;
""", conn3)

# STEP 10
df_hr_total = pd.read_sql("""
SELECT SUM(HR) AS total_home_runs
FROM babe_ruth_stats;
""", conn3)

##### Part 5: Grouping and Aggregation #####

# STEP 11
df_teams_years = pd.read_sql("""
SELECT team, COUNT(*) AS number_years
FROM babe_ruth_stats
GROUP BY team;
""", conn3)

# STEP 12
df_at_bats = pd.read_sql("""
SELECT team, AVG(AB) AS average_at_bats
FROM babe_ruth_stats
GROUP BY team
HAVING AVG(AB) > 200;
""", conn3)

conn1.close()
conn2.close()
conn3.close()