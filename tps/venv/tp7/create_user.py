import cgi
import hashlib
import csv
from Cryptodome.Random import get_random_bytes

with open('data/users', 'rt') as fin:
    dr = csv.DictReader(fin, delimiter=';')
    users = [(i['login'], i['password'], 0) for i in dr]


def checkUsername(username):
    for user in users:
        if user[0] == username:
            return 1
    return 0


def encryptPassword(password):
    aesKey = get_random_bytes(16).hex()
    return hashlib.sha256(aesKey.encode() + password.encode()).hexdigest() + ':' + aesKey


form = cgi.FieldStorage()

username = form.getvalue("username")
password = form.getvalue("password")
confirmPassword = form.getvalue("confirmPassword")


def createUser(username, password):
    encryptedPassword = encryptPassword(password)
    usersFile = open('data/users', 'at')
    usersFile.write("\n" + username + ";" + encryptedPassword)
    usersFile.close()
    users.append((username, encryptedPassword))

html = """
<!DOCTYPE html>
    <head>
        <title>Mon programme</title>
    </head>
    <body>
        <h3>Créer utilisateur</h3>
        <form action="/create_user.py" method="post">
            <label>Username : </label>
            <input type="text" name="username"/><br><br>
            <label>Password</label>
            <input type="password" name="password"/><br><br>
            <label>Confirm password</label>
            <input type="password" name="confirmPassword"/><br><br>
            <input type="submit" name="send" value="Créer utilisateur">
        </form><br><br>"""

if username and password and confirmPassword:
    if password == confirmPassword:
        if checkUsername(username):
            html += """<label>Ce nom utilisateur existe déjà</label>"""
        else:
            createUser(username, password)
            html += """<label>Votre compte a bien été enregistré</label>"""
    else:
        html += """<label>Les mots de passe de correspondent pas</label>"""

html += """
                <br><br>
                <a href="index.py">Login</a>
            </body>
        </html>"""
print("Content-type: text/html; charset=utf-8\n")
print(html)
