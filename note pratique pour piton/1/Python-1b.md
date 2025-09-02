
# Introduction à Python - Cours 1

## Partie 2b - Structures de données fondamentales

- Présentation
    - Les collections sont des structures de données qui permettent de stocker et de gérer plusieurs éléments sous une seule variable
    - Les tableaux sont un exemple de collection.
    - Cette présentation est sommaire et vise à :
        - présenter les collections fondamentales
        - présenter quelques fonctions et méthodes associées
        - donner un aperçu de leur utilisation
    - Nous reviendrons en détail sur les collections dans ce cours et dans d'autres cours
    - Les collections fondamentales en Python sont :
        - Les chaînes de caractères `str` (oui, c'est une collection de caractères)
        - Les listes `list`
        - Les tuples `tuple`
        - Les dictionnaires `dict`
        - Les ensembles `set`

- Caractéristiques principales des collections :
    - `str` (chaîne de caractères) :
        - Ordonnée par position (comme un tableau)
        - Non modifiable (les caractères ne peuvent pas être ajoutés, supprimés ou modifiés après la création)
        - Permet les doublons
        - Utilise des crochets `[]` pour l'indexation en lecture par position seulement (pas en écriture)
        - Utilise des apostrophes `'...'` ou des guillemets `"..."` pour la création
        - Exemple : 
            - `my_str = str('Hello, World!') # constructeur de chaîne`
            - `my_str = 'Hello, World!' # littéral de chaîne`
            - `print(my_str[0]) # accès en lecture, affiche 'H'`
        - Les méthodes importantes sont :
            - `upper()` pour convertir en majuscules
            - `lower()` pour convertir en minuscules
            - `strip()` pour supprimer les espaces au début et à la fin
            - `replace()` pour remplacer une sous-chaîne par une autre
            - `split()` pour diviser la chaîne en une liste de sous-chaînes
            - `join()` pour joindre une liste de chaînes en une seule chaîne
            - `find()` pour trouver la position d'une sous-chaîne
            - `count()` pour compter les occurrences d'une sous-chaîne    
    - `list` (liste) :
        - Ordonnée par position (comme un tableau)
        - Modifiable (des éléments peuvent être ajoutés, supprimés ou modifiés)
        - Permet les doublons
        - Utilise des crochets `[]` pour l'indexation par position en lecture et en écriture
        - Utilise des crochets `[]` pour la création 
        - Exemple : 
            - `my_list = list(1, 2, 3, 4, 5) # constructeur de liste`
            - `my_list = [1, 2, 3, 4, 5] # littéral de liste`
            - `print(my_list[0]) # accès en lecture`
            - `my_list[0] = 10 # accès en écriture`
        - Les méthodes importantes sont :
            - `append()` pour ajouter un élément à la fin
            - `insert()` pour ajouter un élément à une position donnée
            - `remove()` pour supprimer un élément par valeur
            - `pop()` pour supprimer un élément par position
            - `clear()` pour vider la liste
            - `sort()` pour trier la liste
            - `count()` pour compter les occurrences d'un élément
            - `index()` pour obtenir l'index d'un élément
    - `tuple` (tuple) :
        - Ordonné par position (comme un tableau)
        - Le tuple lui-même n'est pas modifiable (des éléments ne peuvent pas être ajoutés, supprimés ou modifiés après la création)
        - Permet les doublons
        - Utilise des crochets `[]` pour l'indexation par position en lecture seule
        - Utilise des parenthèses `()` pour la création (attention à l'une des rares exceptions syntaxiques du langage Python)
        - Exemple : 
            - `my_tuple = tuple(1, 2, 3, 4, 5) # constructeur de tuple`
            - `my_tuple = (1, 2, 3, 4, 5) # littéral de tuple`
            - `print(my_tuple[0]) # accès en lecture`
        - Les méthodes importantes sont :
            - `count()` pour compter les occurrences d'un élément
            - `index()` pour obtenir l'index d'un élément
    - `set` (ensemble) :
        - Non ordonné (les éléments n'ont pas de position fixe)
        - Modifiable (des éléments peuvent être ajoutés ou supprimés)
        - Interdit les doublons (chaque élément est unique)
        - Utilise des accolades `{}` pour la création
        - Exemple : 
            - `my_set = set([1, 2, 3, 4, 5]) # constructeur de set`
            - `my_set = {1, 2, 3, 4, 5} # littéral de set` (attention à l'une des rares exceptions syntaxiques du langage Python, des accolades vides crées un dictionnaire)
            - `my_set.add(6) # ajouter un élément`
        - Les méthodes importantes sont :
            - `add()` pour ajouter un élément
            - `remove()` pour supprimer un élément (lève une exception si l'élément n'existe pas)
            - `discard()` pour supprimer un élément (ne lève pas d'exception si l'élément n'existe pas)
            - `clear()` pour vider l'ensemble
            - `union()`, `intersection()`, `difference()` pour les opérations ensemblistes
    - `dict` (dictionnaire) :
        - Associatif : les éléments sont stockés sous forme de paires clé-valeur
        - Ordonné seulement pour le parcours (les éléments sont parcourus dans l'ordre d'insertion, à partir de Python 3.7)
        - Non ordonné (les éléments n'ont pas de position fixe)
        - Modifiable (des éléments peuvent être ajoutés, supprimés ou modifiés)
        - Utilise des crochets `[]` pour l'indexation par clé en lecture et écriture
        - Les doublons sont :
            - interdits pour les clés
            - permis pour les valeurs
        - Utilise des accolades `{ clé: valeur, ... }` pour la création
        - Exemple : 
            - `my_dict = dict(a=1, b=2, c=3) # constructeur de dictionnaire`
            - `my_dict = {'a': 1, 'b': 2, 'c': 3} # littéral de dictionnaire`
            - `print(my_dict['a']) # accès en lecture, affiche 1`
            - `my_dict['a'] = 10 # accès en écriture, modifie la valeur associée à la clé 'a' - le 1 devient 10`
- Quelques fonctions et méthodes utiles pour les collections :
    - Outils génériques fonctionnant dans toutes les collections :
        - `if <élément> in <collection>` pour vérifier si un élément est dans une collection
            - ex. : `if 'Bob' in my_dict: print("'Bob' est dans le dictionnaire")`
        - `len(<collection>)` pour obtenir la longueur d'une collection
            - ex. : `print(len(my_list)) # affiche 5`
        - `for <value> in <collection>: <action>` pour itérer sur tous les éléments d'une collection
            - ex. : `for item in my_list: print(item)`
- Vous **devez** lire progressivement la documentation officielle pour développer vos compétences et connaissances ([voir](https://docs.python.org/3/tutorial/datastructures.html)).




### Exercices 2

- Vous devez utiliser exclusivement :
    - les mêmes instructions que les exercices 1
    - les collections fondamentales

- Exercice 2.1 : 
    - Objectif : Déterminer si une phrase est un palindrome.
    - Un palindrome est un mot ou une phrase qui se lit de la même manière dans les deux sens en ignorant les espaces, les accents, les signes de ponctuation et la casse.
    - Par exemple, ces mots : ressasser, kayak, radar, etc. 
    - On désire mettre l'accent sur les étapes suivantes de résolution :
        1. Normaliser la phrase en mettant chaque lettre dans une liste(mettre en minuscules, enlever les espaces, les accents et la ponctuation)
        2. Créer une deuxième liste qui est l'inverse de la première
        3. Comparer les deux listes
    - Vous devez parcourir toutes les phrases suivantes et déterminer si elles sont des palindromes en inscrivant l'une ou l'autre des phrases suivantes selon le résultat :
        - Oui : '< la phrase entre apostrophes >'
        - Non : '< la phrase entre apostrophes >'
    - Phrases à tester (pour simplifier, elles ne possède ni accents ni signes de ponctuation) :
``` Python
# Phrases à tester (les accents ont été retirés)
tests = (
    'Esope reste ici et se repose',
    'Elu par cette crapule',
    'Engage le jeu que je le gagne',
    'La mariee ira mal',
    'Eric notre valet alla te laver ton cire',
    'Il est incroyable',
    'Able was I ere I saw Elba',
    'A man a plan a canal Panama',
    'Was it a car or a cat I saw',
    'Never odd or even',
    'Madam, I m Adam',
    'Hello World',
    'A Toyota’s a Toyota',)
```
Sachez que Python offre des outils puissants permettant la simplification de cet exercice mais ce n'est pas le but ici. Voici une solution toute simple.

``` Python
# Solution ultra simple et compacte ()
text = "Esope reste ici et se repose"
normalized_text = text.lower().replace(" ", "")
reversed_text = str(reversed(normalized_text))
print(f"{'Oui' if normalized_text == reversed_text else 'Non'} :", text)
```


 - Exercice 2.2 : 
    - Objectif : Manipuler une collection pour créer des statistiques.
    - Vous devez créer deux dictionnaire qui compte :
        - le nombre d'individus pour chacun des genres : `gender_count`
        - pour chaque ville, le nombre d'individus et l'âge moyen : `city_stat`
    - Vous devez afficher les résultats sous la forme :
        - Genres :
            - femme : 11
            - homme : 9
            - autre : 4
        - Villes :
            - Montréal : 6 individus avec un âge moyen de 35 ans
            - Québec : 5 individus avec un âge moyen de 40 ans
            - ...
    - Vous devez utiliser la collection `data` suivante :
```python
data = [
    ("Tremblay, Marc", 41, "Montréal", 'h'),
    ("Lévesque, Annie", 30, "Gatineau", 'f'),
    ("Beaulieu, Denis", 58, "Longueuil", 'h'),
    ("Aubin, Christine", 41, "Saguenay", 'f'),
    ("Gauthier, Julie", 33, "Québec", 'f'),
    ("Boucher, Geneviève", 37, "Sherbrooke", 'f'),
    ("Bergeron, Mathieu", 36, "Gatineau", 'h'),
    ("Poirier, Daniel", 63, "Saguenay", 'h'),
    ("Gagnon, Laure", 27, "Montréal", 'f'),
    ("Morin, Philippe", 54, "Québec", 'h'),
    ("Caron, Zoé", 21, "Gatineau", 'x'),
    ("Bélanger, Thomas", 42, "Laval", 'h'),
    ("Pelletier, Maude", 24, "Laval", 'f'),
    ("Langlois, Patrick", 50, "Sherbrooke", 'h'),
    ("Simard, Noé", 34, "Longueuil", 'x'),
    ("Roy, Étienne", 35, "Montréal", 'h'),
    ("Ouellet, Kevin", 38, "Laval", 'h'),
    ("Côté, Myriam", 22, "Montréal", 'f'),
    ("Lavoie, Nadine", 46, "Québec", 'f'),
    ("Bouchard, Alex", 31, "Montréal", 'x'),
    ("Fortin, Samuel", 19, "Québec", 'h'),
    ("Girard, Valérie", 26, "Longueuil", 'f'),
    ("Gagné, Chantal", 29, "Laval", 'f'),
    ("Lefebvre, Simon", 18, "Saguenay", 'h'),
    ("Lapointe, Amélie", 23, "Sherbrooke", 'f'),
    ("Dufour, Olivier", 40, "Montréal", 'h'),
    ("Boucher, Camille", 28, "Gatineau", 'f'),
    ("Lemieux, Alexandre", 39, "Québec", 'h'),
    ("Desjardins, Élise", 32, "Laval", 'f'),
    ("Morissette, Vincent", 45, "Longueuil", 'h'),
    ("Caron, Sarah", 20, "Saguenay", 'f'),
    ("Bélanger, Maxime", 44, "Sherbrooke", 'h')]
```


### Exercice 2.3 : 
- Objectif : Validater les parenthèses, crochets et accolades ()[]{} 
    - Étape 1 : Lire une ligne de texte saisie à la console.
    - Étape 2 : Si la ligne est vide, utiliser cette chaîne de caractères par défaut : <br>
      `phrase = "Au labo (site {Nord [A-12]}) nous notons que g(x) = (x+{2y[3z]})/(4u-{5v[6w]}) reste stable."`
    - Étape 3 : Vérifier si les parenthèses, crochets et accolades sont équilibrés.
        - Les parenthèses/crochets/accolades ouvrantes doivent être fermées par des parenthèses/crochets/accolades fermantes
        - Les parenthèses/crochets/accolades doivent être correctement imbriqués, par exemple (ce n'est pas seulement le nombre qui compte) :
            - `([]){} → OK`
            - `([){]} → ERR`
        - Vous devez utiliser une pile pour vérifier l'équilibre des parenthèses, crochets et accolades. Pour y arriver, utilisez une liste avec les méthodes `append` pour ajouter un élément  et `pop` pour retirer le dernier élément ajouté.
    - Étape 4 : Affichez l'un de ces messages :
        - `OK` si les parenthèses, crochets et accolades sont équilibrés
        - `ERR pos = i` si une erreur est détectée, où `i` est la position de la première erreur (_0 based index_)


### Exercice 2.4 :
- Objectif : Effectuer la somme numérique d'un nombre
    - Étape 1 : Lire une ligne de texte saisie à la console.
    - Étape 2 : Si la ligne est vide, utiliser cette chaîne de caractères par défaut : `value = "1234567890"`
    - Étape 3 : Calculer la somme de tous les chiffres dans la chaîne de caractères. Par exemple, pour la chaîne `value = "12345"`, la somme est `15` (`1 + 2 + 3 + 4 + 5`).
    - Étape 4 : Afficher le résultat de la somme.
    - Étape 5 : Recommencer les étapes 3 et 4 en réutilisant le résultat de la somme jusqu'à ce que ce résultat soit de 1 chiffre. Par exemple :
        - `99999999999992 -> 119`
        - `119 -> 11`
        - `11 -> 2`
    - Étape 6 : Afficher le résultat final.
    - Étape 7 : Recommencer les étapes 1 à 6 jusqu'à ce que l'utilisateur saisisse un point `.`.
    - Il existe plusieurs approches pour résoudre cet exercice. Vous pouvez utiliser celle qui vous convient le mieux. L'utilisation de structures de données est très intuitive mais une approche mathématique reste plus efficace. Produire plusieurs solutions utilisant diverses approches est un excellent exercice.
