import numpy as np

# Image de démonstration (votre exemple)
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

def print_separator(title=""):
    """Affiche un séparateur avec titre"""
    print("\n" + "="*70)
    if title:
        print(f"  {title}")
        print("="*70)

def print_matrix(matrix, title="", true_char='█', false_char='.'):
    """Affiche une matrice booléenne ou numérique de façon lisible"""
    print(f"\n{title}")
    print("   ", end="")
    for col in range(matrix.shape[1]):
        print(f"{col:2}", end=" ")
    print()
    
    for row in range(matrix.shape[0]):
        print(f"{row:2} ", end=" ")
        for col in range(matrix.shape[1]):
            if isinstance(matrix[row, col], (bool, np.bool_)):
                char = true_char if matrix[row, col] else false_char
            else:
                char = str(int(matrix[row, col]))
            print(f" {char} ", end="")
        print()

def compare_matrices(mat1, mat2, title1="Matrice 1", title2="Matrice 2"):
    """Compare deux matrices côte à côte"""
    print(f"\n{title1:^35} | {title2:^35}")
    print("-"*35 + "+" + "-"*35)
    
    # En-têtes de colonnes
    header = "   " + "".join([f"{i:3}" for i in range(mat1.shape[1])])
    print(f"{header} | {header}")
    
    for row in range(mat1.shape[0]):
        # Matrice 1
        line1 = f"{row:2} "
        for col in range(mat1.shape[1]):
            if isinstance(mat1[row, col], (bool, np.bool_)):
                char = '█' if mat1[row, col] else '.'
            else:
                char = str(int(mat1[row, col]))
            line1 += f" {char} "
        
        # Matrice 2 (si elle existe et a la bonne taille)
        if mat2.shape[0] > row:
            line2 = f"{row:2} "
            for col in range(mat2.shape[1]):
                if isinstance(mat2[row, col], (bool, np.bool_)):
                    char = '█' if mat2[row, col] else '.'
                else:
                    char = str(int(mat2[row, col]))
                line2 += f" {char} "
        else:
            line2 = ""
        
        print(f"{line1} | {line2}")

