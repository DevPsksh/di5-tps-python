class Date:

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __eq__(self, other):
        return self.year == other.year and self.month == other.month and self.day == other.day

    def __lt__(self, other):
        if self.year == other.year:
            if self.month == other.month:
                return self.day < other.day
            else:
                return self.month < other.month
        else:
            return self.year < other.year

    def __str__(self):
        return self.day + "/" + self.month + "/" + self.year


class Etudiant:

    def __init__(self, prenom, nom, birthdate):
        self.prenom = prenom
        self.nom = nom
        self.birthdate = birthdate

    def adresselec(self):
        return self.prenom + '.' + self.nom + "@etu.univ-tours.fr"

    def age(self):
        return self.age


ETUDIANTS = []

with (open("fichetu.csv", "r")) as file:
    for line in file.readlines():
        line = line[:-1]
        split = line.split(";")
        dateSplit = split[2].split("/")
        etu = Etudiant(split[0], split[1], Date(dateSplit[2], dateSplit[1], dateSplit[0]))
        ETUDIANTS.append(etu)

for etu in ETUDIANTS:
    print(etu.prenom, etu.nom, etu.birthdate)
