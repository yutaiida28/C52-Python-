# - Exercice 2.2 : 
#     - Objectif : Manipuler une collection pour créer des statistiques.
#     - Vous devez créer deux dictionnaire qui compte :
#         - le nombre d'individus pour chacun des genres : `gender_count`
#         - pour chaque ville, le nombre d'individus et l'âge moyen : `city_stat`
#     - Vous devez afficher les résultats sous la forme :
#         - Genres :
#             - femme : 11
#             - homme : 9
#             - autre : 4
#         - Villes :
#             - Montréal : 6 individus avec un âge moyen de 35 ans
#             - Québec : 5 individus avec un âge moyen de 40 ans
#             - ...
#     - Vous devez utiliser la collection `data` suivante :

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

gender_count = dict{'h':0,'f':0,'x':0}
for genre in data:
    if 