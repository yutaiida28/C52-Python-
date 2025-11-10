# 📚 Documentation complète : Voisins et Périmètre avec NumPy

Bienvenue ! Cette documentation vous explique en détail comment identifier les 8 voisins d'une cellule et comment calculer le périmètre d'une forme avec NumPy, avec le lien entre Game of Life et le traitement d'images.

---

## 📖 Fichiers disponibles

### 1. 📄 **Voisins_et_Perimetre_NumPy.md**
**Format :** Markdown (texte)  
**Contenu :** Guide complet et détaillé avec :
- Concept des 8 voisins avec schémas ASCII
- Game of Life et calcul des voisins avec slicing
- Slicing avancé pour accéder aux voisins
- Algorithme complet du périmètre expliqué ligne par ligne
- Exemple complet étape par étape avec votre image
- Comparaison Game of Life vs Périmètre

**👉 Parfait pour :** Lecture approfondie, comprendre en détail

---

### 2. 📑 **Voisins_et_Perimetre_Visual.pdf**
**Format :** PDF (8 pages)  
**Contenu :** Guide visuel avec tableaux et code formaté :
- Tableau des 8 voisins
- Règles de Game of Life en tableau
- Slicing avec exemples visuels
- Algorithme du périmètre complet
- Comparaisons et opérateurs logiques
- Exemple pratique complet
- Résumé des concepts clés

**👉 Parfait pour :** Impression, révision rapide, référence visuelle

---

### 3. 📋 **Aide_Memoire_Voisins_Perimetre.md**
**Format :** Markdown (aide-mémoire)  
**Contenu :** Cheat sheet ultra-rapide :
- Résumé en 2 lignes de code
- Tableaux de référence rapide
- Opérateurs logiques
- Exemples minimaux
- Astuces et pièges à éviter
- Checklist de débogage

**👉 Parfait pour :** Référence rapide pendant le codage, examen

---

### 4. 🐍 **demo_voisins_perimetre.py**
**Format :** Script Python exécutable  
**Contenu :** Démonstration interactive complète :
- Calcul du périmètre étape par étape avec votre image
- Affichage visuel de chaque transformation
- Démonstration Game of Life avec 8 voisins
- Explications détaillées pendant l'exécution

**👉 Parfait pour :** Voir en action, comprendre visuellement

**Comment exécuter :**
```bash
python demo_voisins_perimetre.py
```

---

## 🎯 Par où commencer ?

### Si vous voulez COMPRENDRE en profondeur :
1. Lisez **Voisins_et_Perimetre_NumPy.md** 📄
2. Exécutez **demo_voisins_perimetre.py** 🐍
3. Référez-vous à **Aide_Memoire_Voisins_Perimetre.md** 📋 quand vous codez

### Si vous êtes pressé :
1. Ouvrez **Voisins_et_Perimetre_Visual.pdf** 📑
2. Gardez **Aide_Memoire_Voisins_Perimetre.md** 📋 ouvert pendant que vous codez

### Pour réviser avant un examen :
1. **Aide_Memoire_Voisins_Perimetre.md** 📋
2. **Voisins_et_Perimetre_Visual.pdf** 📑 (imprimer les pages importantes)

---

## 💡 Concepts clés expliqués

### 🎮 Les 8 voisins (Game of Life)

Pour une cellule à position (x, y), ses 8 voisins sont :
```
(-1,-1) (0,-1) (+1,-1)    ← NW  N  NE
(-1, 0) (X, Y) (+1, 0)    ← W  •  E
(-1,+1) (0,+1) (+1,+1)    ← SW  S  SE
```

**En code Python (avec slicing) :**
```python
neighbours = sum(world[x-1][y-1:y+2]) \     # 3 voisins (haut)
           + sum(world[x][y-1:y+2:2]) \     # 2 voisins (milieu, saute centre)
           + sum(world[x+1][y-1:y+2])       # 3 voisins (bas)
```

### 📏 Périmètre (4 voisins cardinaux)

Le périmètre compte les pixels de bord (qui touchent le fond).

**Principe :**
1. Créer des "vues décalées" de l'image (slicing)
2. Comparer chaque pixel avec son voisin
3. Détecter les bords : pixel à 1 ET voisin à 0
4. Soustraire les coins (double comptage)

**Formule :**
```
PÉRIMÈTRE = BORDS_TOTAL - COINS_TOTAL
```

---

## ✅ Checklist d'apprentissage

Vous maîtrisez le sujet quand vous pouvez :

- [ ] Identifier les 8 voisins d'une cellule
- [ ] Expliquer le slicing pour le décalage
- [ ] Calculer les voisins dans Game of Life avec slicing
- [ ] Différencier 8 voisins vs 4 voisins cardinaux
- [ ] Détecter les bords avec des opérations logiques
- [ ] Expliquer pourquoi soustraire les coins
- [ ] Implémenter l'algorithme du périmètre complet
- [ ] Utiliser correctement `&`, `|`, `~` avec NumPy

---

**📝 Note :** Pour la documentation complète du cours Python, consultez aussi :
- **Documentation_Python_C52.md**
- **Documentation_Python_C52.pdf**

---

*Documentation créée pour le cours C52 - Python & NumPy - 2025*
