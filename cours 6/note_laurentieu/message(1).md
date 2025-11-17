```
# gol_engine interieur GOLEngine
# gol_app interieur gol = GOlEngine()

# from gol_engine import GOLEngine

# si on veut faire une nouvelle version on peut la saccager mais on veut faire un backup

# suggestion difference, prendre le ficheirgol_engine et faire un copier coller et recoppier le fichier en gol_engine_np et la classe on l appelle GOLEngine, deux fichier different deux fois la mm classe, l impact dans le projet principal,

# dans gol_app, dans l import on remplace fait gol_engine_np, mais dans le constructeur dans gol engine np le x grid= [[]] on vas creer x grid = ndarray, on ne fait plus de double boucle for mais comme en np, la bordure qui est toujours a 0

# on vectorise tout

# si le client vuet voir un exemple alors on peut juste import l ancien gol_engine, cela s appele du *doc typing*

# une portion du code doit changer, tout est facile sauf la fonction process

# on a deux matrice une pour ecrire et une pour lire
# pour chacun des points on doit voir les 8 voisins etc. l algo
# est ce que ca se vectorise ? etre en n dimension c est un probleme, ca veut dire simplifire le probleme, si jamais t es en 1d pi on applique la mm logique a quoi on s attends

0   1  2  3  4  5  6 etc.
# g
==============================================
|0||0||0||0||1||1||1||0||0||1||0||1||0||1||0|
==============================================

# n
==============================================
|0||0||0||1||1||2||1||1||1||1||0||1||0||1||0|   np.zeros(g.shape)
==============================================
x------------------------------------------x
                center

==============================================
|0||0||0||1||1||2||1||1||1||1||0||1||0||1||0|
==============================================
--------------------------------------------x 
                left

==============================================
|0||0||0||1||1||2||1||1||1||1||0||1||0||1||0|
==============================================
x--------------------------------------------
                right

# examen
# comment modifier les donner sans compter les bordures

# chacune des valeur a besoin de celui de gauche et celui de droite

# gi --> gi-1 et gi+1

# left = g[0: -2]
# right = g[2: ]
# center = g[1: -1] donne la matrice sans les bordures

# creer trois sousmatrice
# n[1:-1] = left + right
# out = nouvelle matrice avec le resultat dedans
==============================================
|0||0||0||0||0||0||0||0||0||0||0||0||0||0||0|
==============================================
                    out

# nn ENSEMBLE [0, 1, 2]

            mort, vivant, mort (si  0 voisin vivant)
# alive_rule = [0, 1, 1]

# est ce que a la position 0 je suis mort ou vivant

```