import random
#exercice 1
# hidden_number = random.randrange(0,100)
# guess = 5
# found = False
# print (hidden_number)
# print("guess the hidden number you got 5 try")
# trycounter = int(0)
# while not found or trycounter :
#     trycounter+=1
#     guessed_number = float (input(f"what is your {trycounter}st guess:"))
#     if(trycounter >= guess):
#         print("you didnt guessed it in the range ")
#         break
#     elif(guessed_number == hidden_number):
#         print(f"WaW! you got it right on the {trycounter}st try")
#         found = True
#     else:
#         print("\nnice try let me give you a hint...")
#         if(guessed_number < hidden_number):
#             print("the hidden nuber is bigger then your guess")
#         else:
#             print("the hidden nuber is smaler then your guess")

#exercice 1.2
# print("Callculatrice simple")

# premier_nombre = float (input("le premier chiffre: "))
# operation =  str (input("l'operations a faire: "))
# dernier_nombre = float (input("la deuxiem valeur: "))

# print(f"voici l'equation {premier_nombre} {operation} {dernier_nombre} = ...")
# if(operation == "+"):
#     print(premier_nombre + dernier_nombre)
# elif(operation == "-"):
#     print(premier_nombre - dernier_nombre)
# elif(operation == "*" or operation == "x"):
#     print(premier_nombre * dernier_nombre)
# elif(operation == "/"):
#     print(premier_nombre / dernier_nombre)

#     - Exercice 1.3 : Table de multiplication
#     - Demandez à l'utilisateur d'entrer deux nombres entiers entre 2 et 10 (en 2 saisies distinctes).
#     - Affichez la table de multiplication de ces nombres.

# - Exercice 1.4 : Trier simplement trois nombres (sans fonctions ni collections)
#     - Objectif. Afficher trois entiers saisis en ordre croissant sans utiliser de liste ni la fonction `sorted(...)`.
#     - Demander à l'usager de saisir trois entiers `a`, `b` et `c` (en 3 saisies distinctes).
#     - Réordonner ces trois entiers en ordre croissant.
#     - Afficher sur trois lignes :
#         - les trois entiers dans l'ordre saisies
#         - les trois entiers en ordre croissant sur une seule ligne
#         - si les trois variables sont strictement différentes les unes des autres, afficher `Strict` sinon afficher `Non-strict`