# Aide-mémoire : Voisins et Périmètre NumPy

## 🎯 Résumé ultra-rapide

### Les 8 voisins (Game of Life)
```python
neighbours = sum(world[x-1][y-1:y+2]) \     # 3 voisins (haut)
           + sum(world[x][y-1:y+2:2]) \     # 2 voisins (gauche/droite)
           + sum(world[x+1][y-1:y+2])       # 3 voisins (bas)
```

### Périmètre (4 voisins cardinaux)
```python
form_mask = image != 0
top_edge = form_mask[1:, :] & ~form_mask[:-1, :]
# Répéter pour bottom, left, right
# Soustraire les coins pour éviter le double comptage
```

---

## 📊 Tableau des 8 voisins

```
┌─────────┬─────────┬─────────┐
│ (-1,-1) │  (0,-1) │ (+1,-1) │
│   NW    │    N    │   NE    │
├─────────┼─────────┼─────────┤
│ (-1, 0) │  (X,Y)  │ (+1, 0) │
│    W    │ CENTRE  │    E    │
├─────────┼─────────┼─────────┤
│ (-1,+1) │  (0,+1) │ (+1,+1) │
│   SW    │    S    │   SE    │
└─────────┴─────────┴─────────┘
```

---

## 🔧 Slicing pour décalage

| Opération | Effet | Nouvelle dimension |
|-----------|-------|-------------------|
| `image[:-1, :]` | Retire dernière ligne → HAUT | (n-1, m) |
| `image[1:, :]` | Retire première ligne → BAS | (n-1, m) |
| `image[:, :-1]` | Retire dernière colonne → GAUCHE | (n, m-1) |
| `image[:, 1:]` | Retire première colonne → DROITE | (n, m-1) |

**⚠️ Important :** Les dimensions changent ! Une matrice (10,10) devient (9,10) ou (10,9).

---

## 🎮 Game of Life - Règles rapides

| État actuel | Voisins vivants | Résultat |
|-------------|-----------------|----------|
| Morte (0) | 3 | Naissance → 1 |
| Morte (0) | Autre | Reste 0 |
| Vivante (1) | 2 ou 3 | Survie → 1 |
| Vivante (1) | < 2 | Meurt → 0 |
| Vivante (1) | > 3 | Meurt → 0 |

### LUT (Look-Up Table)
```python
dead_rule  = (0, 0, 0, 1, 0, 0, 0, 0, 0)  # Naissance avec 3 voisins
alive_rule = (0, 0, 1, 1, 0, 0, 0, 0, 0)  # Survie avec 2 ou 3 voisins
rules = (dead_rule, alive_rule)
new_value = rules[current_cell][num_neighbors]
```

---

## 📏 Périmètre - Algorithme complet

```python
def perimeter(image):
    # 1. Masque de la forme
    form_mask = image != 0
    
    # 2. Voisins (4 directions)
    top = form_mask[:-1, :]
    bottom = form_mask[1:, :]
    left = form_mask[:, :-1]
    right = form_mask[:, 1:]
    
    # 3. Bords (pixel à 1 ET voisin à 0)
    top_edge = form_mask[1:, :] & ~top
    bottom_edge = form_mask[:-1, :] & ~bottom
    left_edge = form_mask[:, 1:] & ~left
    right_edge = form_mask[:, :-1] & ~right
    
    # 4. Coins (bord dans 2 directions)
    tl = form_mask[1:, 1:] & ~top[:, 1:] & ~left[1:, :]
    tr = form_mask[1:, :-1] & ~top[:, :-1] & ~right[1:, :]
    bl = form_mask[:-1, 1:] & ~bottom[:, 1:] & ~left[:-1, :]
    br = form_mask[:-1, :-1] & ~bottom[:, :-1] & ~right[:-1, :]
    
    # 5. Périmètre = Bords - Coins
    edges = np.sum(top_edge) + np.sum(bottom_edge) + \
            np.sum(left_edge) + np.sum(right_edge)
    corners = np.sum(tl) + np.sum(tr) + np.sum(bl) + np.sum(br)
    
    return edges - corners
```

### Pourquoi soustraire les coins ?
Les coins sont comptés **2 fois** (une fois horizontalement, une fois verticalement).

```
Exemple de coin:
  0  0  0
  0  █  █  ← Pixel (1,1) détecté comme:
  0  █  █     • Bord supérieur (haut = 0)
              • Bord gauche (gauche = 0)
              → Compté 2 fois !
```

---

## ⚡ Opérateurs logiques NumPy

| Opérateur | Symbole | Description |
|-----------|---------|-------------|
| AND | `&` | Vrai si les deux sont vrais |
| OR | `\|` | Vrai si au moins un est vrai |
| NOT | `~` | Inverse |
| XOR | `^` | Vrai si exactement un est vrai |

**⚠️ Ne PAS utiliser `and`, `or`, `not` avec NumPy !**

### Exemples d'utilisation
```python
# Détection de bord
edge = form_mask & ~neighbor  # Pixel à 1 ET voisin à 0

# Détection de coin
corner = form_mask & ~top & ~left  # Pixel à 1 ET haut à 0 ET gauche à 0

# Union de deux masques
combined = mask1 | mask2

# Inversion
inverted = ~mask
```

---

## 📐 Exemple complet étape par étape

