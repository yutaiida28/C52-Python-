# Les 8 Voisins et le Calcul du Périmètre avec NumPy

## Table des matières
1. [Concept des 8 voisins](#concept-des-8-voisins)
2. [Game of Life - Calcul des voisins](#game-of-life)
3. [Slicing avancé pour accéder aux voisins](#slicing-avancé)
4. [Calcul du périmètre avec NumPy](#calcul-du-périmètre)
5. [Exemple complet étape par étape](#exemple-complet)

---

## Concept des 8 voisins

### Grille de voisinage

Pour une cellule à la position `(x, y)`, les 8 voisins sont disposés ainsi :

```
┌─────────┬─────────┬─────────┐
│ (x-1,   │ (x,     │ (x+1,   │
│  y-1)   │  y-1)   │  y-1)   │
│  NW     │  N      │  NE     │
├─────────┼─────────┼─────────┤
│ (x-1,   │  [X,Y]  │ (x+1,   │
│  y)     │ CELLULE │  y)     │
│  W      │ ACTUELLE│  E      │
├─────────┼─────────┼─────────┤
│ (x-1,   │ (x,     │ (x+1,   │
│  y+1)   │  y+1)   │  y+1)   │
│  SW     │  S      │  SE     │
└─────────┴─────────┴─────────┘

Légende:
NW = Nord-Ouest    N = Nord      NE = Nord-Est
W  = Ouest         •  = Cellule  E  = Est
SW = Sud-Ouest     S = Sud       SE = Sud-Est
```

### Les 8 directions en coordonnées

```python
# Offsets relatifs pour accéder aux 8 voisins
voisins = [
    (-1, -1),  # Nord-Ouest
    ( 0, -1),  # Nord
    ( 1, -1),  # Nord-Est
    (-1,  0),  # Ouest
    ( 1,  0),  # Est
    (-1,  1),  # Sud-Ouest
    ( 0,  1),  # Sud
    ( 1,  1)   # Sud-Est
]
```

---

## Game of Life - Calcul des voisins

### Approche classique (avec boucles)

```python
def count_neighbors_classic(world, x, y):
    """Compte les voisins vivants d'une cellule (méthode classique)"""
    count = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:  # Ignorer la cellule elle-même
                continue
            # Compter les voisins vivants
            count += world[x + dx][y + dy]
    return count
```

### Approche optimisée (avec slicing)

Dans le code `gol_engine_solution_2.py`, on utilise le slicing de Python :

```python
def count_neighbors_optimized(world, x, y):
    """Compte les voisins vivants avec slicing Python"""
    neighbours = sum(world[x-1][y-1:y+2]) \    # Ligne du haut (3 cellules)
               + sum(world[x][y-1:y+2:2]) \     # Ligne du milieu (2 cellules, saute le centre)
               + sum(world[x+1][y-1:y+2])       # Ligne du bas (3 cellules)
    return neighbours
```

#### Explication détaillée du slicing

Visualisons pour une cellule à `(x=5, y=5)` :

```
Position:        y-1  y  y+1
                 (4) (5) (6)

world[x-1][y-1:y+2]  →  world[4][4:7]  →  [4][4], [4][5], [4][6]  (3 cellules)
                        ╔═══════════════════════════╗
                        ║ Ligne du HAUT (x-1)      ║
                        ╚═══════════════════════════╝

world[x][y-1:y+2:2]  →  world[5][4:7:2] →  [5][4], [5][6]  (2 cellules, step=2)
                        ╔═══════════════════════════╗
                        ║ Ligne du MILIEU (x)      ║
                        ║ Saute y=5 (la cellule)   ║
                        ╚═══════════════════════════╝

world[x+1][y-1:y+2]  →  world[6][4:7]  →  [6][4], [6][5], [6][6]  (3 cellules)
                        ╔═══════════════════════════╗
                        ║ Ligne du BAS (x+1)       ║
                        ╚═══════════════════════════╝

TOTAL: 3 + 2 + 3 = 8 voisins
```

### Table de recherche (LUT - Look-Up Table)

Le code utilise une LUT pour les règles de Game of Life :

```python
# Index = nombre de voisins vivants (0 à 8)
# Valeur = nouvelle valeur de la cellule (0 ou 1)

# Règle pour cellule MORTE (0)
dead_rule  = (0, 0, 0, 1, 0, 0, 0, 0, 0)
#             0  1  2  3  4  5  6  7  8  ← nombre de voisins
#                      ↑
#                      Naissance avec 3 voisins

# Règle pour cellule VIVANTE (1)
alive_rule = (0, 0, 1, 1, 0, 0, 0, 0, 0)
#             0  1  2  3  4  5  6  7  8  ← nombre de voisins
#                   ↑  ↑
#                   Survie avec 2 ou 3 voisins

# Utilisation:
rules = (dead_rule, alive_rule)
nouvelle_valeur = rules[cellule_actuelle][nombre_voisins]
```

---

## Slicing avancé pour accéder aux voisins

### Principe du slicing pour les voisins en NumPy

Avec NumPy, on peut accéder à TOUS les voisins d'une grille en une seule opération !

#### Exemple visuel

Soit une image 10×10 :

```
image[:-1, :]    = Toutes les lignes SAUF la dernière  (décalage vers le haut)
image[1:, :]     = Toutes les lignes SAUF la première  (décalage vers le bas)
image[:, :-1]    = Toutes les colonnes SAUF la dernière (décalage vers la gauche)
image[:, 1:]     = Toutes les colonnes SAUF la première (décalage vers la droite)
```

#### Visualisation avec une grille 5×5

```
Image originale:
┌───┬───┬───┬───┬───┐
│ 0 │ 1 │ 2 │ 3 │ 4 │  ← Ligne 0
├───┼───┼───┼───┼───┤
│ 5 │ 6 │ 7 │ 8 │ 9 │  ← Ligne 1
├───┼───┼───┼───┼───┤
│10 │11 │12 │13 │14 │  ← Ligne 2
├───┼───┼───┼───┼───┤
│15 │16 │17 │18 │19 │  ← Ligne 3
├───┼───┼───┼───┼───┤
│20 │21 │22 │23 │24 │  ← Ligne 4
└───┴───┴───┴───┴───┘

image[:-1, :]  (Décalage HAUT - on retire la dernière ligne)
┌───┬───┬───┬───┬───┐
│ 0 │ 1 │ 2 │ 3 │ 4 │
├───┼───┼───┼───┼───┤
│ 5 │ 6 │ 7 │ 8 │ 9 │
├───┼───┼───┼───┼───┤
│10 │11 │12 │13 │14 │
├───┼───┼───┼───┼───┤
│15 │16 │17 │18 │19 │
└───┴───┴───┴───┴───┘

image[1:, :]  (Décalage BAS - on retire la première ligne)
┌───┬───┬───┬───┬───┐
│ 5 │ 6 │ 7 │ 8 │ 9 │
├───┼───┼───┼───┼───┤
│10 │11 │12 │13 │14 │
├───┼───┼───┼───┼───┤
│15 │16 │17 │18 │19 │
├───┼───┼───┼───┼───┤
│20 │21 │22 │23 │24 │
└───┴───┴───┴───┴───┘

image[:, :-1]  (Décalage GAUCHE - on retire la dernière colonne)
┌───┬───┬───┬───┐
│ 0 │ 1 │ 2 │ 3 │
├───┼───┼───┼───┤
│ 5 │ 6 │ 7 │ 8 │
├───┼───┼───┼───┤
│10 │11 │12 │13 │
├───┼───┼───┼───┤
│15 │16 │17 │18 │
├───┼───┼───┼───┤
│20 │21 │22 │23 │
└───┴───┴───┴───┘

image[:, 1:]  (Décalage DROITE - on retire la première colonne)
┌───┬───┬───┬───┐
│ 1 │ 2 │ 3 │ 4 │
├───┼───┼───┼───┤
│ 6 │ 7 │ 8 │ 9 │
├───┼───┼───┼───┤
│11 │12 │13 │14 │
├───┼───┼───┼───┤
│16 │17 │18 │19 │
├───┼───┼───┼───┤
│21 │22 │23 │24 │
└───┴───┴───┴───┘
```

### Pourquoi les dimensions changent ?

```python
image.shape = (5, 5)

image[:-1, :].shape = (4, 5)  # On perd une ligne
image[1:, :].shape = (4, 5)   # On perd une ligne
image[:, :-1].shape = (5, 4)  # On perd une colonne
image[:, 1:].shape = (5, 4)   # On perd une colonne
```

**Important** : C'est pourquoi on doit comparer des slices de même taille !

---

## Calcul du périmètre

### Concept du périmètre

Le périmètre d'une forme est la somme de tous les **bords** de la forme qui touchent le fond (0).

#### Qu'est-ce qu'un bord ?

Un pixel de la forme (valeur 1) est sur un **bord** si au moins un de ses 4 voisins directs (haut, bas, gauche, droite) est à 0.

```
Exemple:
  0  0  0  0  0
  0  1  1  1  0
  0  1  1  1  0
  0  1  1  1  0
  0  0  0  0  0

Le pixel central (1) n'est PAS un bord (tous ses voisins sont à 1)
Les pixels sur les côtés SONT des bords (ils touchent des 0)
```

### Algorithme du périmètre expliqué

Voici l'algorithme que vous avez fourni, avec explications :

```python
def perimeter(image):
    # 1. Créer un masque booléen de la forme
    form_mask = image != 0
    # Si image[i,j] = 1, alors form_mask[i,j] = True
    # Si image[i,j] = 0, alors form_mask[i,j] = False
    
    # 2. Créer des vues décalées pour chaque direction (4 voisins cardinaux)
    top = form_mask[:-1, :]     # Voisin du HAUT
    bottom = form_mask[1:, :]   # Voisin du BAS
    left = form_mask[:, :-1]    # Voisin de GAUCHE
    right = form_mask[:, 1:]    # Voisin de DROITE
    
    # 3. Détecter les bords dans chaque direction
    # Un pixel est sur un bord si :
    # - Il appartient à la forme (True dans form_mask)
    # - Son voisin n'appartient PAS à la forme (~top = NOT top)
    
    top_edge = form_mask[1:, :] & ~top
    # "Pour chaque pixel (sauf première ligne), est-il à 1 ET son voisin du haut à 0 ?"
    
    bottom_edge = form_mask[:-1, :] & ~bottom
    # "Pour chaque pixel (sauf dernière ligne), est-il à 1 ET son voisin du bas à 0 ?"
    
    left_edge = form_mask[:, 1:] & ~left
    # "Pour chaque pixel (sauf première colonne), est-il à 1 ET son voisin gauche à 0 ?"
    
    right_edge = form_mask[:, :-1] & ~right
    # "Pour chaque pixel (sauf dernière colonne), est-il à 1 ET son voisin droit à 0 ?"
    
    # 4. Détecter les coins (pour éviter de les compter deux fois)
    # Un coin est un pixel qui a un bord dans DEUX directions
    
    top_left_corner = form_mask[1:, 1:] & ~top[:, 1:] & ~left[1:, :]
    top_right_corner = form_mask[1:, :-1] & ~top[:, :-1] & ~right[1:, :]
    bottom_left_corner = form_mask[:-1, 1:] & ~bottom[:, 1:] & ~left[:-1, :]
    bottom_right_corner = form_mask[:-1, :-1] & ~bottom[:, :-1] & ~right[:-1, :]
    
    # 5. Calculer le périmètre
    # Somme des bords - somme des coins (pour éviter le double comptage)
    perimeter = (np.sum(top_edge) + np.sum(bottom_edge) + 
                 np.sum(left_edge) + np.sum(right_edge) - 
                 (np.sum(top_left_corner) + np.sum(top_right_corner) + 
                  np.sum(bottom_left_corner) + np.sum(bottom_right_corner)))
    
    return perimeter
```

### Pourquoi soustraire les coins ?

Les coins sont comptés **deux fois** : une fois dans le bord horizontal ET une fois dans le bord vertical.

```
Exemple d'un coin:
    0  0  0
    0  1  1
    0  1  1

Le pixel (1,1) est détecté comme:
- Bord supérieur (son voisin du haut est 0)
- Bord gauche (son voisin de gauche est 0)

Sans correction, on compterait ce pixel deux fois !
En détectant les coins et en les soustrayant, on corrige ce double comptage.
```

---

## Exemple complet étape par étape

Utilisons l'image que vous avez fournie :

```python
image = [[0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,1,1,0,0,0,0],
         [0,0,0,1,1,1,1,0,0,0],
         [0,0,0,1,1,1,1,0,0,0],
         [0,0,0,0,1,1,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0]]
```

### Visualisation de la forme

```
   0  1  2  3  4  5  6  7  8  9
0  .  .  .  .  .  .  .  .  .  .
1  .  .  .  .  .  .  .  .  .  .
2  .  .  .  .  .  .  .  .  .  .
3  .  .  .  .  █  █  .  .  .  .
4  .  .  .  █  █  █  █  .  .  .
5  .  .  .  █  █  █  █  .  .  .
6  .  .  .  .  █  █  .  .  .  .
7  .  .  .  .  .  .  .  .  .  .
8  .  .  .  .  .  .  .  .  .  .
9  .  .  .  .  .  .  .  .  .  .
```

### Étape 1 : Créer le masque de la forme

```python
form_mask = image != 0
```

```
form_mask (True = fait partie de la forme)
   0  1  2  3  4  5  6  7  8  9
0  F  F  F  F  F  F  F  F  F  F
1  F  F  F  F  F  F  F  F  F  F
2  F  F  F  F  F  F  F  F  F  F
3  F  F  F  F  T  T  F  F  F  F
4  F  F  F  T  T  T  T  F  F  F
5  F  F  F  T  T  T  T  F  F  F
6  F  F  F  F  T  T  F  F  F  F
7  F  F  F  F  F  F  F  F  F  F
8  F  F  F  F  F  F  F  F  F  F
9  F  F  F  F  F  F  F  F  F  F
```

### Étape 2 : Créer les vues décalées

```python
top = form_mask[:-1, :]     # Lignes 0-8
bottom = form_mask[1:, :]   # Lignes 1-9
left = form_mask[:, :-1]    # Colonnes 0-8
right = form_mask[:, 1:]    # Colonnes 1-9
```

Comparons `form_mask` avec `top` (décalé vers le haut) :

```
form_mask[1:, :]  (lignes 1-9)        top = form_mask[:-1, :]  (lignes 0-8)
   0  1  2  3  4  5  6  7  8  9          0  1  2  3  4  5  6  7  8  9
1  F  F  F  F  F  F  F  F  F  F      0  F  F  F  F  F  F  F  F  F  F
2  F  F  F  F  F  F  F  F  F  F      1  F  F  F  F  F  F  F  F  F  F
3  F  F  F  F  T  T  F  F  F  F      2  F  F  F  F  F  F  F  F  F  F
4  F  F  F  T  T  T  T  F  F  F      3  F  F  F  F  T  T  F  F  F  F
5  F  F  F  T  T  T  T  F  F  F      4  F  F  F  T  T  T  T  F  F  F
6  F  F  F  F  T  T  F  F  F  F      5  F  F  F  T  T  T  T  F  F  F
7  F  F  F  F  F  F  F  F  F  F      6  F  F  F  F  T  T  F  F  F  F
8  F  F  F  F  F  F  F  F  F  F      7  F  F  F  F  F  F  F  F  F  F
9  F  F  F  F  F  F  F  F  F  F      8  F  F  F  F  F  F  F  F  F  F
```

### Étape 3 : Détecter les bords supérieurs

```python
top_edge = form_mask[1:, :] & ~top
```

Pour chaque position, on demande :
- **Est-ce que la cellule actuelle fait partie de la forme ?** (`form_mask[1:, :]`)
- **ET son voisin du haut NE fait PAS partie de la forme ?** (`~top`)

```
top_edge (les pixels qui ont un bord supérieur)
   0  1  2  3  4  5  6  7  8  9
1  F  F  F  F  F  F  F  F  F  F
2  F  F  F  F  F  F  F  F  F  F
3  F  F  F  F  T  T  F  F  F  F  ← (3,4) et (3,5) ont un 0 au-dessus
4  F  F  F  T  F  F  F  F  F  F  ← (4,3) a un 0 au-dessus
5  F  F  F  F  F  F  F  F  F  F
6  F  F  F  F  F  F  F  F  F  F
7  F  F  F  F  F  F  F  F  F  F
8  F  F  F  F  F  F  F  F  F  F
9  F  F  F  F  F  F  F  F  F  F

np.sum(top_edge) = 3
```

### Étape 4 : Détecter tous les bords

De manière similaire, on détecte :
- `bottom_edge` : pixels avec un 0 en bas
- `left_edge` : pixels avec un 0 à gauche
- `right_edge` : pixels avec un 0 à droite

```
Visualisation des bords détectés:

    0  1  2  3  4  5  6  7  8  9
0   .  .  .  .  .  .  .  .  .  .
1   .  .  .  .  .  .  .  .  .  .
2   .  .  .  .  .  .  .  .  .  .
3   .  .  .  .  ▀  ▀  .  .  .  .  ← Bords supérieurs
4   .  .  .  ◄  █  █  █  ►  .  .  ← Bords gauches et droits
5   .  .  .  ◄  █  █  █  ►  .  .  ← Bords gauches et droits
6   .  .  .  .  ▄  ▄  .  .  .  .  ← Bords inférieurs
7   .  .  .  .  .  .  .  .  .  .
```

### Étape 5 : Détecter les coins

Les coins sont les pixels qui ont un bord dans DEUX directions :

```python
top_left_corner = form_mask[1:, 1:] & ~top[:, 1:] & ~left[1:, :]
```

Pour la position (3,4) :
- Elle fait partie de la forme : ✓
- Son voisin du haut (2,4) est à 0 : ✓
- Son voisin de gauche (3,3) est à 0 : ✓
→ C'est un coin supérieur-gauche !

```
Coins détectés:

    0  1  2  3  4  5  6  7  8  9
3   .  .  .  .  ╔  ╗  .  .  .  .  ← Coins supérieurs
4   .  .  .  ╔  •  •  •  ╗  .  .
5   .  .  .  ╚  •  •  •  ╝  .  .
6   .  .  .  .  ╚  ╝  .  .  .  .  ← Coins inférieurs
```

### Étape 6 : Calculer le périmètre final

```python
perimeter = (sum(bords) - sum(coins))
          = (top_edge + bottom_edge + left_edge + right_edge) - (tous les coins)
```

Pour notre forme en losange :
- Bords supérieurs : 3
- Bords inférieurs : 3
- Bords gauches : 4
- Bords droits : 4
- **Total brut** : 14

- Coins : 4 (un à chaque angle du losange)
- **Périmètre final** : 14 - 4 = **10**

### Vérification manuelle

Comptons le périmètre en suivant le contour :

```
   0  1  2  3  4  5  6  7  8  9
3  .  .  .  .  █  █  .  .  .  .    Haut: 2 segments
4  .  .  .  █  █  █  █  .  .  .    Côtés: 2 + 2 = 4 segments
5  .  .  .  █  █  █  █  .  .  .    Côtés: 2 + 2 = 4 segments
6  .  .  .  .  █  █  .  .  .  .    Bas: 2 segments

Contour externe:
- Haut ligne 3: 2 pixels
- Descente droite: 1 pixel (ligne 3→4)
- Droite ligne 4-5: 2 pixels
- Descente droite: 1 pixel (ligne 5→6)
- Bas ligne 6: 2 pixels
- Montée gauche: 1 pixel (ligne 6→5)
- Gauche ligne 5-4: 2 pixels
- Montée gauche: 1 pixel (ligne 4→3)

Total: 2+1+2+1+2+1+2+1 = 12 segments

Mais en comptant les pixels de bord (pas les segments), on a 10 pixels de bord.
```

---

## Comparaison Game of Life vs Périmètre

### Game of Life (8 voisins)

```python
# On compte TOUS les 8 voisins
neighbours = sum(world[x-1][y-1:y+2]) \    # 3 voisins (ligne du haut)
           + sum(world[x][y-1:y+2:2]) \     # 2 voisins (gauche et droite)
           + sum(world[x+1][y-1:y+2])       # 3 voisins (ligne du bas)
# Total: 8 voisins
```

### Périmètre (4 voisins cardinaux)

```python
# On ne considère que les 4 voisins cardinaux (haut, bas, gauche, droite)
top = form_mask[:-1, :]      # Voisin du haut
bottom = form_mask[1:, :]    # Voisin du bas
left = form_mask[:, :-1]     # Voisin de gauche
right = form_mask[:, 1:]     # Voisin de droite
# Total: 4 voisins (pas de diagonales)
```

### Pourquoi cette différence ?

- **Game of Life** : Les diagonales comptent pour la reproduction/survie
- **Périmètre** : Seuls les contacts directs (haut/bas/gauche/droite) définissent le contour

---

## Résumé des concepts clés

### 1. Slicing pour décalage
```python
image[:-1, :]  # Décalage vers le haut (retire dernière ligne)
image[1:, :]   # Décalage vers le bas (retire première ligne)
image[:, :-1]  # Décalage vers la gauche (retire dernière colonne)
image[:, 1:]   # Décalage vers la droite (retire première colonne)
```

### 2. Opérations logiques
```python
form_mask & ~neighbor  # pixel à 1 ET voisin à 0 = BORD
```

### 3. Double comptage
```python
# Les coins sont détectés dans deux directions
# Il faut les soustraire pour éviter le double comptage
perimeter = edges - corners
```

### 4. Vectorisation NumPy
```python
# Au lieu de boucles imbriquées:
for x in range(width):
    for y in range(height):
        if pixel[x,y] and not neighbor[x,y]:
            perimeter += 1

# On utilise des opérations sur toute la matrice:
edges = form_mask & ~neighbor
perimeter = np.sum(edges)
```

---

## Exercice pratique

Essayez de calculer le périmètre de cette forme :

```
image = [[0,0,0,0,0],
         [0,1,1,1,0],
         [0,1,0,1,0],
         [0,1,1,1,0],
         [0,0,0,0,0]]
```

**Question** : Quel est le périmètre ?

<details>
<summary>Solution</summary>

Périmètre externe : 12
Périmètre interne (trou) : 4
**Périmètre total : 16**

Le trou au centre ajoute aussi un périmètre !
</details>

---

## Conclusion

Les concepts de voisinage sont fondamentaux en traitement d'image :
- **8 voisins** : Pour la connectivité complète (Game of Life, détection de composantes)
- **4 voisins** : Pour les contours et périmètres (plus restrictif)
- **Slicing NumPy** : Permet d'accéder à tous les voisins simultanément, sans boucles
- **Opérations vectorisées** : Performance optimale pour grandes images

Ces techniques sont utilisées dans :
- Jeu de la vie (Game of Life)
- Détection de contours
- Segmentation d'images
- Morphologie mathématique
- Vision par ordinateur
