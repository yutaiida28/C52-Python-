# Exercice 2.2 :
# Objectif : Manipuler une collection pour créer des statistiques.
# Vous devez créer deux dictionnaire qui compte :
# le nombre d'individus pour chacun des genres : gender_count
# pour chaque ville, le nombre d'individus et l'âge moyen : city_stat
# Vous devez afficher les résultats sous la forme :
# Genres :
# femme : 11
# homme : 9
# autre : 4
# Villes :
# Montréal : 6 individus avec un âge moyen de 35 ans
# Québec : 5 individus avec un âge moyen de 40 ans
# ...
# Vous devez utiliser la collection data suivante :
# data = [
#     ("Tremblay, Marc", 41, "Montréal", 'h'),
#     ("Lévesque, Annie", 30, "Gatineau", 'f'),
#     ("Beaulieu, Denis", 58, "Longueuil", 'h'),
#     ("Aubin, Christine", 41, "Saguenay", 'f'),
#     ("Gauthier, Julie", 33, "Québec", 'f'),
#     ("Boucher, Geneviève", 37, "Sherbrooke", 'f'),
#     ("Bergeron, Mathieu", 36, "Gatineau", 'h'),
#     ("Poirier, Daniel", 63, "Saguenay", 'h'),
#     ("Gagnon, Laure", 27, "Montréal", 'f'),
#     ("Morin, Philippe", 54, "Québec", 'h'),
#     ("Caron, Zoé", 21, "Gatineau", 'x'),
#     ("Bélanger, Thomas", 42, "Laval", 'h'),
#     ("Pelletier, Maude", 24, "Laval", 'f'),
#     ("Langlois, Patrick", 50, "Sherbrooke", 'h'),
#     ("Simard, Noé", 34, "Longueuil", 'x'),
#     ("Roy, Étienne", 35, "Montréal", 'h'),
#     ("Ouellet, Kevin", 38, "Laval", 'h'),
#     ("Côté, Myriam", 22, "Montréal", 'f'),
#     ("Lavoie, Nadine", 46, "Québec", 'f'),
#     ("Bouchard, Alex", 31, "Montréal", 'x'),
#     ("Fortin, Samuel", 19, "Québec", 'h'),
#     ("Girard, Valérie", 26, "Longueuil", 'f'),
#     ("Gagné, Chantal", 29, "Laval", 'f'),
#     ("Lefebvre, Simon", 18, "Saguenay", 'h'),
#     ("Lapointe, Amélie", 23, "Sherbrooke", 'f'),
#     ("Dufour, Olivier", 40, "Montréal", 'h'),
#     ("Boucher, Camille", 28, "Gatineau", 'f'),
#     ("Lemieux, Alexandre", 39, "Québec", 'h'),
#     ("Desjardins, Élise", 32, "Laval", 'f'),
#     ("Morissette, Vincent", 45, "Longueuil", 'h'),
#     ("Caron, Sarah", 20, "Saguenay", 'f'),
#     ("Bélanger, Maxime", 44, "Sherbrooke", 'h')]

# gender_dict = {'h': 0, 'f': 0,'x': 0}
# ville_state = {}
# for i in data:
#     if i[3] == 'h':
#         gender_dict['h']+=1
#     elif i[3] == 'f':
#         gender_dict['f']+=1
#     else:
#         gender_dict['x']+=1
# for j in data:
#     if j[2] in ville_state:
#         ville_state[j[2]].append(j[1])
#     else:
#         ville_state[j[2]] = [j[1]]
# print(f"homme : {gender_dict["h"]}\nfemme : {gender_dict["f"]}\nautre : {gender_dict["x"]}")
# for k in ville_state:
#     print(f"{k} : {len(ville_state[k])} individus avec un age moyen de {sum(ville_state[k])/len(ville_state[k])} ans")


# Exercice 2.3 :
# Objectif : Validater les parenthèses, crochets et accolades ()[]{}
# Étape 1 : Lire une ligne de texte saisie à la console.
# Étape 2 : Si la ligne est vide, utiliser cette chaîne de caractères par défaut :
# phrase = "Au labo (site {Nord [A-12]}) nous notons que g(x) = (x+{2y[3z]})/(4u-{5v[6w]}) reste stable."
# Étape 3 : Vérifier si les parenthèses, crochets et accolades sont équilibrés.
# Les parenthèses/crochets/accolades ouvrantes doivent être fermées par des parenthèses/crochets/accolades fermantes
# Les parenthèses/crochets/accolades doivent être correctement imbriqués, par exemple (ce n'est pas seulement le nombre qui compte) :
# ([]){} → OK
# ([){]} → ERR
# Vous devez utiliser une pile pour vérifier l'équilibre des parenthèses, crochets et accolades. Pour y arriver, utilisez une liste avec les méthodes append pour ajouter un élément et pop pour retirer le dernier élément ajouté.
# Étape 4 : Affichez l'un de ces messages :
# OK si les parenthèses, crochets et accolades sont équilibrés
# ERR pos = i si une erreur est détectée, où i est la position de la première erreur (0 based index)

# phrase = "Au labo (site {Nord [A-12]}) nous notons que g(x) = (x+{2y[3z]})/(4u-{5v[6w]}) reste stable."
# stack = []

# for position, char in enumerate(phrase):  # enumerate gives you both position and character
#     if char in "([{":
#         stack.append((char, position))
#     elif char in ")]}":
#         last_opening = stack[-1]  # Look at top of stack (last item)
#         if they_match:
#             stack.pop()  # Remove the matched pair
#         else:
        
    
il manque la 2.4 reffaire 2.3
