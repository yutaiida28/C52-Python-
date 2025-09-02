
# Introduction à Python - Cours 2

## Partie 2b

### Programmation orientée objet

- Généralités et rappels :
    - La POO est un paradigme de programmation qui permet de modéliser des objets du monde réel (abstraits ou concrets) en utilisant des classes et des objets.
    - La POO permet de structurer le code en regroupant les données et les comportements associés dans des entités appelées classes. 
    - Une classe est une définition d'un type d'objet, tandis qu'un objet est une instance de cette classe.
    - La POO permet de créer des objets qui encapsulent des données et des comportements, facilitant ainsi la réutilisation du code et la modularité. `DRY`
    - Rappelez-vous les grands principes de la POO :
        - **Abstraction** : représenter des concepts abstraits et concrets par des classes et des objets simples.
        - **Encapsulation** : regrouper les données et les comportements associés dans une classe.
        - **Héritage** : permettre à une classe de hériter des propriétés et des méthodes d'une autre classe.
        - **Polymorphisme** : permettre à des objets de différentes classes d'être traités de manière uniforme.
    - La POO n'est pas sans faille et ne prétend pas être la solution à tous les problèmes de programmation. Comme tous les paradigmes de programmation, elle offre des avantages et des inconvénients. Comme tout, son usage est une question de compromis. Néanmoins, son importance dans l'industrie et le développement logiciel fait d'elle le paradigme le plus important dans l'apprentissage du métier. Elle permet un excellent formalisme, une abstraction des concepts en jeu et une excellente organisation du code.

- En Python :
    - En Python, la programmation orientée objet (POO) est fondamentale. En fait, Python est un langage orienté objet par défaut. Plus précisément, **tout** est un objet en Python, y compris les fonctions et les types de données primitifs.
    - Déclaration d'une classe :
        - En Python, les classes sont définies à l'aide du mot-clé `class` suivi du nom de la classe et d'un deux-points `:`.
        - Les attributs (variables) et les opérations (méthodes ou fonctions) de la classe sont définis à l'intérieur de la classe.
        - Contrairement aux langages statiques C++ et Java, la déclaration des attributs n'est pas limitée à la définition statique de la classe, ils peuvent être ajouté dynamiquement à n'importe quel moment.
        - Les attributs sont généralement définis dans la méthode spéciale `__init__`, qui est appelée lors de la création d'une instance de la classe. Cette méthode permet d'initialiser les attributs de l'objet. Nous reviendrons en détail sur cette méthode dans d'autres cours.
        - Les opérations sont généralement définies comme des méthodes de la classe, en utilisant le mot-clé `def` suivi du nom de la méthode et d'un deux-points `:`. La première variable d'une méthode **est toujours** `self`, qui fait référence à l'instance de la classe (exactement comme `this` de C++ et Java). La différence est que `self` doit être explicitement déclaré dans la définition de la méthode en Python alors qu'il est implicite en C++ et Java.
        - Python ne supporte pas les modificateurs d'accès (le masquage : `package`,`public`, `protected` et `private`) comme en C++ et Java. Nous reviendrons sur ce sujet plus tard cette session. 
    - Héritage :
        - L'héritage est également pris en charge en Python, permettant à une classe de hériter des propriétés et des méthodes d'une autre classe. La syntaxe pour l'héritage est `class NomDeLaClasse(NomDeLaClasseParent):`.
        - Contrairement à Java mais comme C++, Python supporte l'héritage multiple, ce qui signifie qu'une classe peut hériter de plusieurs classes parentes.
    - Polymorphisme :
        - Le polymorphisme est également pris en charge, permettant à des objets de différentes classes d'être traités de manière uniforme. 
        - Contrairement à C++ et Java, il n'y a pas de mots réservés comme `virtual`, `override` et `final` spécifiques pour déclarer le polymorphisme.
        - En fait, il suffit de définir des méthodes avec le même nom dans différentes classes pour que le polymorphisme fonctionne (_override_ implicite).
    - Instanciation d'une classe, création d'un objet :
        - Pour créer une instance (un objet) d'une classe, il suffit d'appeler le nom de la classe comme une fonction, en passant les arguments requis par la méthode `__init__` si nécessaire.
        - Contrairement à d'autres langages, il n'existe pas d'opérateur `new` en Python. De plus, comme en Java et contrairement à C++, Python utilise un _garbage collector_ pour gérer automatiquement la mémoire. Donc, pas besoin d'utiliser manuellement la fonction `free` ou l'opérateur `delete`.
        - Par exemple, si la classe s'appelle `MaClasse`, on peut créer une instance en écrivant `mon_objet = MaClasse()`.
    - Le sujet du _POO- est vaste et complexe. Il reste plusieurs autres concepts importants à aborder, tels que les classes abstraites, les interfaces, les propriétés, les décorateurs, etc. 

