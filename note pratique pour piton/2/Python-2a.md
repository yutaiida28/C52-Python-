
# Introduction à Python - Cours 2

## Partie 2a

### Fonctions

- Le paradigme de programmation fonctionnelle est très important en Python
- Une fonction est un bloc de code réutilisable qui effectue une tâche spécifique
- Une fonction est définie à l'aide du mot-clé `def` suivi du nom de la fonction, des parenthèses et d'un deux-points `:`
- Une fonction peut prendre des paramètres en argument (déclarée entre parenthèses et considérée comme des variables locales)
- Les fonctions retournent toujours une valeur (à quelques exceptions près)
    - explicitement avec le mot-clé `return`
    - implicitement, si aucune valeur n'est retournée, ainsi la fonction retourne toujours `None`
- La syntaxe générale est la suivante :
```Python
# Exemple de définition de fonction

def nom_de_la_fonction_1():
    # bloc de code
    pass
    # retourne implicitement None

def nom_de_la_fonction_2(param1, param2):
    # bloc de code
    return valeur_de_retour

def print_hello():
    print("Hello, World!")

def add(a, b):
    resuilt = a + b
    return result
```
- Comme pour tous les autres langages, les fonctions peuvent être appelées en utilisant leur nom suivi de parenthèses et en passant les arguments requis
```Python
# Exemple d'appel de fonction

print_hello()
add(5, 10)
```

- Les fonctions peuvent également être définies avec des paramètres par défaut, ce qui permet de les appeler sans fournir tous les arguments

```Python
# Exemple de fonctions avec un paramètre par défaut

def add(a, b=0):
    return a + b

def print_message(message = "Hello, World!", count = 1):
    for _ in range(count):
        print(message)

# Exemple d'appel de fonction avec un paramètre par défaut
result = add(5, 10)  # b prend la valeur donnée de 10
result = add(5)  # b prend la valeur par défaut de 0

print_message()  # affiche "Hello, World!" une fois
print_message("Bonjour maman!")  # affiche "Bonjour maman!" une fois
print_message("Bonjour, le monde!", 3)  # affiche "Bonjour, le monde!" trois fois

```

