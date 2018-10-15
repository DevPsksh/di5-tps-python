import sys

print("Bonjour tout le monde")

FILE = None

while True:
    print("1. Choisir un nom de fichier")
    print("2. Ajouter une texte")
    print("3. Afficher le fichier complet")
    print("4. Vider le fichier")
    print("9. Quitter")

    answer = sys.stdin.readline()[:-1]

    if answer == "1":
        print("Tapez le nom du fichier")
        FILE = open(sys.stdin.readline()[:-1], "a+")
    elif answer == "2":
        print("Tapez le text a ajouter")
        tmp = sys.stdin.readline()[:-1]
        print("Got [" + tmp + "]")
        FILE.write(tmp)
    elif answer == "3":
        tmp = FILE.read()
        print(tmp)
    elif answer == "4":
        FILE.truncate(0)
    elif answer == "9":
        FILE.close()
        exit(0)
    else:
        exit(-5)

    print("\n\n\n\n\n")