```Python
# Exemple de définition de classe

# Déclaration de la classe
class UneClasse:

    # Méthode spéciale d'initialisation
    def __init__(self, valeur = 0):
        # On crée un attribut 'valeur' pour l'objet
        self.valeur = valeur

    # Définition d'une méthode
    def afficher(self):
        print("Valeur :", self.valeur)

# Exemple d'instanciation de la classe et d'utilisation de l'objet
obj_1 = UneClasse() # <<< Création d'une instance de la classe
obj_2 = UneClasse(42) # <<< Création d'une instance de la classe

# Accès direct à un attribut de l'objet
print(obj_1.valeur)  # <<< en lecture
obj_1.valeur = 100 # <<< en écriture

# Appel d'une méthode de l'objet
obj_1.afficher()
```




## Gestion d'exceptions

- En Python, la gestion des exceptions est effectuée à l'aide des mots-clés `try`, `except`, `finally` et `raise`.
- Le bloc `try` contient le code qui peut potentiellement générer une exception. Si une exception se produit, le flux d'exécution est transféré au bloc `except`.
- Le bloc `except` contient le code qui gère l'exception. Il est possible 
    - de capturer des exceptions spécifiques en spécifiant le type d'exception après le mot-clé `except`
    - d'avoir plusieurs blocs `except` pour gérer différents types d'exceptions
    - d'utiliser un bloc `except` sans spécifier de type d'exception pour capturer toutes les exceptions 
- Le bloc `finally` est optionnel et contient le code qui sera exécuté à la fin, qu'une exception se soit produite ou non. Il est souvent utilisé pour libérer des ressources ou effectuer des opérations de nettoyage.
- Le mot-clé `raise` est utilisé pour déclencher une exception manuellement. Il peut être utilisé pour signaler des erreurs spécifiques ou pour relancer une exception capturée.
- Il existe des exceptions intégrées en Python, telles que `ValueError`, `TypeError`, `IndexError`, `KeyError`, etc. Il est également possible de créer des exceptions personnalisées en définissant une nouvelle classe qui hérite de la classe `Exception`.

```Python
# Exemple complet de gestion d'exceptions

def process(data, index):
    if not isinstance(data, list):
        raise TypeError("data doit être une liste")
    if len(data) == 0:
        raise ValueError("data ne peut pas être vide")
    if index < 0 or index >= len(data):
        raise IndexError("index hors limites")
    
    return data[index]

value = [0, 1, 2, 3, 4]

try:
    result = process(value, 10)
    print("Résultat :", result)
except TypeError as e:
    print("TypeError :", e)
except ValueError as e:
    print("ValueError :", e)
except IndexError as e:
    print("IndexError :", e)
except Exception as e:  # capture toutes les autres exceptions
    print("Exception inattendue :", e)
finally:
    print("Fin du traitement")

``` 






## main

- Fonction `main`
    - En Python, il n'y a pas de fonction `main` par défaut comme dans d'autres langages (C, C++, Java, ...). Cependant, il est courant de définir une fonction `main` pour organiser le code principal du programme.
    - La convention est de définir une fonction `main()` et de l'appeler à la fin du script, en utilisant la condition `if __name__ == "__main__":` pour s'assurer que le code ne s'exécute que si le script est exécuté directement, et non importé en tant que module.
    - Cette convention permet de structurer le code et de le rendre plus lisible, en séparant la logique principale du reste du code. De plus, cela permet de ne pas polluer l'espace de noms global avec des variables et des fonctions définies dans le script.
    - Exemple :
```Python
# Exemple de fonction main

def utility_function():
    print("Ceci est une fonction utilitaire.")

def main():
    # Code principal du programme
    var = 0
    utility_function()
    

if __name__ == "__main__": # <<< Nous reviendrons sur cette syntaxe plus tard
    main()
```


## Modules personnalisés

Pour créer un module personnalisé en Python, il suffit de créer un fichier texte avec l'extension `.py` contenant le code souhaité. Le nom du fichier sera le nom du module.

Ce fichier peut être le point d'entrée principal du programme (le script principal) ou un fichier séparé contenant des fonctions, des classes ou des variables réutilisables.

Pour l'instant, on simplifiera l'importation de fichier en plaçant tous les fichiers dans le même répertoire. Dans d'autres cours, nous verrons comment organiser les modules dans des répertoires et des packages.

