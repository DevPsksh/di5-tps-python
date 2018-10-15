#!/usr/bin/python3
import cgi

form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")
print(form.getvalue("name"))
print(form.getvalue("password"))
html = """<!DOCTYPE html>
<head>
    <title>Mon programme</title>
</head>
<body>
    <form action="/index.py" method="post">
        <input type="text" name="name" value="Votre nom" />
        <input type="text" name="password" value="Votre mot de passe" />
        <input type="submit" name="send" value="Envoyer information au serveur">
    </form>
</body>
</html>
"""
print(html)