- La surchage de fonction n'est pas supportée en Python. À la place, Python offre un modèle de passage d'arguments différents des autres langages, permettant différents types de passage d'argument. Nous y reviendrons dans d'autres cours.
- En informatique, les fonctions sont un sujet plus large qu'il n'y paraît. Python offre des fonctionnalités avancées que nous couvrirons plus en détail dans ce cours mais davantage à la prochaine session.
- Finalement, rappelez-vous toujours cet axiome `DRY` (_Don't Repeat Yourself_) : évitez de répéter le même code plusieurs fois, utilisez des fonctions pour encapsuler la logique réutilisable. Sauf dans quelques cas particuliers, il est largement préférable de ne pas répéter le même code plusieurs fois dans un programme. C'est la raison même des paradigmes de programmation procédurale, fonctionnelle et orientée objet (en partie)! 
    - Préférez-vous `DRY` ou `WET` (_Write Everything Twice_ ou _We Enjoy Typing_) ?
    - Évidemment, il y a quelques exceptions et nuances, mais en général, c'est une excellente règle! Surtout pour de jeunes programmeurs en situation d'apprentissage. 
    - Cette pratique demande un effort supplémentaire qui se développe au fil des années et qui est recherchée dans l'industrie (fonctions, structures, classes, ...).



### Modules

- Un module est un fichier Python contenant du code réutilisable, tel que des fonctions, des classes ou des variables.
- Les modules permettent de structurer le code en séparant les fonctionnalités en fichiers distincts, facilitant ainsi la réutilisation et la maintenance du code.
- Pour utiliser un module, il faut l'importer dans le script Python en utilisant le mot-clé `import` suivi du nom du module.
- Pour utiliser un élément spécifique du module dans le code, il faut préfixer le nom de l'élément par le nom du module suivi d'un point `.`. Par exemple, si le module s'appelle `math` et que l'on souhaite utiliser la fonction `sqrt`, on écrira `math.sqrt(9)`.
- Il est possible d'importer un module entier ou des éléments spécifiques d'un module en utilisant la syntaxe `from <module> import <element>`. Avec cette syntaxe, on peut utiliser directement l'élément sans préfixer par le nom du module. De plus, les autres éléments du module ne sont pas importés, ce qui peut être utile pour éviter les conflits de noms.
- Il est aussi possible d'utiliser un alias créé par le mot réservé `as` renommant le module ou l'élément importé, ce qui peut être utile pour éviter les conflits de noms ou pour simplifier le code. Par exemple, on peut écrire `import tkinter as tk` pour renommer le module `tkinter` en `tk`, et ensuite utiliser `tk` pour accéder aux éléments de ce module. Par exemple, `tk.Button()` au lieu de `tkinter.Button()`.

```Python
# Importation du module math

import math
result = math.sqrt(16)  # result vaut 4.0
```

```Python
# Importation spécifique de la fonction sqrt du module math

from math import sqrt
result = sqrt(25)  # result vaut 5.0
```

```Python
# Importation du module math avec un alias
import math as m
result = m.sqrt(36)  # result vaut 6.0
```

- Python dispose d'une vaste bibliothèque standard de modules intégrés, tels que `math`, `os`, `sys`, `random`, `datetime`, etc. Ces modules offrent des fonctionnalités variées pour effectuer des opérations mathématiques, manipuler des fichiers et des répertoires, générer des nombres aléatoires, travailler avec des dates et des heures, etc.
- Il est également possible d'installer des modules tiers à l'aide de gestionnaires de paquets tels que `pip`. Ces modules peuvent être trouvés sur le [Python Package Index (PyPI)](https://pypi.org/), qui est la principale source de bibliothèques Python.
- Il est également possible de créer ses propres modules en écrivant du code dans un fichier Python et en l'importer dans d'autres scripts. Pour cela, il suffit de créer un fichier avec l'extension `.py` contenant le code souhaité, puis de l'importer dans un autre script en utilisant le mot-clé `import` suivi du nom du fichier sans l'extension `.py`. Nous couvrirons ce sujet dans la prochaine partie.

- Quelques modules standards importants :
    - `math` : fournit des fonctions mathématiques de base comme `pi`, `sin`, `cos`, `tan`, `sqrt`, `pow`, `log`, `exp`, etc
    - `random` : permet de générer des nombres aléatoires
        - `random.random()` : génère un nombre à virgule flottante aléatoire entre 0 et 1 (la borne supérieure est excluse)
        - `random.randint(a, b)` : génère un entier aléatoire entre `a` et `b` (la borne supérieure est incluse)
        - `random.uniform(a, b)` : génère un nombre à virgule flottante aléatoire entre `a` et `b` (la borne supérieure est incluse)
        - `random.choice(sequence)` : choisit un élément aléatoire dans une séquence
    - `datetime` : permet de travailler avec les dates et les heures
        - `datetime.datetime.now()` : obtient la date et l'heure actuelles
        - `datetime.timedelta(days=1)` : représente une durée de temps
        - `datetime.date.today()` : obtient la date actuelle
    - `time` : permet de travailler avec le temps
        - `time.sleep(seconds)` : suspend l'exécution du programme pendant un certain nombre de secondes
        - `time.time()` : obtient le temps écoulé depuis le 1er janvier 1970 (timestamp)
        - `time.perf_counter()` : obtient un compteur pour mesurer le temps d'exécution
    - `re` : permet de travailler avec les expressions régulières
        - `re.match(pattern, string)` : tente de faire correspondre un motif au début d'une chaîne
        - `re.findall(pattern, string)` : trouve toutes les occurrences d'un motif dans une chaîne
    - `os` : permet d'interagir avec le système d'exploitation
        - `os.path` : fournit des fonctions pour manipuler les chemins de fichiers
        - `os.environ` : permet d'accéder aux variables d'environnement
    - `sys` : fournit des fonctions et des variables pour interagir avec l'interpréteur Python
        - `sys.argv` : liste des arguments de la ligne de commande
        - `sys.exit()` : permet de quitter le programme
    - ... et bien d'autres encore !

```Python
# Exemple d'utilisation de quelques modules standards

# Importation des modules
import math
import random
import time

# Définition des constantes et variables
COUNT = 10000
RANGE = 10000
ref_time = time.perf_counter()  # prend un compteur de référence

# Fait un calcul relativement lourd
for _ in range(COUNT):
    # Génère un entier aléatoire dans l'intervalle [-RANGE, RANGE]
    value = random.randint(-RANGE, RANGE)
    # Calcule la racine carrée de la valeur aléatoire
    value = math.sqrt(value)  

# Calcule le temps écoulé et l'affiche
elapsed_time = time.perf_counter() - ref_time  
print("Temps écoulé pour ", COUNT, " itérations : ", elapsed_time, " secondes")
```

### Exercices 3

- Exercice 3.1 : 
    - Générerez _n_ nombres aléatoires dans l'intervalle [0, 100] et affichez à l'écran ces statistiques :
        - le nombre de valeurs générées
        - valeur la plus petite
        - valeur la plus grande
        - moyenne
        - le temps d'exécution de l'algorithme
        - optionnellement :
            - la variance (la variance est la moyenne des carrés des écarts à la moyenne)
            - l'écart-type (l'écart-type est la racine carrée de la variance)
            - la médiane
    - _n_ est un nombre saisie par l'utilisateur au début du programme. Il doit être borné entre 3 et 10000. Si l'utilisateur saisit une valeur invalide, le programme remplace automatiquement par 100.
    - voici quelques considérations pour cet exercice :
        - vous pouvez utiliser les modules `random`, `math` et `time`
        - vous pouvez utiliser une liste pour stocker les valeurs aléatoires
        - les fonctions suivantes existent directement dans le _core_ Python :
            - `len(...)`
            - `min(...)`
            - `max(...)`
            - `sum(...)`
            - `sorted(...)`
        - pratiquez-vous en créant ces fonctions utilitaires :
            - `get_n()` : retourne la valeur _n_ saisie par l'utilisateur (la valeur est adaptée)
            - `generate_random_values(n, min_value, max_value)` : génère et retourne une liste de _n_ valeurs aléatoires dans l'intervalle [min_value, max_value]
            - `mean(values)` : calcule et retourne la moyenne d'une liste de valeurs
            - `variance(<à votre choix>)` : calcule et retourne la variance d'une liste de valeurs
            - `stddev(<à votre choix>)` : calcule et retourne l'écart-type d'une liste de valeurs
            - `median(<à votre choix>)` : calcule et retourne la médiane d'une liste de valeurs

- Exercice 3.2 :
    - Écrivez un programme qui demande à l'utilisateur de saisir une phrase et qui affiche :
        - le nombre de caractères
        - le nombre de voyelles : <br> `vowels = 'aeiouy'`
        - le nombre de consonnes : <br> `consonants = 'bcdfghjklmnpqrstvwxz'`
        - le nombre de caractères spéciaux (ponctuation, espaces, etc.) :  <br> `special_characters = ' !"#$%&\'()*+,-./:;<=>?@[\\]^_{|}~'`
        - le nombre de mots
    - Vous devez créer au moins ces fonctions utilitaires :
        - `get_sentence()` : retourne la phrase saisie par l'utilisateur
        - `sentence_stats(sentence)` : une seule fonction qui retourne un tuple avec les statistiques suivantes :
            - le nombre de caractères
            - le nombre de voyelles
            - le nombre de consonnes
            - le nombre de caractères spéciaux
            - le nombre de mots
    - Autres astuces :
        - consulter la méthode `str.split()` 

- Exercice 3.3 :
    - Faites un jeu de dés pour un utilisateur. 
    - Au démarrage d'une partie, le programme demande à l'utilisateur les 3 informations suivantes :`
        - combien de dés, entre 1 et 4, par défaut 2
        - combien le nombre de faces de chaque dé (entre 4 et 16, par défaut 6)
        - combien de tours, entre 1 et 10, par défaut 2
    - Ensuite, le programme passe les _t_ tours et joue pour les deux joueurs (l'utilisateur et lui-même). À chaque tour :
        - il lance tous les dés pour les joueurs
        - il affiche les résultats de tous les dés
        - il affiche la somme cumulée de chaque joueur pour le tour
        - il affiche la somme cumulée de chaque joueur pour la partie
        - il invite l'utilisateur à appuyer sur une touche pour passer au tour suivant
    - À la fin de la partie, le programme affiche le gagnant (le joueur avec la somme la plus élevée) et les scores finaux.
    - Faites un effort pour créer des fonctions pertinentes.
