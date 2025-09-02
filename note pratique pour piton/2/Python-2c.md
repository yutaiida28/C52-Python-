
# Introduction à Python - Cours 2

## Partie 2c

# Devoir

- Devoir 2 :
    - Créer un module `shapes.py` qui contient les classes suivantes :
        - `Shape` : classe de base _abstraite_ pour toutes les formes géométriques. Elle doit avoir les méthodes suivantes :
            - `bounding_box_width()` qui retourne la largeur de la forme
            - `bounding_box_height()` qui retourne la hauteur de la forme
            - `area()` qui calcule et retourne l'aire de la forme
            - `perimeter()` qui calcule et retourne le périmètre de la forme (optionnel)
            - `to_string(shape_char = '*', background_char = ' ')` qui retourne la forme sous forme de caractères. Par exemple :
                - pour un rectangle de 30 x 3 :
                ```
                ******************************
                ******************************
                ******************************
                ```
                - pour un triangle rectangle de base 15 et de hauteur 7 :
                ```
                **
                ****
                ******
                *********
                ***********
                *************
                ***************
                ```
            - toutes les classes héritant de `Shape` doivent implémenter les 5 méthodes mentionnées ci-dessus.
        - `Square` représente un carré (hérite de `Shape`) :
            - la classe possède un attribut `side` pour la longueur du côté du carré
        - `Rectangle` représente un rectangle (hérite de `Shape`) :
            - la classe possède des attributs `width` et `height` pour la largeur et la hauteur du rectangle
        - `RectTriangle` représente un triangle rectangle (hérite de `Shape`) :
            - la classe possède des attributs `width` et `height` pour la largeur et la hauteur du triangle rectangle
        - `Circle` représente un cercle (hérite de `Shape`) :
            - la classe possède un attribut `radius` pour le rayon du cercle
        - Créer une fonction utilitaire nommée qui crée aléatoirement des forme nommée `create_random_shape(size = 0)`.
            - La fonction détermine aléatoirement laquelle des 4 formes elle créera.
            - le paramètre `size` détermine la taille de la forme. Pour les formes non symétriques, l'autre dimention doit être de `1/2 size`. Si `size <= 0`, `size` est déterminée aléatoirement dans l'intervalle [5, 15].
            - Retourne l'objet de la forme créée.
    - Créer un fichier `main.py` qui :
        - crée 10 instances aléatoires de formes et les insère dans une liste
        - pour chacune des formes, on affiche :
            - la forme en chaîne de caractèrs (bonus, ajouter un encadré)
            - les informations de chaque forme (aire, périmètre, dimensions, etc.)
        - affiche les informations globales suivantes :
            - le nombre de formes
            - la somme des aires
            - la somme des périmètres
        - En bonus, créer une image de 80 x 30 caractères et superposer toutes les formes en leur donnant des position aléatoires et afficher l'image dans la console. Utiliser le caractère espace `' '` pour le fond. Si une forme dépasse les limites de l'image, elle est tronquée.

    