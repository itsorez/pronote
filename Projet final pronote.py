'''
Projet gestion classe Flavien
'''



classes = {}  # Dictionnaire des classes

'''
fonction qui permets de creér une classe
>>> gestion_classe("SIGMA")
   Classe SIGMA créée.
'''

def gestion_classe(nom_classe):
    nom_classe = nom_classe.upper()
    if nom_classe not in classes:
        classes[nom_classe] = {}  # Chaque classe est un dictionnaire vide
        print(f"Classe {nom_classe} créée.")
    else:
        print("Cette classe existe déjà.")


"""
Fonction qui permets d'ajouter un éléve a une classe
>>> ajouter_eleve("SIGMA" , "NATHAN")
Élève NATHAN ajouté à la classe SIGMA.
"""



def ajouter_eleve(nom_classe: str, nom: str):
    nom = nom.upper()
    if nom_classe in classes:
        classe = classes[nom_classe]
        if nom not in classe:
            classe[nom] = []
            print(f"Élève {nom} ajouté à la classe {nom_classe}.")
        else:
            print("Cet élève est déjà inscrit dans cette classe.")
    else:
        print("Cette classe n'existe pas.")

"""
Fonction qui permets d'ajouter une note a une classe et de ne pas pénaliser les éléves absents

>>> ajouter_note("SIGMA")
NATHAN Présent ? (Oui/Non): Oui
, note : 14
, coefficient : 2
"""
def ajouter_note(nom_classe: str):
    if nom_classe in classes:
        classe = classes[nom_classe]
        for eleve in classe:
            while True:
                print(eleve, end=" ")
                presence = input("Présent ? (Oui/Non): ").strip().lower()
                if presence == "non":
                    classe[eleve].append((-1, 0))  # Absent avec note -1 et coefficient 0
                    print("Eleve non noté ") 
                    break
                else:
                    note = round(float(input(", note : ")), 2)
                    coefficient = round(float(input(", coefficient : ")), 2)
                    if 0 <= coefficient <= 100:
                        classe[eleve].append((note, coefficient))
                        break
    else:
        print("Cette classe n'existe pas.")


"""
Fonction qui calcule la moyenne pondérée d'une classe
>>> calculer_moyenne("SIGMA")
NATHAN moyenne : 14.0

Moyenne générale de la classe : 14.0
"""
def calculer_moyenne(nom_classe: str):
    if nom_classe in classes:
        classe = classes[nom_classe]
        total_eleves = len(classe)
        total_moyenne = 0.0

        for eleve in classe:
            moyenne = 0.0
            total_coefficients = 0.0

            for note, coefficient in classe[eleve]:
                if note != -1:  
                    moyenne += note * coefficient
                    total_coefficients += coefficient

            if total_coefficients != 0:
                moyenne /= total_coefficients

            total_moyenne += moyenne
            print(eleve, "moyenne :", round(moyenne, 2))

        if total_eleves != 0:
            moyenne_generale = total_moyenne / total_eleves
            print("\nMoyenne générale de la classe :", round(moyenne_generale, 2))
        else:
            print("\nLa classe est vide.")
    else:
        print("Cette classe n'existe pas.")


'''
cette fonction permet de modifier une note rentrée précedemment en rentrant
le nom de l'éléve ,sa classe, le nombre de la note et la note
>>> modifier_note("SIGMA" , "NATHAN" , 0 , 14 )
NATHAN , note : 13
Note à modifier : (14.0, 2.0)
Note changée en : 13.0
   '''
def modifier_note(nom_classe: str, nom: str, numero, note):
    if nom_classe in classes:
        classe = classes[nom_classe]
        if nom in classe:
            if numero > len(classe[nom]) - 1:
                print("Impossible, pas assez de notes")
                return
        else:
            print("Impossible, l'élève n'est pas dans la classe")
            return

        if note != -1 or not (0 <= note <= 20):
            while True:
                print(nom, end=" ")
                note = round(float(input(", note : ")), 2)
                if note == -1 or (0 <= note <= 20):
                    break

        reponse = ""
        if nom in classe:
            while True:
                print("Note à modifier :", classe[nom][numero])
                print("Note changée en :", note)
                break
        else:
            print(nom, "n'est pas dans la classe")
    else:
        print("Cette classe n'existe pas.")

"""
Fonction qui permets de supprimer une note a une classe
>>> supprimer_note("SIGMA" , 0 )
Note suprimée
"""
def supprimer_note(nom_classe: str, numero_note):
    if nom_classe in classes:
        classe = classes[nom_classe]
        for eleve in classe:
            if 0 <= numero_note <= len(classe[eleve]) - 1:
                del classe[eleve][numero_note]
                print("Note suprimée")
            else:
                print("Le numéro de note spécifié est invalide.")
    else:
        print("Cette classe n'existe pas.")

"""
Fonction qui permets de voir les notes d'une classe
>>> voir_note("SIGMA")
NATHAN (13.0, 2.0) 
"""

