# Documentation Python - Cours C52

## Table des matières
1. [Bonnes pratiques et normes de codage](#bonnes-pratiques)
2. [Types fondamentaux](#types-fondamentaux)
3. [Structures de données](#structures-de-données)
4. [Slicing (découpage)](#slicing)
5. [Boucles et parcours](#boucles-et-parcours)
6. [List comprehension](#list-comprehension)
7. [Références et Garbage Collector](#références-et-garbage-collector)
8. [F-strings (formatage de chaînes)](#f-strings)
9. [Programmation Orientée Objet](#programmation-orientée-objet)
10. [NumPy - Introduction](#numpy)

---

## Bonnes pratiques

### Principes fondamentaux

**CALTAL** - *Code A Little | Test A Little*
- Écrivez du code en petites portions
- Testez immédiatement après chaque modification
- Ne pas écrire 100 lignes sans tester

**DRY** - *Don't Repeat Yourself*
- Évitez la duplication de code
- Créez des fonctions réutilisables
- Si vous copiez-collez du code, pensez à créer une fonction

**UMUD** - *yoU Must Use the Debugger*
- Utilisez TOUJOURS le débogueur pour trouver les erreurs
- N'utilisez pas uniquement `print()` pour déboguer
- Apprenez à utiliser les breakpoints

### Norme PEP8

PEP8 est la norme de codage officielle de Python. Voici les éléments essentiels :

#### Disposition
- **Indentation** : 4 espaces (JAMAIS de tabs)
- **Longueur des lignes** : Maximum 79 caractères
- **Lignes vides** :
  - 2 lignes avant une fonction ou classe
  - 1 ligne avant une méthode dans une classe

#### Nommage
```python
# Types/Classes : PascalCase
class GameCharacter:
    pass

# Variables, fonctions, méthodes : snake_case
player_health = 100
def calculate_damage():
    pass

# Constantes : CAPITAL_SNAKE_CASE
MAX_HEALTH = 100
GAME_VERSION = "1.0.2"
```

#### Imports
Organisez les imports au début du fichier dans cet ordre :
```python
# 1. Librairies standards
import sys
import copy
from datetime import datetime

# 2. Librairies externes
import numpy as np

# 3. Librairies internes (vos propres modules)
from mon_module import ma_fonction
```

---

## Types fondamentaux

Python possède plusieurs types de base :

```python
# Entier (int)
a = 10
print(type(a))  # <class 'int'>

# Réel/Flottant (float)
b = 3.14
print(type(b))  # <class 'float'>

# Booléen (bool)
c = True
print(type(c))  # <class 'bool'>

# Chaîne de caractères (str)
d = "C52"
print(type(d))  # <class 'str'>

# Type None (NoneType)
e = None
print(type(e))  # <class 'NoneType'>

# Nombre complexe (complex)
f = 1+2j
print(type(f))  # <class 'complex'>
```

### Opérateurs conditionnels

#### Condition ternaire
```python
value = -5
# Vérifier si une valeur est dans un intervalle
print(0 <= value < 10)  # Équivalent à : value >= 0 and value < 10
```

#### Opérateur ternaire
```python
value = -5
result = 'positif' if value >= 0 else 'négatif'
print(result)  # 'négatif'

# Autre exemple
age = 20
statut = 'Majeur' if age >= 18 else 'Mineur'
```

---

## Structures de données

### Vue d'ensemble

| Structure | Modifiable | Indexable | Itérable | Doublons | Implémentation |
|-----------|-----------|-----------|----------|----------|----------------|
| **str**   | ❌ Non    | ✅ Lecture | ✅ Oui   | ✅ Oui   | Fixed array    |
| **list**  | ✅ Oui    | ✅ L/É     | ✅ Oui   | ✅ Oui   | Variable array |
| **tuple** | ❌ Non    | ✅ Lecture | ✅ Oui   | ✅ Oui   | Fixed array    |
| **set**   | ✅ Oui    | ❌ Non    | ✅ Oui   | ❌ Non   | Hash table     |
| **dict**  | ✅ Oui    | ✅ L/É     | ✅ Oui   | Clés: ❌ | Hash table     |

### Exemples d'utilisation

```python
# Chaîne de caractères (immutable)
my_str = 'Hello world'

# Liste (mutable)
my_list = [0, 1, 2, 3, 4]
my_list[0] = 10  # Modification possible
my_list.append(5)  # Ajout possible

# Tuple (immutable)
my_tuple = (0, 1, 2, 3, 4)
# my_tuple[0] = 10  # ERREUR ! Impossible de modifier

# Set (ensemble - pas de doublons)
my_set = {0, 1, 2, 3, 4}
my_set.add(5)
my_set.add(1)  # Pas d'effet, 1 existe déjà

# Dictionnaire (clé-valeur)
my_dict = {
    0: 'zéro',
    1: 'un',
    2: 'deux',
    3: 'trois',
    4: 'quatre'
}
print(my_dict[2])  # 'deux'
```

---

## Slicing

Le slicing permet d'extraire des portions de séquences (listes, tuples, chaînes).

### Syntaxe
```python
sequence[start:stop:step]
```

### Exemples détaillés

```python
my_list = list(range(0, 10))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Indexation simple
print(my_list[0])      # 0 (premier élément)
print(my_list[-1])     # 9 (dernier élément)
print(my_list[-2])     # 8 (avant-dernier)

# Slicing de base
print(my_list[0:3])    # [0, 1, 2] (indices 0 à 2, 3 exclu)
print(my_list[4:6])    # [4, 5]

# Slicing avec omission
print(my_list[:6])     # [0, 1, 2, 3, 4, 5] (du début jusqu'à 6)
print(my_list[4:])     # [4, 5, 6, 7, 8, 9] (de 4 jusqu'à la fin)
print(my_list[:])      # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] (copie complète)

# Slicing avec step
print(my_list[2:8:2])  # [2, 4, 6] (de 2 à 8, par pas de 2)
print(my_list[::2])    # [0, 2, 4, 6, 8] (tous les 2 éléments)

# Slicing inversé
print(my_list[::-1])   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (inverse)
print(my_list[8:2:-1]) # [8, 7, 6, 5, 4, 3] (de 8 à 2, en arrière)
```

### Application pratique
```python
text = "Hello World"
print(text[0:5])       # "Hello"
print(text[6:])        # "World"
print(text[::-1])      # "dlroW olleH"
```

---

## Boucles et parcours

### Boucle for classique
```python
my_list = [10, 20, 30, 40, 50]

for value in my_list:
    print(value, end=' ')
# Affiche : 10 20 30 40 50
```

### Enumerate - Parcourir avec index
```python
my_list = [10, 20, 30, 40, 50]

for i, value in enumerate(my_list):
    print(f"Index {i}: {value}")

# Affiche :
# Index 0: 10
# Index 1: 20
# Index 2: 30
# Index 3: 40
# Index 4: 50
```

### Zip - Parcourir plusieurs listes simultanément
```python
liste_1 = [0, 1, 2, 3, 4]
liste_2 = [100, 101, 102, 103, 104]

for value1, value2 in zip(liste_1, liste_2):
    print(f"{value1} - {value2}")

# Affiche :
# 0 - 100
# 1 - 101
# 2 - 102
# 3 - 103
# 4 - 104
```

---

## List Comprehension

La list comprehension permet de créer des listes de manière concise et élégante.

### Syntaxe de base
```python
nouvelle_liste = [expression for item in iterable if condition]
```

### Exemples

#### Méthode classique vs Comprehension
```python
# Méthode classique
values = []
for i in range(10):
    if i % 2 == 0:
        values.append(i**2)
print(values)  # [0, 4, 16, 36, 64]

# List comprehension (équivalent)
values2 = [i**2 for i in range(10) if i % 2 == 0]
print(values2)  # [0, 4, 16, 36, 64]
```

#### Avec condition
```python
# Filtrer les nombres pairs
pairs = [i for i in range(10) if i % 2 == 0]
print(pairs)  # [0, 2, 4, 6, 8]
```

#### Avec opérateur ternaire
```python
# Remplacer les nombres pairs par '!'
result = [i if i % 2 else '!' for i in range(10)]
print(result)  # ['!', 1, '!', 3, '!', 5, '!', 7, '!', 9]
```

#### Manipulation de texte
```python
text = 'Hello world'

# Supprimer toutes les lettres 'l'
no_l = [letter for letter in text if letter != 'l']
print(''.join(no_l))  # 'Heo word'

# Version plus directe
no_l = ''.join([i for i in text if i != 'l'])
print(no_l)  # 'Heo word'
```

---

## Références et Garbage Collector

### Concept de référence

En Python, les variables sont des **références** vers des objets en mémoire, pas des copies.

### Types immutables (int, str, tuple)
```python
a = 5
b = 5
print(f'{a=} {b=} {hex(id(a))} {hex(id(b))}')
print(f'Même objet ? {id(a) == id(b)}')  # True

# Les entiers identiques partagent souvent la même adresse mémoire (optimisation Python)

a = 10
b = 5
print(f'Même objet ? {id(a) == id(b)}')  # False maintenant

# Les strings sont immutables
a = 'Allo'
print(hex(id(a)))  # Adresse 1
a = a + ' monde'
print(hex(id(a)))  # Adresse 2 (nouvelle string créée)
```

### Types mutables (list, dict, set)
```python
# Attention avec les listes !
a = [0, 1, 2]
b = a  # b référence le MÊME objet que a

print(f'{a=} {b=}')
print(f'Même objet ? {id(a) == id(b)}')  # True

a[0] = 10  # Modification de a
print(f'{a=} {b=}')  # b est aussi modifié !
# a=[10, 1, 2] b=[10, 1, 2]
```

### Copie profonde (deep copy)
```python
import copy

a = [0, 1, 2]
b = copy.deepcopy(a)  # Vraie copie indépendante

a[0] = 10
print(f'{a=} {b=}')
# a=[10, 1, 2] b=[0, 1, 2]  <- b n'est pas affecté
```

### Résumé
- **Types immutables** (int, float, str, tuple) : Créent de nouveaux objets lors des modifications
- **Types mutables** (list, dict, set) : Les modifications affectent l'objet original
- **Assignation** (`b = a`) : Crée une référence, pas une copie
- **Copie réelle** : Utilisez `copy.deepcopy()` pour les objets mutables

---

## F-strings

Les f-strings (format strings) sont la méthode moderne et recommandée pour formater des chaînes de caractères en Python (depuis Python 3.6).

### Syntaxe de base
```python
nom = "Alice"
age = 25

# Avec f-string
print(f"Je m'appelle {nom} et j'ai {age} ans.")

# Afficher le nom de la variable ET sa valeur
print(f"{age=}")  # age=25
```

### Expressions dans les f-strings
```python
a = 10
b = 5

print(f"La somme de {a} et {b} est {a + b}")
print(f"Le résultat de 2 * 3.14 = {2 * 3.14}")
```

### Formatage de l'alignement et largeur
```python
texte = "Python"
nombre = 42

# Alignement à gauche (<), centré (^), à droite (>)
print(f"{texte:<20}")    # "Python              "
print(f"{texte:^20}")    # "       Python       "
print(f"{texte:>20}")    # "              Python"

# Remplissage avec un caractère
print(f"{nombre:.<20}")  # "42.................."
print(f"{texte:.>20}")   # "..............Python"
```

### Formatage des nombres entiers
```python
nombre = 255

# Différentes bases
print(f"Binaire:      {nombre:b}")    # 11111111
print(f"Octale:       {nombre:o}")    # 377
print(f"Décimale:     {nombre:d}")    # 255
print(f"Hexadécimale: {nombre:x}")    # ff
print(f"Hexadécimale: {nombre:X}")    # FF

# Séparateurs de milliers
grand_nombre = 1000000
print(f"{grand_nombre:,}")  # 1,000,000
print(f"{grand_nombre:_}")  # 1_000_000
```

### Formatage des nombres flottants
```python
pi = 3.141592654

# Précision
print(f"{pi:.2f}")   # 3.14
print(f"{pi:.5f}")   # 3.14159
print(f"{pi:.9f}")   # 3.141592654

# Notation scientifique
print(f"{pi:e}")     # 3.141593e+00
print(f"{pi:E}")     # 3.141593E+00
print(f"{pi:.2e}")   # 3.14e+00

# Pourcentages
valeur = 0.75
print(f"{valeur:.1%}")  # 75.0%
print(f"{1.0:.2%}")     # 100.00%
```

### Formatage des dates
```python
from datetime import datetime

maintenant = datetime.now()

# Différents formats de date et heure
print(f"Date: {maintenant:%d/%m/%Y}")           # 07/11/2025
print(f"Heure: {maintenant:%H:%M:%S}")          # 14:30:45
print(f"Complet: {maintenant:%d/%m/%Y %H:%M}") # 07/11/2025 14:30
```

### Valeurs par défaut avec 'or'
```python
valeur1 = "CVM"
valeur2 = None

print(f"{valeur1 or 'par défaut'}")  # CVM
print(f"{valeur2 or 'par défaut'}")  # par défaut
```

### Accolades littérales
```python
# Pour afficher des accolades, doublez-les
print(f"Les accolades: {{valeur}}")  # Les accolades: {valeur}
```

---

## Programmation Orientée Objet

### Classe de base

```python
class Human:
    
    def __init__(self, name):
        """Initialisateur (constructeur)"""
        self.name = name
        self.age = 0
    
    def tic(self):
        """Méthode pour augmenter l'âge"""
        self.age += 1
    
    def print(self):
        """Afficher les informations"""
        print(f"Un '{type(self).__name__}' nommé {self.name} a {self.age:02} an{'s' if self.age > 1 else ''}")


# Utilisation
humain = Human('Roger')
humain.tic()
humain.print()  # Un 'Human' nommé Roger a 01 an
```

### Encapsulation et conventions

En Python, l'encapsulation est une **convention**, pas une restriction technique.

```python
class GameCharacter:
    
    def __init__(self, name, health, power):
        # Public : accessible partout
        self.name = name
        
        # Protected : accessible mais ne devrait pas être modifié directement
        # Convention : préfixe avec _
        self._health = health
        
        # Private : vraiment privé grâce au "name mangling"
        # Convention : préfixe avec __
        self.__power = power
```

### Name Mangling

Le name mangling transforme les attributs privés pour les rendre difficiles d'accès.

```python
class GameCharacter:
    def __init__(self, name, health, power):
        self.__power = power

roger = GameCharacter("Roger", 100, 15)

# Accès impossible directement
# print(roger.__power)  # AttributeError

# Mais accessible via le name mangling (à éviter !)
print(roger._GameCharacter__power)  # 15
```

### Properties (getters et setters)

Les properties permettent de contrôler l'accès aux attributs.

```python
class Human:
    
    def __init__(self, name):
        self.__name = None
        self.__age = 0
        self.name = name  # Passe par le setter
    
    @property
    def name(self):
        """Getter pour name"""
        return self.__name
    
    @name.setter
    def name(self, value):
        """Setter pour name avec validation"""
        if not isinstance(value, str):
            raise TypeError('Le nom doit être une chaîne de caractères')
        if len(value) < 2:
            raise ValueError("Le nom doit être d'au moins 2 caractères")
        self.__name = value
    
    @property
    def age(self):
        """Getter pour age (lecture seule)"""
        return self.__age
    
    def tic(self):
        """Seule méthode pour modifier l'âge"""
        self.__age += 1


# Utilisation
u = Human('Gustave')
print(u.name)  # Gustave

# u = Human(123)  # TypeError: Le nom doit être une chaîne de caractères
# u.name = 'G'    # ValueError: Le nom doit être d'au moins 2 caractères

u.tic()
print(u.age)  # 1
# u.age = 10  # AttributeError: can't set attribute
```

### Méthodes d'instance

```python
class GameCharacter:
    def __init__(self, name):
        self.name = name
    
    def attack(self):
        print(f"{self.name} attaque !")

roger = GameCharacter("Roger")

# Deux façons équivalentes d'appeler une méthode
roger.attack()                      # Méthode préférée
GameCharacter.attack(roger)         # Équivalent mais plus verbeux
```

### Attributs de classe vs d'instance

```python
class Character:
    # Attribut de classe (partagé par toutes les instances)
    species = "Human"
    
    def __init__(self, name):
        # Attribut d'instance (unique à chaque instance)
        self.name = name

c1 = Character("Alice")
c2 = Character("Bob")

print(c1.species)  # Human
print(c2.species)  # Human

# Modification de l'attribut de classe
Character.species = "Elf"
print(c1.species)  # Elf
print(c2.species)  # Elf
```

---

## NumPy

NumPy est une bibliothèque fondamentale pour le calcul scientifique en Python.

### Installation et import
```python
import numpy as np
```

### Créer des arrays

```python
# À partir d'une liste
liste = [9.50, 33.50, 30.25, 10.75]
arr = np.array(liste)

# Array de zéros
zeros = np.zeros((3, 4))  # Matrice 3x4 de zéros

# Array de uns
ones = np.ones((2, 3))    # Matrice 2x3 de uns

# Array avec une plage de valeurs
range_arr = np.arange(0, 10, 2)  # [0, 2, 4, 6, 8]

# Array avec type spécifique
binary_img = np.zeros((100, 100), dtype=np.uint8)
```

### Opérations statistiques de base

```python
salaire_horaire = np.array([9.50, 33.50, 30.25, 10.75, 41.50])

# Somme
total = np.sum(salaire_horaire)
print(f"Total: {total}")

# Moyenne
moyenne = np.mean(salaire_horaire)  # ou np.average()
print(f"Moyenne: {moyenne}")

# Médiane
mediane = np.median(salaire_horaire)
print(f"Médiane: {mediane}")

# Minimum et Maximum
mini = np.min(salaire_horaire)
maxi = np.max(salaire_horaire)
print(f"Min: {mini}, Max: {maxi}")

# Écart-type
std = np.std(salaire_horaire)
print(f"Écart-type: {std}")
```

### Indexation et filtrage booléen

```python
salaire_horaire = np.array([9.50, 33.50, 30.25, 10.75, 41.50])

# Filtrage booléen
salaires_bas = salaire_horaire[salaire_horaire < 15.5]
print(salaires_bas)  # [9.5  10.75]

# Compter les éléments qui satisfont une condition
nb_hauts_salaires = np.count_nonzero(salaire_horaire >= 30)
# ou équivalent :
nb_hauts_salaires = np.sum(salaire_horaire >= 30)
print(nb_hauts_salaires)  # 3
```

### Opérations vectorisées

```python
# Opérations élément par élément (sans boucle !)
salaires = np.array([10, 15, 20, 25])

# Augmentation de 10%
nouveaux_salaires = salaires * 1.1
print(nouveaux_salaires)  # [11.  16.5 22.  27.5]

# Opérations multiples
calcul = salaires * 37.5 * 52  # salaire annuel
print(calcul)
```

### Manipulation d'images binaires

```python
# Créer une image binaire (0 ou 1)
def create_image(size):
    return np.zeros((size[1], size[0]), dtype=np.uint8)

# Remplir l'image
def fill(image, color=1):
    image[:] = color

# Dessiner un rectangle
def draw_rectangle(image, top_left, bottom_right):
    x0, y0 = top_left
    x1, y1 = bottom_right
    image[y0:y1, x0:x1] = 1

# Utilisation
img = create_image((100, 100))
draw_rectangle(img, (10, 10), (50, 50))
```

### Meshgrid - Créer des grilles de coordonnées

```python
# Créer une grille pour dessiner un cercle
def draw_circle(image, center, radius):
    # Créer des grilles de coordonnées x et y
    cols, rows = np.meshgrid(
        np.arange(image.shape[1]), 
        np.arange(image.shape[0])
    )
    
    # Calculer la distance de chaque pixel au centre
    dist = np.sqrt((rows - center[1])**2 + (cols - center[0])**2)
    
    # Mettre à 1 tous les pixels dans le rayon
    image[dist <= radius] = 1
```

### Générateur de nombres aléatoires

```python
# Nouvelle méthode (recommandée)
rng = np.random.default_rng()

# Nombres aléatoires entre 0 et 1
random_vals = rng.random((3, 4))  # Matrice 3x4

# Entiers aléatoires
random_ints = rng.integers(0, 100, size=10)  # 10 entiers entre 0 et 99

# Remplir une image aléatoirement
def randomize(image, percent=0.5):
    rng = np.random.default_rng()
    image[:] = (rng.random(image.shape) <= percent).astype(image.dtype)
```

### Calculs géométriques

```python
# Calculer l'aire d'une forme dans une image binaire
def area(image):
    return np.sum(image)

# Calculer le centroïde d'une forme
def centroid(image):
    cols, rows = np.meshgrid(
        np.arange(image.shape[1]), 
        np.arange(image.shape[0])
    )
    total_area = area(image)
    
    cx = np.sum(cols * image) / total_area
    cy = np.sum(rows * image) / total_area
    
    return (cx, cy)
```

---

## Exercices pratiques recommandés

### Niveau 1 : Bases
1. Créer une fonction qui prend une liste et retourne seulement les nombres pairs
2. Utiliser list comprehension pour créer une liste des carrés de 0 à 9
3. Créer une classe `Voiture` avec des attributs et méthodes de base

### Niveau 2 : Intermédiaire
1. Créer une classe avec des properties pour valider les données
2. Utiliser NumPy pour calculer des statistiques sur des données salariales
3. Implémenter des fonctions de dessin d'images binaires

### Niveau 3 : Avancé
1. Créer un système de gestion de personnages de jeu avec héritage
2. Implémenter des algorithmes de traitement d'image avec NumPy
3. Combiner plusieurs concepts (OOP, NumPy, list comprehension)

---

## Ressources supplémentaires

### Documentation officielle
- Python : https://docs.python.org/3/
- PEP8 : https://www.python.org/dev/peps/pep-0008/
- NumPy : https://numpy.org/doc/

### Outils de développement
- **Debugger** : Apprendre à utiliser les breakpoints dans votre IDE
- **Linter** : Utiliser pylint ou flake8 pour vérifier la conformité PEP8
- **Formateur** : Utiliser black ou autopep8 pour formater automatiquement le code

---

## Checklist avant de soumettre votre code

- [ ] Le code respecte PEP8 (indentation, nommage, espaces)
- [ ] Pas de code dupliqué (principe DRY)
- [ ] Les fonctions ont des noms descriptifs
- [ ] Le code a été testé avec le debugger
- [ ] Les classes utilisent correctement l'encapsulation
- [ ] Les f-strings sont utilisées pour le formatage
- [ ] Les opérations sur arrays NumPy sont vectorisées (pas de boucles inutiles)
- [ ] Le code est commenté seulement quand nécessaire (pas de commentaires évidents)

---

*Documentation créée pour le cours C52 - Python*
*Dernière mise à jour : 2025*