def calculate_perimeter_detailed(image):
    """Calcule le périmètre avec affichage détaillé de chaque étape"""
    
    print_separator("CALCUL DU PÉRIMÈTRE - DÉMONSTRATION DÉTAILLÉE")
    
    # Afficher l'image originale
    print_matrix(image, "Image originale (votre forme):", '█', '.')
    
    # Étape 1: Créer le masque de la forme
    print_separator("ÉTAPE 1: Créer le masque booléen de la forme")
    form_mask = image != 0
    print_matrix(form_mask, "form_mask = image != 0", '█', '.')
    print(f"\nDimensions: {form_mask.shape}")
    print(f"Nombre de pixels dans la forme: {np.sum(form_mask)}")
    
    # Étape 2: Créer les vues décalées
    print_separator("ÉTAPE 2: Créer les vues décalées (voisins)")
    
    print("\n>>> top = form_mask[:-1, :]  (retire la dernière ligne)")
    print("    Représente le voisin DU HAUT de chaque pixel")
    top = form_mask[:-1, :]
    print(f"    Dimensions: {top.shape} (on perd 1 ligne)")
    
    print("\n>>> bottom = form_mask[1:, :]  (retire la première ligne)")
    print("    Représente le voisin DU BAS de chaque pixel")
    bottom = form_mask[1:, :]
    print(f"    Dimensions: {bottom.shape} (on perd 1 ligne)")
    
    print("\n>>> left = form_mask[:, :-1]  (retire la dernière colonne)")
    print("    Représente le voisin DE GAUCHE de chaque pixel")
    left = form_mask[:, :-1]
    print(f"    Dimensions: {left.shape} (on perd 1 colonne)")
    
    print("\n>>> right = form_mask[:, 1:]  (retire la première colonne)")
    print("    Représente le voisin DE DROITE de chaque pixel")
    right = form_mask[:, 1:]
    print(f"    Dimensions: {right.shape} (on perd 1 colonne)")
    
    # Visualiser les décalages
    print_separator("VISUALISATION DES DÉCALAGES")
    print("\nComparaison: Pixels actuels VS leurs voisins du HAUT")
    compare_matrices(form_mask[1:, :], top, 
                    "form_mask[1:, :] (lignes 1-9)", 
                    "top = form_mask[:-1, :] (lignes 0-8)")
    
    # Étape 3: Détecter les bords
    print_separator("ÉTAPE 3: Détecter les bords")
    
    print("\n>>> top_edge = form_mask[1:, :] & ~top")
    print("    Détecte les pixels qui ont un 0 AU-DESSUS")
    print("    & = AND logique")
    print("    ~ = NOT logique (inverse)")
    top_edge = form_mask[1:, :] & ~top
    print_matrix(top_edge, "Pixels avec bord supérieur:", '▲', '.')
    print(f"Nombre de bords supérieurs: {np.sum(top_edge)}")
    
    print("\n>>> bottom_edge = form_mask[:-1, :] & ~bottom")
    print("    Détecte les pixels qui ont un 0 EN-DESSOUS")
    bottom_edge = form_mask[:-1, :] & ~bottom
    print_matrix(bottom_edge, "Pixels avec bord inférieur:", '▼', '.')
    print(f"Nombre de bords inférieurs: {np.sum(bottom_edge)}")
    
    print("\n>>> left_edge = form_mask[:, 1:] & ~left")
    print("    Détecte les pixels qui ont un 0 À GAUCHE")
    left_edge = form_mask[:, 1:] & ~left
    print_matrix(left_edge, "Pixels avec bord gauche:", '◄', '.')
    print(f"Nombre de bords gauches: {np.sum(left_edge)}")
    
    print("\n>>> right_edge = form_mask[:, :-1] & ~right")
    print("    Détecte les pixels qui ont un 0 À DROITE")
    right_edge = form_mask[:, :-1] & ~right
    print_matrix(right_edge, "Pixels avec bord droit:", '►', '.')
    print(f"Nombre de bords droits: {np.sum(right_edge)}")
    
    # Somme des bords
    total_edges = (np.sum(top_edge) + np.sum(bottom_edge) + 
                   np.sum(left_edge) + np.sum(right_edge))
    print(f"\n>>> TOTAL des bords: {np.sum(top_edge)} + {np.sum(bottom_edge)} + "
          f"{np.sum(left_edge)} + {np.sum(right_edge)} = {total_edges}")
    
    # Étape 4: Détecter les coins
    print_separator("ÉTAPE 4: Détecter les coins (pour éviter le double comptage)")
    
    print("\nUn COIN est un pixel qui a un bord dans DEUX directions.")
    print("Les coins sont comptés 2 fois, il faut les soustraire!")
    
    print("\n>>> top_left_corner = form_mask[1:, 1:] & ~top[:, 1:] & ~left[1:, :]")
    print("    Pixel avec 0 EN HAUT ET 0 À GAUCHE")
    top_left_corner = form_mask[1:, 1:] & ~top[:, 1:] & ~left[1:, :]
    print_matrix(top_left_corner, "Coins supérieurs gauches:", '╔', '.')
    print(f"Nombre: {np.sum(top_left_corner)}")
    
    print("\n>>> top_right_corner = form_mask[1:, :-1] & ~top[:, :-1] & ~right[1:, :]")
    print("    Pixel avec 0 EN HAUT ET 0 À DROITE")
    top_right_corner = form_mask[1:, :-1] & ~top[:, :-1] & ~right[1:, :]
    print_matrix(top_right_corner, "Coins supérieurs droits:", '╗', '.')
    print(f"Nombre: {np.sum(top_right_corner)}")
    
    print("\n>>> bottom_left_corner = form_mask[:-1, 1:] & ~bottom[:, 1:] & ~left[:-1, :]")
    print("    Pixel avec 0 EN BAS ET 0 À GAUCHE")
    bottom_left_corner = form_mask[:-1, 1:] & ~bottom[:, 1:] & ~left[:-1, :]
    print_matrix(bottom_left_corner, "Coins inférieurs gauches:", '╚', '.')
    print(f"Nombre: {np.sum(bottom_left_corner)}")
    
    print("\n>>> bottom_right_corner = form_mask[:-1, :-1] & ~bottom[:, :-1] & ~right[:-1, :]")
    print("    Pixel avec 0 EN BAS ET 0 À DROITE")
    bottom_right_corner = form_mask[:-1, :-1] & ~bottom[:, :-1] & ~right[:-1, :]
    print_matrix(bottom_right_corner, "Coins inférieurs droits:", '╝', '.')
    print(f"Nombre: {np.sum(bottom_right_corner)}")
    
    total_corners = (np.sum(top_left_corner) + np.sum(top_right_corner) + 
                     np.sum(bottom_left_corner) + np.sum(bottom_right_corner))
    print(f"\n>>> TOTAL des coins: {np.sum(top_left_corner)} + {np.sum(top_right_corner)} + "
          f"{np.sum(bottom_left_corner)} + {np.sum(bottom_right_corner)} = {total_corners}")
    
    # Étape 5: Calculer le périmètre final
    print_separator("ÉTAPE 5: Calcul du périmètre final")
    
    perimeter = total_edges - total_corners
    
    print(f"\nFormule: PÉRIMÈTRE = TOTAL_BORDS - TOTAL_COINS")
    print(f"         PÉRIMÈTRE = {total_edges} - {total_corners}")
    print(f"         PÉRIMÈTRE = {perimeter}")
    
    # Visualisation finale
    print_separator("VISUALISATION FINALE DU CONTOUR")
    
    # Créer une matrice de visualisation
    visual = np.zeros_like(image, dtype=str)
    visual[:] = '.'
    
    # Marquer la forme
    visual[image == 1] = '█'
    
    # Marquer les bords (avec alignement des dimensions)
    # Note: on doit faire attention aux dimensions réduites
    for i in range(1, image.shape[0]):
        for j in range(image.shape[1]):
            if top_edge[i-1, j]:
                visual[i, j] = '▲'
    
    for i in range(image.shape[0]-1):
        for j in range(image.shape[1]):
            if bottom_edge[i, j]:
                visual[i, j] = '▼'
    
    for i in range(image.shape[0]):
        for j in range(1, image.shape[1]):
            if left_edge[i, j-1]:
                visual[i, j] = '◄'
    
    for i in range(image.shape[0]):
        for j in range(image.shape[1]-1):
            if right_edge[i, j]:
                visual[i, j] = '►'
    
    # Marquer les coins (priorité sur les bords)
    for i in range(1, image.shape[0]):
        for j in range(1, image.shape[1]):
            if top_left_corner[i-1, j-1]:
                visual[i, j] = '╔'
    
    for i in range(1, image.shape[0]):
        for j in range(image.shape[1]-1):
            if top_right_corner[i-1, j]:
                visual[i, j] = '╗'
    
    for i in range(image.shape[0]-1):
        for j in range(1, image.shape[1]):
            if bottom_left_corner[i, j-1]:
                visual[i, j] = '╚'
    
    for i in range(image.shape[0]-1):
        for j in range(image.shape[1]-1):
            if bottom_right_corner[i, j]:
                visual[i, j] = '╝'
    
    print("\nLégende:")
    print("  █ = Intérieur de la forme")
    print("  ▲ = Bord supérieur")
    print("  ▼ = Bord inférieur")
    print("  ◄ = Bord gauche")
    print("  ► = Bord droit")
    print("  ╔╗╚╝ = Coins")
    print("  . = Fond (0)")
    
    print("\nContour de la forme:")
    print("   ", end="")
    for col in range(visual.shape[1]):
        print(f"{col:2}", end=" ")
    print()
    
    for row in range(visual.shape[0]):
        print(f"{row:2} ", end=" ")
        for col in range(visual.shape[1]):
            print(f" {visual[row, col]} ", end="")
        print()
    
    return perimeter


