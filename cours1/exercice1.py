import random
#exercice 1#########################################################################
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

#exercice 1.2#######################################################
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
my_liste = [2,3,4,5,6,7,8,9,]
print("afficheur de table mathematic")
premier_nombre=1
deuxiem_nombre=1
valide = False
while valide == False :
    premier_nombre = float (input("le premier chifre entre 2 et 10 "))
    if premier_nombre in my_liste:
        deuxiem_nombre = float (input("le deuxiem chifre entre 2 et 10 "))
        if deuxiem_nombre in my_liste:
            valide = True

   