```Python
# Fichier my_module.py

une_variable_globale = 42 # HAAAA! Pas de variables globales! (sauf pour quelques exceptions)
UNE_CONSTANTE_GLOBALE = 24 # Ok pour les constantes globales.

def une_fonction(param):
    return param * 2

class UneClasse:
    def __init__(self, value):
        self.value = value

    def afficher(self):
        print("Valeur :", self.value)
```

```Python
# Fichier main.py
# Fichier principal correspondant au point d'entrée souhaité du programme

import my_module as mymo

def main():
    # Code principal du programme
    variable_locale = mymo.UneClasse()
    variable_locale.afficher()
    # ...

if __name__ == "__main__": # Le point d'entrée officiel du programme
    main()
```

### Exercices 4

- Exercice 4.1 : 
    - Créer une classe qui représente un dé nommée `Dice`.
    - La fonction d'initialisation `__init__` doit permettre de définir le nombre de faces du dé (entre 4 et 20, par défaut 6).
    - La classe doit avoir une méthode `roll()` qui simule un lancer de dé et retourne un entier aléatoire entre 1 et le nombre de faces du dé.
    - Créer un module `dice.py` qui contient la définition de la classe `Dice`.
    - Créer un fichier `main.py` qui importe le module `dice` et utilise la classe `Die` pour créer 4 dés de 4, 6, 8 et 12 faces respectivement.
    - Le programme fait 10 lancers de chaque dé et, pour chaque tour, affiche les résultats de chaque dé ainsi que la somme des résultats.
- Exercice 4.2 :
    - Créer un module `math_utils.py` qui contient les fonctions suivantes :
        - `factorial(n)` : calcule et retourne la factorielle de _n_ (n!)
            - si _n_ est négatif, lever une exception `ValueError` ou afficher un message d'erreur et retourner -1
            - si _n_ = 0, retourne 1
            - si _n_ > 0, retourne 1 * 2 * 3 * ... * n
        - `triangular(n)` : calcule et retourne le nombre triangulaire de _n_
            - si _n_ est négatif, lever une exception `ValueError` ou afficher un message d'erreur et retourner -1
            - si _n_ >= 0, retourne 0 + 1 + 2 + 3 + ... + n
        - `is_prime(n)` : vérifie si _n_ est un nombre premier et retourne `True` ou `False` 
            - un nombre premier est un entier naturel **supérieur à 1** qui n'a que deux diviseurs distincts : 1 et lui-même
            - voici l'approche à utiliser :
                - si _n_ est inférieur ou égal à 1, lever une exception `ValueError` ou afficher un message d'erreur et retourner -1
                - si _n_ est 2, retourne `True`
                - si _n_ est pair, retourne `False`
                - parcourir tous les nombre impairs à partir de 3 jusqu'à _m_ (où  `m = floor(sqrt(n))`) et analyser si le _i_ nombre divise _n_ sans reste
                    - retourner `False` si un diviseur est trouvé
                    - retourner `True` si aucun diviseur n'est trouvé
    - Créer un fichier `main.py` qui importe le module `math_utils` et utilise les fonctions `factorial` et `is_prime` pour afficher la factorielle de 5 et vérifier si 7 est un nombre premier.

- Exercice 4.3 :
    - Créer un module contenant une classe `BankAccount` qui représente un compte bancaire.
        - La fonction d'initialisation doit permettre de définir le nom du titulaire du compte et le solde initial (par défaut 0).
        - La classe doit avoir les méthodes suivantes :     
            - `deposit(amount)` : permet de déposer une somme d'argent sur le compte. Si le montant est négatif ou nul, lever une exception `ValueError`.
            - `withdraw(amount)` : permet de retirer une somme d'argent du compte. Si le montant est négatif ou nul, lever une exception `ValueError`. Si le montant est supérieur au solde, lever une exception `ValueError`.
            - `get_balance()` : retourne le solde actuel du compte.
            - `get_account_holder()` : retourne le nom du titulaire du compte.
    - Créer un module contenant une classe `Bank` qui représente une banque.
        - La fonction d'initialisation doit permettre de définir le nom de la banque.
        - La classe doit avoir les méthodes suivantes :
            - `add_account(account)` : permet d'ajouter un compte bancaire à la banque.
            - `remove_account(account)` : permet de retirer un compte bancaire de la banque.
            - `get_total_balance()` : retourne le solde total de tous les comptes de la banque.
    - Créer un fichier `main.py` qui crée une instance de la classe `Bank`, ajouter plusieurs comptes bancaires à la banque, effectue des dépôts et des retraits sur les comptes, et affiche le solde total de la banque.