def voir_note(nom_classe: str):
    if nom_classe in classes:
        classe = classes[nom_classe]
        for eleve in classe:
            taille = len(classe[eleve])
            print(eleve, end=" ")
            for note in classe[eleve]:
                print(note, end=" ")
    else:
        print("Cette classe n'existe pas.")




    """
    Visualiser les classes ainsi que les éléves de ces classes
>>> voir_classe()
Classe : SIGMA
1. NATHAN - Notes : [(13.0, 2.0)]
    """
def voir_classe():
    for nom_classe, classe in classes.items():
        print(f"Classe : {nom_classe}")
        for rang, (eleve, notes) in enumerate(classe.items(), start=1):
            print(f"{rang}. {eleve} - Notes : {notes}")
        print()  # Ligne vide pour séparer les classes

        
'''
Fonction qui écrit dans le fichier classe
'''

def ecrire_classe():
    fichier = open("ma_classe.don", "w", encoding="utf8")
    for nom_classe, classe in classes.items():
        fichier.write(f"Classe : {nom_classe}\n")
        fichier.write(f"Nombre élèves : {len(classe)}\n")
        for eleve, notes in classe.items():
            fichier.write(f"{eleve} : {notes}\n")
    fichier.close()

      
def lire_classe():
    """
    Lire sur le disque le dictionnaire classe
    Chargement en mémoire vive du dictionnaire
    """
    try:
        with open("ma_classe.don", "r", encoding="utf8") as fichier:
            classes.clear()
            while True:
                nom_classe = fichier.readline().strip()
                if not nom_classe:
                    break  # Fin du fichier

                if nom_classe.startswith("Nombre élèves"):
                    fichier.readline()  
                    fichier.readline()  
                    continue

                if not nom_classe.isdigit():
                    continue  # Si ce n'est pas un nombre, passer à la prochaine ligne

                taille = int(nom_classe)  
                nombre = int(fichier.readline().strip())  

                classe = {}
                for _ in range(taille):
                    eleve = fichier.readline().strip()
                    notes = eval(fichier.readline().strip())
                    classe[eleve] = notes

                classes[nom_classe] = classe

            print("Classes chargées avec succès !")
    except FileNotFoundError:
        print("Le fichier n'existe pas.")


'''
fonction qui crée le menu de l'application de gestion de notes grace a des chiffres de 0 à 11
si la saisie est autre qu'un  chiffre compris entre 0 et 11 , le programme demande une saisie correcte
>>> app()
   Menu:
 1. Ajouter un éléve
 2. Ajouter les notes
 3. Modifier une note
 4. Supprimer une note
 5.Voir les notes
 6.Afficher la moyenne pondérée
 7.Ecrire dans le fichier classe
 8.Voir le fichier classe
 9.Lire le fichier classe
 10.Quitter
 Choisissez une option (1-11) : 
'''
def app():
    while True:
        print("\nMenu : ")
        print("1. Créer une classe")
        print("2. Ajouter un éléve")
        print("3. Ajouter une note")
        print("4. Modifier une note")
        print("5. Supprimer une note")
        print("6. Voir les notes")
        print("7. Calculer la moyenne pondérée")
        print("8. Ecrire dans le fichier classe")
        print("9. Voir le fichier classe")
        print("10. Lire le fichier classe")
        print("11. Quitter")
         
        choix = input("Choisissez une option (1-11) : ")
        if choix == "1":
            nom_classe = str(input("Entrez un nom de classe : "))
            ajtclasse = gestion_classe(nom_classe)
        elif choix == "2" :
            nom_classe = input("Entrez le nom de la classe :")
            nom = input("Entrez un nom :")
            ajteleve = ajouter_eleve(nom_classe , nom)
        elif choix == "3":
            notes = ajouter_note(nom_classe)
        elif choix == "4":
            nom_classe = input("Entrez le nom de la classe : " )
            nom = str(input("Entrez le nom : "))
            numero = int(input("Entrez le numero : "))
            note = int(input("Entrez la note : "))
            modifnotes = modifier_note(nom_classe,nom,numero,note)
        elif choix == "5":
            nom_classe = input("Entrez le nom de la classe : ")
            nom = str(input("Entrez le nom de l'éléve :"))
            numero_note = int(input("Entrez le numéro de la note : "))
            supprnote = supprimer_note(nom_classe , numero_note)
        elif choix == "6":
            nom_classe = input("Entrez le nom de la classe : " )
            voirnote = voir_note(nom_classe)
        elif choix == "7" :
            nom_classe = input("Entrez le nom de la classe : " )
            moyennepond = calculer_moyenne(nom_classe)
        elif choix == "8" :
            ecrire_classe()
        elif choix == "9" :
            voir_classe()
        elif choix == "10" :
            lire_classe()
        elif choix == "11":
            print("Au Revoir")
            break
        else:            
            print("Option invalide. Veuillez choisir une autre option.")
app()