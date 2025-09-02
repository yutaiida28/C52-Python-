# Méthode a pratiquer lors de programation 
# DRY Dont Repeat Yourself éviter toute repetition de code 
# CALTAL Code A Little Test A Little code bout par bout teste a chaque fois que jai la chance 
# UMUD  U Must Use Debugger
from copy import deepcopy
# les varriable immuable 
#entier  int?
#a = 1 # en python a est un alience qui point sur 1 en memoir la valeur de 1 nes pas immuable si on dit a = 3 a change ca destination de 1 a 3 qui serra allouer a une nouvelle position dans la memoir q 
#float
# b = 3.14
#complex
#str
#boolen
#none type
#byte
#  muable 
#byte array un peux different du byte 

#format string 
print(f'')

#  4 structure de donnee fondamentale
        #|MUTABLE
# list    #| oui 
# tuple   #| non
# set     #| oui
# dict    #| oui 

# Nom                   # type | Mutable    |Subscriptable[read/write]  | Iterable peut etre dans une boucle 
# Nom                   # type | Modifiable |Indexable[lect./ecrit.]    | Iterable  | doublon  
my_str = "allo"         # str  | 0        | [1/0] par position        | 1           | 1
my_list = [0,-1,20,7,46]   # list | 1        | [1/1] par position        | 1           | 1
my_tuple = (0,1,2,3,4)  # tuple| 0        | [1/0] par position        | 1           | 1
my_set = {0,1,2,3,4}    # set  | 1        | [0/0]                     | 1           | 0
my_dicti = {0: 'zero',  # list | 1        | [1/1] par la cle          | 1           | [0:1]
            1: 'one',
            'two': 2,
            3: '...'}     

#indexation ++ => slicing
my_list[0] = 10
my_list[0] = 10
# my_list[13] = 10
#f9 pour rajouter un point  f5 pour lancer le debugeur
print(my_list[-1])
# lorsque on commencepar 0 on est sur du zerobass (donc commence a zero ) 
# lorsque on commence de la fin on devien one basse (donc on commence a conter de maniere a -1 )  

#indexation ++ => slicing
#[from: to] #le to est exclu
print(my_list[1:3]) #donc on commence a 1 pis fini a 2 car le 3 est exclusif
print(my_list[0:1])
print(my_list[3:10])
print(my_list[:4]) # rien dans le from => 0
print(my_list[2:]) #rien dans le to => le dernier  ...
print(my_list[2:-1])
print(my_list[:])
#[from: to : strep(mot juste stride) ] #le to est exclu
print(my_list[0:4:2])
print(my_list[4:1:-1]) 
print(my_list[4::-2]) # si le to n'est pas specifier le dernier est inclue ( premier )  
pass

# Iterateur
for value in my_list:
    print(value)

# n = input("veillez saisir un entier")
n = 2
#for i in range(n): #ici on se serre pas du i don on le retire 
#    print("allo") 
for _ in range(n):
    print("allo") 

my_list = [1,2,3]
my_str = 'ZUT'
for info in zip(my_list, my_str): # info est un tupple qui contien my_list, my_str
    print(info[0]* info[0])
for n, char in zip(my_list, my_str):
    print(char * n)

colors = ('red','blue','yellow') #cest un tuple
for i,color in enumerate(colors):  #cree un nouveaux objet iterable avec enumerate
    print(i +1,' ', color)


data = { 123:'Marcel'
        ,456:'Eric'
        ,789:'Jean-Marc'
        ,666:'Jean-Christophe'}
for k in data: # ne parcour que les cles
    print(k)
for v in data.values(): # ne parcour que les cles
    print(v)
for k,v in data.items(): # ne parcour que les cles
    print(k, ' ~ ', v)

nom, prenom = 'labonte', 'eric' #fontionnel

# Creation de liste 
# 1 liste vide
a = []
a = list() 

#Construction avec valeurs
# 2a construction manuel 
a = []
for value in range(10,22,3):
    if value % 2 == 0: #verifier si cest un nombre pair  
        a.append(value)

# 2b construction avec iterateur
a = list(range(10))
a = list(data) #ca marche car un dictionnaire c'est iterable cependent ici on vois les cles 
a = list(data.values())
a = list(data.items())

# 2c literal
a = [0,10,20]

# 2d
a = '- ' * 40
pass
a = [10] * 5
a = [None] * 5 #il vas avoir 5 fois le None
pass

# 2e comprehention list 
# a = []
# for value in range(10,22,3):
#     if value % 2 == 0: #verifier si cest un nombre pair  
#         a.append(value)
a = [value for value in range(10) if value %2 == 0]
#          _________for__________
#    _____ apend
# conditionnel                   _________________
a = [value ** 2 for value in range(10)]
a = [char for char in 'Python']
a = [-1 for value in range(10)]
a = [[0, 'allo', 3.14]for _ in range(10)]
pass

#reference, garbage collector et concepts relies

def show(v1,v2):
    print(v1,' - ', v2, hex(id(v1), id(v2)))

a = 5
b = 10
show(a,b)
b = 5
# ici le garbege collector sai que le 5 existe deja donc aulieux de recrer un nouvelle valeur 5 on prend le meme que celui du a 

a = 'Hello'
b = a + ' World'
show(a,b)


a = [value ** 2 for i in range(10) if i %2]
b = a 
show(a,b)
# 3 type de copy
# ref copy
# shallow copy
# deep copy

b[1] = 100
show(a,b) 

#la fonction .copy  elle copy un liste (un nouvelle )

#Cahngement de sujet 
a = (1,2,3,4)
# a[0] = 1000 #impossible
a = ([0,1],[2,3])
a[0][1] = 1000 #ca fonctionne car dans le tuple il ya un tableau qui nest pas immuable 


#f-string
a = 11 
b = 3.14
print(f'ici du text ')
print(f'a =  {a} \npi = {b}')
print(f'pi =  {a * b}')
print(f'{a = }') #remplacement pour un print 
print(f'{a:10}') # rajouter 10 d'espaces
print(f' {a:>10}') #alignement a droite avec la fleche 
print(f'pi =  {a:.<10}') #space filed with bunch off .

print(f'{b:>10.4f}') #le 4f c'est pour 4 decimal apres le point 

#--------------------------------------------pep8
#variable fonction module en snake_case 
#class PascalCase
#const UPPER_SNAKE_CASE