
# Introduction à Python - Cours 1

## Partie 1 

### Présentation générale de Python

- Bref historique
    - Créé par Guido van Rossum en 1991
    - Nommé d'après la célèbre série télévisée britannique _Monty Python's Flying Circus_
    - Les versions majeures de Python sont :
        - `Python 1.0` (janvier 1994 -> octobre 2000)
        - `Python 2.0` (octobre 2000 -> juillet 2010)
        - `Python 3.0` (décembre 2008 -> présent)
        - `Python 3.13` est la version actuelle et recommandée
        - `Python 3.14` est prévue pour le 7 octobre 2025
    - Aujourd'hui, Python est maintenu par la _Python Software Foundation_ ([PSF](https://www.python.org/psf-landing/)), dispose d'une large communauté de développeurs et de contributeurs et est utilisé dans de nombreux domaines
- Caractéristiques principales :
    - Langage _open source_, avec une large communauté de développeurs et de contributeurs
    - Disponible sur de nombreuses plateformes, y compris Windows, macOS, Linux, iOS, Android, IoT, _embedded_, etc.
    - Langage de programmation polyvalent, utilisé dans divers domaines tels que le développement web, l'analyse de données, l'intelligence artificielle, l'automatisation, etc.
    - Est utilisé par de nombreuses entreprises et organisations, y compris Google, Facebook, NASA, et tellement d'autres
    - Souvent utilisé pour l'enseignement de la programmation en raison de sa syntaxe claire et de sa facilité d'apprentissage
    - Langage de programmation multi-paradigmes. Prend en charge plusieurs styles de programmation : impérative, procédurale, fonctionnelle et orientée objet (tout est `POO`)
    - Langage de programmation de haut niveau offrant plusieurs abstractions facilitant le développement
    - Langage de programmation interprété, permettant d'exécuter du code sans compilation préalable
    - Langage de programmation à typage dynamique (au _run time_), les types de données sont déterminés au moment de l'exécution, plutôt qu'à la compilation (statique, _compile time_)
    - Gestion automatique de la mémoire (_garbage collector_)
    - Support de la programmation asynchrone
    - Langage de programmation extensible, ce qui signifie qu'il peut être étendu avec des modules et des bibliothèques écrits dans d'autres langages, tels que C ou C++ notamment
    - Langage de programmation populaire et très important dans l'industrie, classé parmi les langages les plus utilisés dans le monde :
        - [TIOBE Index](https://www.tiobe.com/tiobe-index/) [`<nom du langage> programming`]
        - [PYPL](https://pypl.github.io/PYPL.html) (_PopularitY of Programming Languages_) [`<nom du langage> tutorial`]
        - [Stack Overflow Developer Survey](https://insights.stackoverflow.com/survey) [`<nom du langage> developer`]
        - Les différents index donnent des résultats différents à cause de la méthodologie de calcul et des différents domaines de développement. Simplement dit, dans [`<nom du langage> xyz`], le `xyz` fait référence à l'approche (largement simplifiée).
    - Python est considéré l'un des langages de programmation les plus :
        - faciles à apprendre
        - élégants 
        - pertinents pour les débutants et experts 
    - Les fichiers de code Python sont des fichiers texte avec l'extension `.py` (ex. `mon_script.py`)
    - Lors de sa première exécution, le code source Python `.py` est compilé en `bytecode` et sauvegardé dans un fichier `.pyc`; c'est ce `bytecode`, et non le code source original, qui est ensuite exécuté par la machine virtuelle Python (PVM). Processus similaire à la JMV de Java.
    - Il existe de nombreuses implémentations de Python, la plus courante étant CPython (implémentation de référence), mais il y a aussi Jython (pour Java), IronPython (pour .NET), PyPy (interprétation rapide), MicroPython (pour les microcontrôleurs et systèmes embarqués) et d'autres
    - Il existe plusieurs documents officiels appelés `PEP ###` (_Python Enhancement Proposals_) qui décrivent les améliorations (passées et à venir) ainsi que plusieurs guides adressant divers sujets :
        - [PEP 20](https://peps.python.org/pep-0020/) : Philosophie zen de Python
            - Il devrait y avoir une seule façon évidente de faire les choses - _There should be one -- and preferably only one -- obvious way to do it_
            - La lisibilité compte - _Readability counts_
            - Le simple est meilleur que le complexe - _Simple is better than complex_
            - L'explicite est meilleur que l'implicite - _Explicit is better than implicit_
            - Face à l'ambiguïté, refusez la tentation de deviner - _In the face of ambiguity, refuse the temptation to guess_
            - Maintenant vaut mieux que jamais - _Now is better than never_
            - Si l'implémentation est difficile à expliquer, c'est une mauvaise idée - _If the implementation is hard to explain, it's a bad idea_
            - ...
        - [PEP 8](https://peps.python.org/pep-0008/) : Guide de style pour Python
            - Python est l'un des seuls langages de programmation à avoir un guide de style officiel
            - Une norme de codage est toujours définie pour un projet ou une organisation, Python en propose une qui est largement adoptée mais pas obligatoire
            - Quelques conventions de nommage selon `PEP 8` :
                - les variables et fonctions utilisent le `lower_snake_case` (ex. `ma_variable`, `ma_fonction`, `current_speed`, `accelerate(...)`)
                - les constantes utilisent le `UPPER_SNAKE_CASE` (ex. `PI`, `MAXIMUM_ACCELERATION`)
                - les classes et _types_ utilisent le `PascalCase` (ex. `MaClasse`, `FireTower`)
                - les modules et packages utilisent le `lower_snake_case` (ex. `mon_module`, `mon_package`)
        - ... et plusieurs autres
- Python vs Java et C++
    - Python est à typage dynamique, alors que Java et C++ sont statiquement typés
    - Complexité relative :
        - Python est considéré comme plus simple et plus lisible que Java et C++
        - Java a une syntaxe plus stricte que Python, mais est beaucoup plus facile que C++ (sa syntaxe s'inspire de C++)
        - C++ est considéré comme le langage de programmation le plus complexe de l'industrie, avec une syntaxe nécessitant plusieurs nuances et des concepts très larges ainsi qu'avancés
    - Python est plus flexible que Java et C++, permettant une programmation plus rapide et plus facile
    - Python est souvent utilisé pour l'enseignement de la programmation en raison de sa syntaxe claire et de sa facilité d'apprentissage, tandis que C++ est souvent utilisés dans des contextes plus avancés
    - Python est l'un des langages les plus lents à l'exécution, toutefois il reste très performant pour de nombreux cas d'utilisation, notamment grâce à son écosystème riche en bibliothèques optimisées précompilées

### Éléments de base du langage Python

- Structure syntaxique générale
    - sensible à la casse
    - commentaires :
        - sur une seule ligne débutant par `#`
        - pas de multilignes
    - il n'y a pas de symbole pour terminer une instruction (pas de  point-virgule `;`)
    - les blocs de code sont définis par l'indentation (4 espaces est le standard, les tabulations ne sont pas recommandées)
    - les instructions doivent être sur une seule ligne, à l'exception de :
        - dans certains contextes, si elles sont entre parenthèses `()`, crochets `[]` ou accolades `{}` 
        - avec l'utilisation de la barre oblique inversée `\` à la fin de la ligne
    - il n'y a pas de point d'entrée formel : 
        - pas de `main`
        - chaque fichier Python est appelé un _module_ et peut être exécuté directement
        - les instructions sont exécutées dans l'ordre où elles apparaissent dans le fichier
    - les fichiers texte contenant du code `Python` utilise l'extension `py`
    - langage offrant ne supportant pas tous les concepts de `Java` et `C++` :
        - certains concepts sont similaires mais fondamentalement différents : `struct`, `enum`, `switch`, `static`, `interface`, `override`, `final`,  `union`, `pointer`, `reference`, ...
        - d'autres n'existent pas mais sont compensés par des conventions bien établies : `const`, `private`, `protected`, `package`, `friend`, ...
        - certains concepts n'existent pas du tout : `do-while`, `goto`, ...
    - typage dynamique
    - offre un large éventail de bibliothèque
    - formellement, tout est un objet en `Python` (nous y reviendrons)
- Types fondamentaux
    - `bool`
    - `int`
    - `float` (pas de `double`, en fait le `float` est un `double`)
    - `complex`
    - `str`
    - `bytes` et `bytearray`
    - `None` (équivalent à `null` en `Java` ou conceptuellement similaire `nullptr` en `C++`)
- Les litéraux sont similaires aux autres langages :
    - `int` : `42`, `0x2A`, `0b101010`
    - `float` : `3.14`, `2.71828`, `1.0e-10`
    - `complex` : `1 + 2j`, `3 - 4j`
    - `str` : 
        - avec apostrophes : `'Hello'`, `'''Multiline string'''`
        - avec guillemets : `"World"`, `"""Multiline string"""`
        - pas de préférence, utiliser l'un ou l'autre selon le contexte mais rester cohérent et consistant
    - `bool` : `True`, `False`
    - `None` : `None`
- Deux fonctions utilitaires pour afficher et saisir des données dans la console :
    - `print` pour afficher des données à la console
        - `print(<valeur>, ...)`
        - `print('Hello World!')`
        - `print('Hello', ' ', 'World!')`
    - `input` pour saisir des données depuis la console
        - `result = input(<message>)` pour afficher un message avant la saisie
        - `name = input('Veuillez saisir votre nom : ')`
- Quelques fonctions utilitaires  :
    - Conversion de types :
        - `bool(<valeur>)` pour convertir en booléen
        - `int(<valeur>)` pour convertir en entier
        - `float(<valeur>)` pour convertir en flottant
        - `str(<valeur>)` pour convertir en chaîne de caractères
    - Fonctions de base :
        - `abs(<valeur>)` pour obtenir la valeur absolue
        - `round(<valeur>, <précision>)` pour arrondir un nombre
    - Introspection :
        - `id(<valeur>)` pour obtenir l'identifiant unique d'un objet
        - `type(<valeur>)` pour obtenir le type d'une valeur

```Python
# Exemple de code Python

# Déclaration de variables et utilisation de litéraux
x = 42  # entier
y = 3.14  # flottant
z = 1 + 2j  # complexe
s = 'Hello, World!' # chaîne de caractères

# Affichage des variables
print('Bonjour, Monde!')  # Affiche une chaîne de caractères
print(s)  # Affiche la variable s

# Saisie, concaténation et affichage
response = input("Entrez votre nom : ")  # Saisie utilisateur
print("Bonjour, " + response + "!")  # Affiche un message de bienvenue 
                                     # utilisant l'opérateur de concaténation
```

- Les opérateurs sont très similaires aux autres langages :
    - unaires : `-`, `+`, `not`, `~`
    - binaires : 
        - assignation : `=`
        - arithmétiques : `-`, `+`, `*`, `/`, `%`, `^`
            - différents : `//`, `**`
        - comparaisons : `==`, `!=`, `<`, `<=`, `>`, `>=` 
        - logique : `or`, `and`
        - bit à bit : `&`, `|`, `^`, `~`, `<<`, `>>`
        - opérateurs d'assignation combinée : `+=`, `-=`, `*=`, ...
        - opérateurs d'identité : `is`, `is not`
        - opérateurs d'appartenance : `in`, `not in` (_on y reviens avec les collections_)
        - et plusieurs autres
    - attention, ces opérateurs ne sont pas disponibles :
        - `++`, `--` (incrémentation et décrémentation)
        - `!`, `&&`, `||` (négation logique, et logique, ou logique)
        - `?:` l'opérateur ternaire mais possède l'alternative syntaxique suivante (_beaucoup plus lisible_) :
            - on utilise : `value = x if condition else y`
            - au lieu de : `value = condition ? x : y;`
        - `sizeof`, `&`, `*` et `->` (taille en mémoire, adresse, déréférencement et accès aux membres via un pointeur)
        - et plusieurs autres
    - attention, le `=` n'est pas un opérateur à proprement parlé comme l'opérateur d'assignation existant dans d'autres langages (_nous y reviendrons dans d'autres cours_)
```Python
# Exemple de code Python
# Déclaration de variables
a = 10
b = 5
c = a + b  # Addition
d = a - b  # Soustraction

s = "Hello"
t = "World"
y = s + " " + t  # Concaténation de chaînes
z = '-' * 10 # Répétition de chaînes

test = 'Positif' if a > 0 else 'Négatif'  # Opérateur ternaire
```
- Contrôle de flux
    - `if`, `elif`, `else` (il n'y a pas de `switch-case`)
    - `while` 
    - `for` 
    - `break` 
    - `continue` 
    - `return` 
    - `pass` (instruction vide, _placeholder_, nécessaire pour la syntaxe)
    - `match` (_pattern matching_, à partir de Python 3.10 seulement)
    - `try`, `except`, `finally` et `raise` pour gérer les exceptions
    - la définition d'une section logique utilise une approche par indentation avec l'usage des deux-points `:` plutôt que les accolades `{ }` (4 espaces est le standard)
    - il est possible de créer un bloc logique vide avec `pass` (utile pour les fonctions ou classes non implémentées)
    - attention, il n'y a pas de `do-while` ni de `switch-case` (mais on y revient avec le `match`)

```Python
# Exemple de code Python

test = False
while not test:
    result = input("Entrez un nombre entre 0 et 100 : ") # le résultat est une chaîne de caractères
    if result.isdigit(): # isdigit est une méthode de la classe str
        number = int(result)
        if 0 <= number <= 100:
            test = True
            print("Vous avez entré un nombre valide :", number)
        else:
            print("Le nombre doit être entre 0 et 100.")
    else:
        print("Veuillez entrer un nombre entier valide.")
```


- Particularité de la boucle `for` :
    - itère sur les éléments d'une séquence (comme une liste, un tuple, une chaîne de caractères, etc.)
    - syntaxe : <br>`for <variable> in <séquence> : <faire quelque chose>`
    - par exemple :  <br>`for letter in 'Bonjour' : print(letter)`
    - il existe une fonction utilitaire `range` pour générer une séquence de nombres :
        - `range(<début>, <fin>, <pas>)` génère une séquence linéaire de nombres de `<début>` à `<fin>` (exclusif) avec un pas de `<pas>`
        - si `<début>` est omis, il est considéré comme 0
        - si `<pas>` est omis, il est considéré comme 1
        - par exemple :
            - `range(5)` génère la séquence `[0, 1, 2, 3, 4]`
            - `range(-4, 5)` génère la séquence `[-4, -3, -2, -1, 0, 1, 2, 3, 4]`
            - `range(0, 10, 2)` génère la séquence `[0, 2, 4, 6, 8]`
    - nous reviendrons en détail sur les boucles `for` qui offrent beaucoup plus encore

```Python
# Exemple de code Python

# Boucles for avec range
for i in range(5):  # itère de 0 à 4
    print(i)  # Affiche les nombres de 0 à 4

for i in range(2, 5, 2):  # itère de 2 à 4 avec un pas de 2 => [2, 4]
    for j in range(3, 0, -1):  # itère de 3 à 1 avec un pas de -1 => [3, 2, 1]
        print(i * 100 + j)  # Affiche : 203, 202, 201, 403, 402, 401
```


### Exercices 1

- Utilisez uniquement :
    - les types fondamentaux `int`, `float`, `str`, `bool`
    - les opérateurs arithmétiques, de comparaison et logiques
    - les structures de contrôle de flux `if`, `elif`, `else`, `while`, `for`
    - les fonction `print` et `input` pour interagir avec la console.

- Exercice 1.1 : Devinez un nombre (avec essais limités)
    - Le programme possède un _nombre secret_ défini dans le code par la variable `number` dans l'intervalle [0, 100] (par exemple, 42).
    - L'utilisateur a cinq essais pour le deviner. 

    - Après chaque essai, le programme indique si le nombre à deviner est "Plus haut" ou "Plus bas". 
    - Le jeu se termine si l'utilisateur trouve le nombre ou s'il n'a plus d'essais.

- Exercice 1.2 : Calculatrice simple
    - Créez une calculatrice simple qui peut effectuer les opérations de base : addition, soustraction, multiplication et division.
    - Le programme doit demander à l'utilisateur d'entrer deux nombres et l'opération souhaitée en trois saisies différentes.
    - Affichez le résultat de l'opération.
    - Optionnellement, gérez les erreurs potentielles, comme les erreurs de saisie etla division par zéro.

- Exercice 1.3 : Table de multiplication
    - Demandez à l'utilisateur d'entrer deux nombres entiers entre 2 et 10 (en 2 saisies distinctes).
    - Affichez la table de multiplication de ces nombres.

- Exercice 1.4 : Trier simplement trois nombres (sans fonctions ni collections)
    - Objectif. Afficher trois entiers saisis en ordre croissant sans utiliser de liste ni la fonction `sorted(...)`.
    - Demander à l'usager de saisir trois entiers `a`, `b` et `c` (en 3 saisies distinctes).
    - Réordonner ces trois entiers en ordre croissant.
    - Afficher sur trois lignes :
        - les trois entiers dans l'ordre saisies
        - les trois entiers en ordre croissant sur une seule ligne
        - si les trois variables sont strictement différentes les unes des autres, afficher `Strict` sinon afficher `Non-strict`



