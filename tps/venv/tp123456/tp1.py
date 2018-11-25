# Fichiers

# 1. Afficher « Bonjour le monde ! »

print(" Bonjour le monde ! ")

print("1. Choisir un nom de fichier")
print("2. Ajouter un text")
print("3. Afficher le fichier complet")
print("4. Vider le fichier")
print("9. Quitter")


# 2. En mode console, proposez un petit menu


# 3. a. Concevoir une classe Date
class Date:

    # Constructor
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    # Overloading '<'
    def __lt__(self, date):
        if self.year < date.year and self.month < date.month and self.day < date.day:
            return 1
        elif self.year > date.year and self.month > date.month:
            return 0
        return 0

    # Overloading '=='
    def __eq__(self, date):
        if self.year == date.year and self.month == date.month and self.day == date.day:
            return 1
        return 0


# 3. b. Concevoir une classe Etudiant
import time


class Etudiant:
    def __init__(self, prenom, nom, date):
        self.nom = nom
        self.prenom = prenom
        result = date.split("/")
        day = int(result[0])
        month = int(result[1])
        year = int(result[2])
        self.date = Date(day, month, year)

    def adresselec(self):
        return self.prenom.lower() + "." + self.nom.lower() + "@etu.univ-tours.fr"

    def getAge(self):
        today = Date(int(time.strftime("%d")), int(time.strftime("%m")), int(time.strftime("%Y")))
        # Options et Gestion d'erreur
        if today.month == self.date.month and today.day == self.date.day:
            return str(today.year - self.date.year) + " (Joyeux Anniv ;) )"
        if self.date.year < today.year:
            if self.date.month > today.month:
                return str(today.year - self.date.year - 1)
            elif self.date.month == today.month and self.date.day > today.day:
                return str(today.year - self.date.year - 1)
            else:
                return str(today.year - self.date.year)
        else:
            return "Y a un soucis avec l'année, trop jeune ;) "

    def toString(self):
        return self.prenom + " " + self.nom


# 3. c. Lire le fichier fichetu.csv et constituer une liste d'objets Etudiant

nom_fichier = ""
choix = 0


def menu(nameFile=""):
    if nameFile != "":
        nameFile = "(" + nameFile + ")"
    else:
        nameFile = "(Pas de fichier sélectionné)"
    print("\nMenu principale " + nameFile)
    print("1. Choisir un nom de fichier")
    print("2. Ajouter un texte")
    print("3. Afficher le fichier complet")
    print("4. Vider le fichier")
    print("9. Quitter le programme")
    return input("Veuillez choisir le numéro souhaité : ")


while choix != "9":
    try:
        # Cas 1 : choisir le nom du fichier
        if choix == "1":
            nom_fichier = input("Saisissez le Nom de fichier :")
            fichier = open("data/" + nom_fichier + ".txt", 'at')

        # Cas 2 : Ajouter du texte
        elif choix == "2":
            try:
                fichier
            except NameError:
                raise ValueError
            else:
                saisie = input("Saisissez un texte :")
                fichier.write(saisie + "\n")
                fichier.flush()

        # Cas 3 : Afficher le contenu du fichier
        elif choix == "3":
            try:
                fichier
            except NameError:
                raise ValueError
            else:
                # d'abord on ouvre le fichier puis on le lit en utilisant la fonction read()
                allTextFile = open("data/" + nom_fichier + ".txt", 'r').read()
                print(allTextFile)

        # Cas 4 : Vider le fichier
        elif choix == "4":
            try:
                fichier
            except NameError:
                raise ValueError
            else:
                open(nom_fichier + ".txt", 'w')
                print("Le fichier " + nom_fichier + " est vide")


    except ValueError:
        print("\nVeuillez sélectionner un fichier")
        input("(entrer pour continuer)")

    if choix == "9":
        exit(0)
    choix = menu(nom_fichier)

nameFile = "fichetu.csv"
etudiants = []
with open(nameFile, "rt") as fic:
    for line in fic:
        info = line.split(';')
        prenom = info[0]
        nom = info[1]
        dateN = info[2]
        etudiants.append((Etudiant(prenom, nom, dateN)))
