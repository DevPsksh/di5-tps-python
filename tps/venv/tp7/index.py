#!/usr/bin/python3
import cgi

form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")

print(form.getvalue("name"))

html = """<!DOCTYPE html>
<head>
    <title>Mon programme</title>
</head>
<body>
    <h2> Login Page </h2>
    <form action="/index.py" method="post">
        <label> Utilisateur </label>
        <input type="text" name="Nom d'utilisateur">
        <label> Mot de passe </label>
        <input type="password" name="Mot de passe">
        <input type="submit" name="send" value="S'inscrire">
    </form>
    <br>
    <a href ="creerUtilisateur.py">Créer l'utilisateur</a> 
</body>
</html>
"""

print(html)