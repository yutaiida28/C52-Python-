# le random n est pas aléatoire mais est généré grâce à un algorithme, donc si on trouve l algo on peut le trouver, mais il faut prendre des conditions de la vrai vie, comme un phénomène aléatoire ( pluie, vent etc ou des phénomènes quantiques ( on peut l acheter et la mettre dans le pc ))

# seed pour tester 


# numpy comment chercher la valeur a l inex

a[1][2] =  a[1,2]


a[1][2][2][2] = a[1, 2, 2 , 2]

# slice
# de 0 a 10 slice de 2, 0 compris 3 incompris

a[0:10:3] 

# 0 3 6 9, il pointe directement aux mm données. 

# multi slicing
a[0:10:3, 2 : 3]

a = arange(5) 

# premier crochet index, deuxieme liste python
# la taille ( shape ) 

b = a[ [True, True, False, True, False] ]

# nouvelle matrice, issue d'élément à élément
    -----------
b = |0 | 1 | 3|
    -----------

c = a[ [0, 3] ]

    -------
c = |0 | 3|
    -------

# ça ne créer pas de nouvelle matrice, mais la transforme

# question exam, diagonale d un cube

data[[0, 1, 2], [0, 1, 2], [0, 1, 2]]


# pythagore
np.sum((data1 - data2)**2, axis=0)**0.5
