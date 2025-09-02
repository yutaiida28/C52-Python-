# Exercice 1.1 : Devinez un nombre (avec essais limités)
# Le programme possède un nombre secret défini dans le code par la variable number dans l'intervalle [0, 100] (par exemple, 42).
# L'utilisateur a cinq essais pour le deviner.
# Après chaque essai, le programme indique si le nombre à deviner est "Plus haut" ou "Plus bas".
# Le jeu se termine si l'utilisateur trouve le nombre ou s'il n'a plus d'essais.

# import random
# trouve = False
# nbrMistere = int(random.randint(0, 100))
# # tentative = 5
# tentative = int(5)
# print(nbrMistere)
# while not trouve:
    
#     nbrInscrit = input(f"deviner le nombre mister il vois reste {tentative} tentative :")
#     if nbrInscrit.isdigit():
#         chiffre = int(nbrInscrit)
#         if chiffre == nbrMistere:
#             trouve = True
#         else:
#             if chiffre < nbrMistere:
#                 print("la valeur du nombre mister est plus grande")
#                 tentative -= 1
#             elif chiffre > nbrMistere:
#                 print("la valeur du nombre mister est plus petit")
#                 tentative -= 1
#             if tentative == 0:
#                 print("le nombre de tentative est a 0 domage")
#                 break


# Exercice 1.3 : Table de multiplication

# Demandez à l'utilisateur d'entrer deux nombres entiers entre 2 et 10 (en 2 saisies distinctes).
# Affichez la table de multiplication de ces nombres.
# valide = False
# while not valide:
#     premier_nombre = float (input("le premier chiffre: "))
#     if 2 <= premier_nombre <=10:
#         dernier_nombre = float (input("la deuxiem valeur: "))
#         if 2 <= dernier_nombre <=10:
#             for i in range(10):
#                 print(f"{int(premier_nombre)} x {i} = {int(premier_nombre * i)}")
#             for j in range(10):
#                 print(f"{int(dernier_nombre)} x {j} = {int(dernier_nombre * i)}")
#         else:
#             print("rentrer un nombre valide")
#     else:
#         print("rentrer un nombre valide")

# Exercice 1.4 : Trier simplement trois nombres (sans fonctions ni collections)

# Objectif. Afficher trois entiers saisis en ordre croissant sans utiliser de liste ni la fonction sorted(...).
# Demander à l'usager de saisir trois entiers a, b et c (en 3 saisies distinctes).
# Réordonner ces trois entiers en ordre croissant.
# Afficher sur trois lignes :
# les trois entiers dans l'ordre saisies
# les trois entiers en ordre croissant sur une seule ligne
# si les trois variables sont strictement différentes les unes des autres, afficher Strict sinon afficher Non-strict

a = input("la valeur a :")
b = input("la valeur b :")
c = input("la valeur c :")

print(f"en ordre saisies {a},{b},{c}")

if a <= b:
    if a <= c:
        if b <= c:
            print("en ordre croissan a,b,c")
        else:
            print("en ordre croissan a,c,b")
    else:
        print("en ordre croissan c,a,b")
else:
    if b <= c:
        if c <= a:
            print("en ordre croissan b,c,a")
        else:
            print("en ordre croissan b,a,c")
    else:
        print("en ordre croissan c,b,a")

if a == b == c:
    print("Strict")
else:
    print("Non-strict")
    