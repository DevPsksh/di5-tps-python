# TP5 : Base de données
import sqlite3
import csv


# Creation des tables (requetes sql)
def init(cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS region(id INTEGER PRIMARY KEY,
                                          nom TEXT);
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS departement(id TEXT PRIMARY KEY,
                                               nom TEXT,
                                               region_id INTEGER,
                                               FOREIGN KEY(region_id) REFERENCES region(id));

    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS commune(id INTEGER PRIMARY KEY AUTOINCREMENT,
                                          nom TEXT,
                                          canton TEXT,
                                          arrondissement TEXT,
                                          populationMunicipale INTEGER,
                                          populationAutre INTEGER,
                                          departement_id INTEGER,
                                          FOREIGN KEY(departement_id) REFERENCES departement(id));
    ''')

    with open('data/regions.csv', 'r') as fin:
        dr = csv.DictReader(fin, delimiter=';')
        to_db = [(i['id'], i['nom']) for i in dr]

    cursor.executemany("INSERT INTO region (id, nom) VALUES (?, ?);", to_db)

    with open('data/departements.csv', 'r') as fin:
        dr = csv.DictReader(fin, delimiter=';')
        to_db = [(i['id'], i['nom'], i["region_id"]) for i in dr]

    cursor.executemany("INSERT INTO departement (id, nom, region_id) VALUES (?, ?, ?);", to_db)

    with open('data/communes.csv', 'r') as fin:
        dr = csv.DictReader(fin, delimiter=';')
        to_db = [(i['nom'], i["canton"], i["arrondissement"], i["populationMunicipale"], i["populationAutre"],
                  i["departement_id"]) for i in dr]

    cursor.executemany(
        "INSERT INTO commune (nom, canton, arrondissement, populationMunicipale, populationAutre, departement_id) VALUES (?, ?, ?, ?, ?, ?);",
        to_db)


# Creation d'une bdd (requete ou fichier)
db = sqlite3.connect('country')
cursor = db.cursor()

init(cursor)
db.commit()


# db.close()


# -------------------------------------------------------------------------------------#

def computePopulation(cursor):
    result = cursor.execute('''
      SELECT d.region_id, SUM(c.populationMunicipale + c .populationAutre)
      FROM commune c, departement d
      WHERE c.departement_id = d.id
      GROUP BY c.departement_id
    ''')
    populationByDepartement = result.fetchall()

    result = cursor.execute('''
      SELECT r.nom, SUM(populationByDepartement.population)
      FROM region r, (SELECT d.region_id, SUM(c.populationMunicipale + c.populationAutre) AS population
                      FROM commune c, departement d
                      WHERE c.departement_id = d.id
                      GROUP BY c.departement_id) AS populationByDepartement
      WHERE populationByDepartement.region_id = r.id
      GROUP BY populationByDepartement.region_id
    ''')
    populationByRegion = result.fetchall()


# -------------------------------------------------------------------------------------#

import xml.etree.cElementTree as eTree


def extractRegion(cursor):
    result = cursor.execute('''
      SELECT * FROM region
    ''')
    regions = result.fetchall()

    regionsXML = eTree.Element("regions")
    for region in regions:
        regionXML = eTree.SubElement(regionsXML, "region")
        eTree.SubElement(regionXML, "id").text = str(region[0])
        nom = str(region[1])
        eTree.SubElement(regionXML, "nom").text = nom
    tree = eTree.ElementTree(regionsXML)
    tree.write("data/regions.xml")


def extractDepartement(cursor):
    result = cursor.execute('''
      SELECT * FROM departement
    ''')
    departements = result.fetchall()

    departementsXML = eTree.Element("departements")
    for departement in departements:
        departementXML = eTree.SubElement(departementsXML, "departement")
        eTree.SubElement(departementXML, "id").text = str(departement[0])
        eTree.SubElement(departementXML, "nom").text = str(departement[1])
        eTree.SubElement(departementXML, "regionId").text = str(departement[2])
    tree = eTree.ElementTree(departementsXML)
    tree.write("data/departement.xml")


def extractCommune(cursor):
    result = cursor.execute('''
      SELECT * FROM commune
    ''')
    communes = result.fetchall()

    communesXML = eTree.Element("communes")
    for commune in communes:
        communeXML = eTree.SubElement(communesXML, "commune")
        eTree.SubElement(communeXML, "id").text = str(commune[0])
        eTree.SubElement(communeXML, "nom").text = str(commune[1])
        eTree.SubElement(communeXML, "canton").text = str(commune[2])
        eTree.SubElement(communeXML, "arrondissement").text = str(commune[3])
        eTree.SubElement(communeXML, "populatinMunicipale").text = str(commune[4])
        eTree.SubElement(communeXML, "populationAutre").text = str(commune[5])
        eTree.SubElement(communeXML, "departement_id").text = str(commune[6])

    tree = eTree.ElementTree(communesXML)
    tree.write("data/commune.xml")


# ------------------------test des fonction-----------------------------#

computePopulation(cursor)
extractRegion(cursor)
extractDepartement(cursor)
extractCommune(cursor)

db.close()