def demo_game_of_life_neighbors():
    """Démontre le calcul des 8 voisins pour Game of Life"""
    print_separator("GAME OF LIFE - CALCUL DES 8 VOISINS")
    
    # Petite grille pour la démo
    world = np.array([[0,0,0,0,0],
                      [0,0,1,0,0],
                      [0,1,1,1,0],
                      [0,0,1,0,0],
                      [0,0,0,0,0]])
    
    print_matrix(world, "Grille Game of Life (croix):", '●', '·')
    
    # Calculer les voisins de la cellule centrale (2,2)
    x, y = 2, 2
    
    print(f"\nCalculons les voisins de la cellule ({x},{y})")
    print("\nMéthode avec slicing Python:")
    print(f">>> neighbours = sum(world[{x-1}][{y-1}:{y+2}]) \\")
    print(f"               + sum(world[{x}][{y-1}:{y+2}:2]) \\")
    print(f"               + sum(world[{x+1}][{y-1}:{y+2}])")
    
    # Détail du calcul
    print("\nDétail du calcul:")
    
    print(f"\n1. Ligne du HAUT (x-1 = {x-1}):")
    print(f"   world[{x-1}][{y-1}:{y+2}] = world[{x-1}][{y-1}:{y+2}]")
    print(f"   = [{world[x-1][y-1]}, {world[x-1][y]}, {world[x-1][y+1]}]")
    line_top = sum(world[x-1][y-1:y+2])
    print(f"   sum = {line_top}")
    
    print(f"\n2. Ligne du MILIEU (x = {x}):")
    print(f"   world[{x}][{y-1}:{y+2}:2] = world[{x}][{y-1}:{y+2}:2]")
    print(f"   = [{world[x][y-1]}, {world[x][y+1]}]  (step=2, saute le centre)")
    line_mid = sum(world[x][y-1:y+2:2])
    print(f"   sum = {line_mid}")
    
    print(f"\n3. Ligne du BAS (x+1 = {x+1}):")
    print(f"   world[{x+1}][{y-1}:{y+2}] = world[{x+1}][{y-1}:{y+2}]")
    print(f"   = [{world[x+1][y-1]}, {world[x+1][y]}, {world[x+1][y+1]}]")
    line_bot = sum(world[x+1][y-1:y+2])
    print(f"   sum = {line_bot}")
    
    total_neighbors = line_top + line_mid + line_bot
    print(f"\n>>> TOTAL: {line_top} + {line_mid} + {line_bot} = {total_neighbors} voisins vivants")
    
    # Visualisation des voisins
    print("\nVisualisation des 8 voisins:")
    print(f"   {y-1}  {y} {y+1}")
    print(f"{x-1}  {world[x-1][y-1]}  {world[x-1][y]}  {world[x-1][y+1]}")
    print(f"{x}   {world[x][y-1]}  X  {world[x][y+1]}")
    print(f"{x+1}  {world[x+1][y-1]}  {world[x+1][y]}  {world[x+1][y+1]}")
    
    # Règles du jeu
    print("\n" + "="*70)
    print("RÈGLES DE GAME OF LIFE")
    print("="*70)
    
    print("\nCellule MORTE (0):")
    print("  - Exactement 3 voisins vivants → Naissance (devient 1)")
    print("  - Sinon → Reste morte (0)")
    
    print("\nCellule VIVANTE (1):")
    print("  - 2 ou 3 voisins vivants → Survie (reste 1)")
    print("  - Moins de 2 voisins → Meurt de solitude (devient 0)")
    print("  - Plus de 3 voisins → Meurt de surpopulation (devient 0)")
    
    print(f"\nPour notre cellule ({x},{y}) avec {total_neighbors} voisins:")
    if world[x][y] == 1:
        if total_neighbors == 2 or total_neighbors == 3:
            print(f"  → Cellule vivante avec {total_neighbors} voisins → SURVIT")
        else:
            print(f"  → Cellule vivante avec {total_neighbors} voisins → MEURT")
    else:
        if total_neighbors == 3:
            print(f"  → Cellule morte avec {total_neighbors} voisins → NAISSANCE")
        else:
            print(f"  → Cellule morte avec {total_neighbors} voisins → RESTE MORTE")


# Exécution de la démonstration
if __name__ == "__main__":
    print("\n" + "█"*70)
    print("█" + " "*68 + "█")
    print("█" + " "*18 + "DÉMONSTRATION COMPLÈTE" + " "*28 + "█")
    print("█" + " "*10 + "Voisins et Périmètre avec NumPy" + " "*27 + "█")
    print("█" + " "*68 + "█")
    print("█"*70)
    
    # Partie 1: Calcul du périmètre
    perimeter = calculate_perimeter_detailed(image)
    
    print("\n" + "█"*70)
    print(f"█  RÉSULTAT FINAL: Le périmètre de la forme est {perimeter}" + " "*(70-48-len(str(perimeter))) + "█")
    print("█"*70)
    
    # Partie 2: Game of Life
    print("\n" * 3)
    demo_game_of_life_neighbors()
    
    print("\n" + "█"*70)
    print("█" + " "*68 + "█")
    print("█" + " "*22 + "FIN DE LA DÉMONSTRATION" + " "*23 + "█")
    print("█" + " "*68 + "█")
    print("█"*70 + "\n")