```python
import numpy as np

# Image exemple (losange)
image = np.array([[0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,1,1,0,0,0,0],
                  [0,0,0,1,1,1,1,0,0,0],
                  [0,0,0,1,1,1,1,0,0,0],
                  [0,0,0,0,1,1,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0]])

# Visualisation
"""
   0  1  2  3  4  5  6  7  8  9
3  .  .  .  .  █  █  .  .  .  .
4  .  .  .  █  █  █  █  .  .  .
5  .  .  .  █  █  █  █  .  .  .
6  .  .  .  .  █  █  .  .  .  .
"""

# Calcul
form_mask = image != 0
print(f"Pixels dans la forme: {np.sum(form_mask)}")  # 12

# Bords
top = form_mask[:-1, :]
top_edge = form_mask[1:, :] & ~top
print(f"Bords supérieurs: {np.sum(top_edge)}")  # 4

# Répéter pour les 4 directions → Total: 16 bords

# Coins
tl = form_mask[1:, 1:] & ~top[:, 1:] & ~form_mask[:, :-1][1:, :]
print(f"Coins supérieurs-gauches: {np.sum(tl)}")  # 2

# Répéter pour les 4 coins → Total: 8 coins

# Périmètre final
perimetre = 16 - 8  # = 8
print(f"Périmètre: {perimetre}")
```

---

## 🔍 Différences clés

### Game of Life vs Périmètre

| Aspect | Game of Life | Périmètre |
|--------|-------------|-----------|
| Voisins | 8 (avec diagonales) | 4 (cardinaux seulement) |
| But | Compter voisins vivants | Trouver contour |
| Opération | Somme `sum()` | Logique `&`, `~` |
| Résultat | Nombre 0-8 | Longueur contour |

---

## 💡 Astuces et pièges

### ✅ Bonnes pratiques
```python
# Utiliser des noms descriptifs
form_mask = image != 0  # Clair
neighbor_top = form_mask[:-1, :]  # Explicite

# Vectoriser (pas de boucles)
edges = form_mask & ~neighbor  # ✅ Rapide
```

### ❌ Erreurs courantes
```python
# Ne PAS utiliser and/or/not avec NumPy
if mask and neighbor:  # ❌ ERREUR !
if mask & neighbor:    # ✅ Correct

# Ne PAS oublier les dimensions
# form_mask: (10, 10)
# top: (9, 10)
# Toujours comparer des dimensions compatibles !
```

### 🎯 Vérification rapide
```python
# Pour déboguer
print(f"Dimensions: {image.shape}")
print(f"Nombre de pixels: {np.sum(image != 0)}")
print(f"Min/Max: {np.min(image)}, {np.max(image)}")
```

---

## 🚀 Performance

### Sans NumPy (boucles)
```python
# Lent : O(n²)
count = 0
for i in range(height):
    for j in range(width):
        if image[i,j] == 1:
            count += 1
```

### Avec NumPy (vectorisé)
```python
# Rapide : O(n) optimisé en C
count = np.sum(image == 1)  # 100x-1000x plus rapide !
```

### Gain de performance
- **Petit tableau** (100×100) : 10-50x plus rapide
- **Grand tableau** (1000×1000) : 100-1000x plus rapide
- **Très grand** (10000×10000) : Jusqu'à 10000x plus rapide

---

## 📚 Fonctions NumPy utiles

```python
# Création
np.zeros((h, w))          # Matrice de zéros
np.ones((h, w))           # Matrice de uns
np.full((h, w), value)    # Matrice remplie de 'value'
np.arange(start, stop, step)  # Séquence

# Opérations
np.sum(array)             # Somme totale
np.count_nonzero(array)   # Compte les non-zéros
np.where(condition)       # Indices où condition = True
np.logical_or(a, b)       # OU logique
np.logical_and(a, b)      # ET logique
np.logical_not(a)         # NON logique

# Grilles
np.meshgrid(x, y)         # Créer grille de coordonnées

# Info
array.shape               # Dimensions
array.dtype               # Type de données
array.size                # Nombre total d'éléments
```

---

## 🎓 Applications réelles

1. **Game of Life** : Automates cellulaires, simulations
2. **Vision par ordinateur** : Détection de contours, segmentation
3. **Imagerie médicale** : Analyse de tumeurs, organes
4. **Géomatique** : Analyse d'images satellitaires
5. **Robotique** : Navigation, détection d'obstacles
6. **Morphologie** : Érosion, dilatation, squelettisation

---

## 📝 Checklist de débogage

Quand ça ne marche pas :

- [ ] Vérifier les dimensions avec `.shape`
- [ ] Afficher un petit échantillon de la matrice
- [ ] Vérifier le type de données `.dtype`
- [ ] Utiliser `&` et non `and`
- [ ] S'assurer que les slices ont la bonne taille
- [ ] Visualiser avec `print()` ou matplotlib
- [ ] Tester sur un petit exemple simple d'abord

---

## 🔗 Ressources

- Documentation NumPy : https://numpy.org/doc/
- Tutoriel slicing : https://numpy.org/doc/stable/user/basics.indexing.html
- Opérations booléennes : https://numpy.org/doc/stable/reference/routines.logic.html

---

**💾 Enregistrez cet aide-mémoire et gardez-le à portée de main !**

*Créé pour le cours C52 - Python & NumPy - 2025*
