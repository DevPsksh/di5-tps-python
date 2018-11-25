import cgi
import hashlib
import csv

user = ""

with open('data/users', 'rt') as fin:
    dr = csv.DictReader(fin, delimiter=';')
    users = [(i['login'], i['password'], 0) for i in dr]


def getUser(username):
    for user in users:
        if user[0] == username:
            return user
    return 0


def passwordCheking(user, password):
    encryptedUserPassword, salt = user[1].split(':')
    encryptedPassword = hashlib.sha256(salt.encode() + password.encode()).hexdigest()
    if encryptedUserPassword == encryptedPassword:
        return 1
    return 0


def logUserIn(username, password):
    user = getUser(username)
    if user:
        if passwordCheking(user, password):
            return user
        else:
            return 0
    else:
        return 0


form = cgi.FieldStorage()

username = form.getvalue("username")
password = form.getvalue("password")
logout = form.getvalue("logout")

if logout:
    user = ""
    username = ""
    password = ""

html = """
<!DOCTYPE html>
    <head>
        <title>Mon programme</title>
    </head>
    <body>
        <h3>Login page</h3>
        <form action="/index.py" method="post">
            <label>Username</label>
            <input type="text" name="username"/><br><br>
            <label>Password</label>
            <input type="password" name="password"/><br><br>
            <input type="submit" name="send" value="Login">
        </form>
        <br><br>"""


if username and password:
    user = logUserIn(username, password)
    if user == 0:
        html += """<label>Ce couple login/mot de passe n'existe pas</label>"""
    else:
        html = """
            <!DOCTYPE html>
                <head>
                    <title>Mon programme</title>
                </head>
                <body>
                    <h3>User page</h3>
                    <label>""" + user[0] + """</label><br><br>
                    <form action="/index.py" method="post">
                        <input type="hidden" name="logout" value="true">
                        <input type="submit" name="send" value="Logout">
                    </form>
                </body>
            </html>
            """
        print("Content-type: text/html; charset=utf-8\n")
        print(html)
        exit(0)

html += """
            <br><br>
            <a href="create_user.py">Créer un utilisateur</a>
        </body>
    </html>"""

print("Content-type: text/html; charset=utf-8\n")
print(html)
