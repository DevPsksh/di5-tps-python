import hashlib
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
import csv

choix = ""
with open('data/users', 'rt') as fin:
    dr = csv.DictReader(fin, delimiter=';')
    users = [(i['login'], i['password']) for i in dr]


def checkLoging(login):
    for user in users:
        if user[0] == login:
            return 1
    return 0


def getUser(login):
    for user in users:
        if user[0] == login:
            return user
    return 0


def passwordCheking(user, password):
    encryptedUserPassword, salt = user[1].split(':')
    encryptedPasswordSha256 = hashlib.sha256(salt.encode() + password.encode()).hexdigest()
    if encryptedUserPassword == encryptedPasswordSha256:
        return 1
    return 0


def encryptPassword(password):
    aesKey = get_random_bytes(16).hex()
    return hashlib.sha256(aesKey.encode() + password.encode()).hexdigest() + ':' + aesKey


while choix != "5":
    print("\nMenu principale")
    print("1. Créer un utilisateur")
    print("2. Créer un fichier (si utilisateur existant)")
    print("3. Editer un fichier (si utilisateur existant)")
    print("4. Afficher le contenu d'un fichier (si utilisateur existant)")
    print("5. Quitter le programme")
    choix = input("Veuillez choisir le numéro souhaité : ")

    if choix == "1":
        login = input("Veuillez saisir un login : ")
        if checkLoging(login):
            print("\nLe login existe déjà")
            input("(Appuiyez entrer pour continuer)")

        else:
            password = input("Veuillez saisir un mot de passe : ")
            checkPassword = input("Veuillez confirmer votre mot de passe : ")
            if password != checkPassword:
                print("\nLes mots de passe ne correspondent pas, veuillez recommencer")
                input("(Appuiyez entrer pour continuer)")
            else:
                encryptedPassword = encryptPassword(password)
                usersFile = open('data/users', 'at')
                usersFile.write("\n" + login + ";" + encryptedPassword)
                usersFile.close()
                users.append((login, encryptedPassword))
                print("\nVotre compte a été créé")
                input("(entrer pour continuer)")

    if choix == "2":
        login = input("Veuillez saisir votre login : ")
        password = input("Veuillez saisir votre mot de passe : ")
        user = getUser(login)
        if user != 0 and passwordCheking(user, password):
            fileName = input("Veuillez saisir le nom du fichier à créer : ")
            data = input("Veuillez saisir le texte :\n")
            aesKey = user[1].split(':')[1]
            aes = AES.new(bytes(aesKey.encode()), AES.MODE_EAX)
            aesText, tag = aes.encrypt_and_digest(data.encode())
            file = open("data/" + fileName, "ab")
            for x in (aes.nonce, tag, aesText):
                file.write(x)
            file.close()
        else:
            print("\n login/mot de passe n'existe pas")
            input("(Appuiyez entrer pour continuer)")

    if choix == "3":
        login = input("Veuillez saisir votre login : ")
        password = input("Veuillez saisir votre mot de passe : ")
        user = getUser(login)
        if user != 0 and passwordCheking(user, password):
            fileName = input("Veuillez saisir le nom du fichier à éditer : ")
            try:
                file = open("data/" + fileName, "r")
                data = input("Veuillez saisir le texte à ajouter :\n")
                aesKey = user[1].split(':')[1]
                aes = AES.new(bytes(aesKey.encode()), AES.MODE_EAX)
                aesText, tag = aes.encrypt_and_digest(data.encode())
                file = open("data/" + fileName, "wb")
                for x in (aes.nonce, tag, aesText):
                    file.write(x)

            except FileNotFoundError:
                print("\nLe fichier " + fileName + " n'existe pas, veuillez le créer")
                input("(entrer pour continuer)")
            finally:
                file.close()

        else:
            print("\nLe couple login/mot de passe n'existe pas")
            input("(entrer pour continuer)")

    if choix == "4":
        login = input("Veuillez saisir votre login : ")
        password = input("Veuillez saisir votre mot de passe : ")
        user = getUser(login)
        if user != 0 and passwordCheking(user, password):
            fileName = input("Veuillez saisir le nom du fichier à afficher : ")
            try:
                file = open("data/" + fileName, "rb")
                nonce, tag, aesText = [file.read(x) for x in (16, 16, -1)]
                aesKey = user[1].split(':')[1]
                aes = AES.new(bytes(aesKey.encode()), AES.MODE_EAX, nonce)
                data = aes.decrypt_and_verify(aesText, tag)
                print("\nContenu du fichier " + fileName + " :\n" + str(data))
            except FileNotFoundError:
                print("\nLe fichier " + fileName + " n'existe pas, veuillez le créer")
                input("(entrer pour continuer)")
            finally:
                file.close()

        else:
            print("\nLe couple login/mot de passe n'existe pas")
            input("(entrer pour continuer)")
