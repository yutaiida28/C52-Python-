<hr>

# Géométrie

Une image binaire est une image pour laquelle chaque pixel est soit 0 ou 1.

## 2) On vous demande de créer toutes les fonctions suivantes sans faire de boucle :
1. Faites une fonction qui crée une image binaire de dimension paramétrable dont tous les pixels sont initialisés à 0. À vous de déterminer le meilleur type pour ce type d'image.
<br>`create_image(size)`
<br>&nbsp;&nbsp;&nbsp;- `size` est un tuple indiquant la taille de l'image : `(largeur, hauteur)`.
<br>&nbsp;&nbsp;&nbsp;- `return` l'image produite de type `np.ndarray`.
1. Faites une fonction qui rempli l'image de la même couleur.
<br>`fill(image, color=1)` 
<br>&nbsp;&nbsp;&nbsp;- `image` est l'image à modifier
<br>&nbsp;&nbsp;&nbsp;- `color` la couleur à remplir : `0` ou `1`
<br>&nbsp;&nbsp;&nbsp;- `return` rien, cette fonction modifie l'image passé en argument (`image`) 
1. Faites une fonction qui réinitialise le contenu de l'image (tous les pixels à `0`).
<br>`clear(image)` 
<br>&nbsp;&nbsp;&nbsp;- `image` est l'image à modifier
<br>&nbsp;&nbsp;&nbsp;- `return` rien, cette fonction modifie l'image passé en argument (`image`) 
1. Faites une fonction qui met tous les pixels de l'image à une couleur aléatoire.
<br>`randomize(image, percent=0.5)` 
<br>&nbsp;&nbsp;&nbsp;- `image` est l'image à modifier
<br>&nbsp;&nbsp;&nbsp;- `percent` est le pourcentage de pixel à `1` : `[0., 1.]`
<br>&nbsp;&nbsp;&nbsp;- `return` rien, cette fonction modifie l'image passé en argument (`image`) 
1. Faites une fonction qui trace un seul point dans l'image.
<br>`draw_point(image, point, color=1)` 
<br>&nbsp;&nbsp;&nbsp;- `image` est l'image à modifier
<br>&nbsp;&nbsp;&nbsp;- `point` un tuple de la coordonnée du point à tracer : `(x, y)`
<br>&nbsp;&nbsp;&nbsp;- `color` la couleur à tracer : `0` ou `1`
<br>&nbsp;&nbsp;&nbsp;- `return` rien, cette fonction modifie l'image passé en argument (`image`) 
<br>_si le point se trouve à l'extérieur de l'image, la fonction est sans effet_
1. Faites une fonction qui trace un rectangle rempli dans l'image. 
<br>`draw_rectangle(image, top_left, bottom_right)` 
<br>&nbsp;&nbsp;&nbsp;- `image` est l'image à modifier
<br>&nbsp;&nbsp;&nbsp;- `top_left` un tuple de la coordonnée supérieure gauche : `(x0, y0)`
<br>&nbsp;&nbsp;&nbsp;- `bottom_right` un tuple de la coordonnée inférieure droite  : `(x1, y1)`
<br>&nbsp;&nbsp;&nbsp;- **attention** `bottom_right` est une frontière exclue
<br>&nbsp;&nbsp;&nbsp;- `return` rien, cette fonction modifie l'image passé en argument (`image`) 
<br>_si le rectangle dépasse l'image tout ou en partie, seulement la partie visible est tracée_
1. Faites une fonction qui met tous les pixels de la bordure à 0.
<br>`reset_border(image)` 
<br>&nbsp;&nbsp;&nbsp;- `image` est l'image à modifier
<br>&nbsp;&nbsp;&nbsp;- `return` rien, cette fonction modifie l'image passé en argument (`image`) 
1. Faites une fonction qui trace un point de la couleur spécifiée à une position aléatoire. La position est n'importe où à l'intérieur de l'image.
<br>`draw_random_point(image, color=1)` 
<br>&nbsp;&nbsp;&nbsp;- `image` est l'image à modifier
<br>&nbsp;&nbsp;&nbsp;- `color` la couleur à tracer : `0` ou `1`
<br>&nbsp;&nbsp;&nbsp;- `return` rien, cette fonction modifie l'image passé en argument (`image`) 
<br>_cette fonction peut dessiner la même couleur sur un pixel, ce qui n'aura aucun effet visible_
1. Faites une fonction qui inverse un point de l'image à une position aléatoire. La position doit être aléatoire parmi les pixels de la couleur donnée.
<br>`inverse_random_point(image, color=0)` 
<br>&nbsp;&nbsp;&nbsp;- `image` est l'image à modifier
<br>&nbsp;&nbsp;&nbsp;- `color` est la couleur à considérer pour l'analyse des positions disponibles : `0` ou `1`
<br>&nbsp;&nbsp;&nbsp;- `return` rien, cette fonction modifie l'image passé en argument (`image`) 
<br>_s'il n'existe aucun pixel de la couleur spécifiée, la fonction est sans effet_
1. Faites une fonction calculant la distance entre 2 points de l'image.
<br>`distance_between_two_points(image)` 
<br>&nbsp;&nbsp;&nbsp;- `image` est l'image à analyser
<br>&nbsp;&nbsp;&nbsp;- `return` un `float` représentant la distance calculée, retourne `None` si l'image ne possède pas strictement deux points
<br>_cette fonction considère que toute l'image est à 0 et que seulement 2 points sont à 1 - ainsi, c'est la distance entre ces deux points qui doit être retournée_
1. Faites une fonction qui trace un cercle rempli dans l'image.
<br>`draw_circle(image, center, radius)` 
<br>&nbsp;&nbsp;&nbsp;- `image` est l'image à modifier
<br>&nbsp;&nbsp;&nbsp;- `center` est une tuple représentant la coordonnée du centre : `(cx, cy)`
<br>&nbsp;&nbsp;&nbsp;- `radius` est le rayon du cercle
<br>&nbsp;&nbsp;&nbsp;- `return` rien, cette fonction modifie l'image passé en argument (`image`) 
<br>_si le cercle dépasse l'image tout ou en partie, seulement la partie visible est tracée_
1. Considérant qu'une seule forme se trouve dans l'image, faites une fonction qui calcule l'aire de la forme.
<br>`area(image)` 
<br>&nbsp;&nbsp;&nbsp;- `image` est l'image à considérer
<br>&nbsp;&nbsp;&nbsp;- `return` un `float` représentant l'aire calculée
<br>$$ area = \sum_{} I_{x,y}, \forall x,y\in shape $$
<br>où :
<br>&nbsp;&nbsp;&nbsp;- $I_{x,y}$ est la valeur de l'image à la coordonnées $x$ et $y$
<br>&nbsp;&nbsp;&nbsp;- $x$ est la coordonnées sur les abscisses
<br>&nbsp;&nbsp;&nbsp;- $y$ est la coordonnées sur les ordonnées
1. Considérant qu'une seule forme se trouve dans l'image, faites une fonction qui calcule le centroïde de la forme.
<br>`centroid(image)` 
<br>&nbsp;&nbsp;&nbsp;- `image` est l'image à considérer
<br>&nbsp;&nbsp;&nbsp;- `return` un `tuple` de deux `float` représentant la coordonnée du centroïde.
<br>_le centroïde est ce qu'on appel en physique le centre de masse et correspond au point d'équilibre de tous les pixels à 1_
<br>$$ centroid = \left(C_x, C_y\right) = \frac{\left(\sum x I_{x,y}, \sum y I_{x,y}\right)}{area}, \forall x,y\in shape $$
<br>où :
<br>&nbsp;&nbsp;&nbsp;- $I_{x,y}$ est la valeur de l'image à la coordonnées $x$ et $y$
<br>&nbsp;&nbsp;&nbsp;- $x$ est la coordonnées sur les abscisses
<br>&nbsp;&nbsp;&nbsp;- $y$ est la coordonnées sur les ordonnées
1. Considérant qu'une seule forme se trouve dans l'image et que les bordures sont à 0, faites une fonction qui calcule le périmètre de la forme.
<br>`perimeter(image)`
<br>&nbsp;&nbsp;&nbsp;- `image` est l'image à considérer
<br>&nbsp;&nbsp;&nbsp;- `return` un `float` représentant le périmètre de la forme.
<br>__attention__ _cet exercice présente un niveau de difficulté __beaucoup__ plus élevé_ __<---__
