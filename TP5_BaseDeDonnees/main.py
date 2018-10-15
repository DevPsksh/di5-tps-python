import sqlite3 as sql


CONNECTION = sql.connect("salut.db")
CURSOR = CONNECTION.cursor()



CURSOR.execute('''CREATE TABLE Communes
             (regionCode text,
             regionName  text,
             arrondissementsCode text,
             cantonsCode real,
             communeCode text,
             communeName text,
             municipalPopulation real,
             comptePopulation real,
             totalPopulation real)''')

CURSOR.execute('''CREATE TABLE Departements
             (regionCode text,
             regionName  text,
             departementCode text,
             departementName text,
             arrondissementsCount text,
             cantonsCount real,
             communesCount real,
             municipalPopulation real,
             totalPopulation real)''')

CURSOR.execute('''CREATE TABLE Regions
             (code text,
             name text,
             arrondissementsCount text,
             cantonsCount real,
             communesCount real,
             municipalPopulation real,
             totalPopulation real)''')

# READING COMMUNES

with (open("bdddata/communes.csv", "r")) as file:
    for line in file.readlines():
        try:
            line = line[:-1]
            split = line.split(";")
            CURSOR.execute('''INSERT INTO Communes VALUES (split[0], split[1], split[2],
                split[3], split[4], split[5],
                split[6], split[7], split[8]
            )''')
        except Exception as e:
            print("Error in communes ", e)

# READING DEPARTEMENTS

with (open("bdddata/departements.csv", "r")) as file:
    for line in file.readlines():
        try:
            line = line[:-1]
            split = line.split(";")
            CURSOR.execute('''INSERT INTO Departements VALUES (split[0], split[1], split[2],
                split[3], split[4], split[5],
                split[6], split[7]
            )''')
        except Exception as e:
            print("Error in departements ", e)

# READIONG REGIONS

with (open("bdddata/regions.csv", "r")) as file:
    for line in file.readlines():
        try:
            line = line[:-1]
            split = line.split(";")
            CURSOR.execute('''INSERT INTO Regions VALUES (split[0], split[1], split[2],
                split[3], split[4], split[5], split[6]
            )''')
        except Exception as e:
            print("Error in regions ", e)

# Insert a row of data
CURSOR.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

CONNECTION.commit()
CONNECTION.close()
