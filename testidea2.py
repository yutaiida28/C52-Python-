import numpy as np
def affiche(image):
    image = np.array(image)
    return image

def get_max_min(image):
    liste_y = np.sum(image,axis=0)
    liste_x = np.sum(image,axis=1)
    max_Y = np.where(liste_y != 0)[0]
    max_X = np.where(liste_x != 0)[0]
    top_left = (max_X[0]-1,max_Y[0]-1)
    bottom_right = (max_X[-1]+1,max_Y[-1]+1)
    return top_left,bottom_right

def get_centroid(p1,p2,p3,p4): # version ou on trouve le  pente puis trouver le point d'intersection jsp comment faire
    pente_p1_p2 = (p2[0]-p1[0])/(p2[1]-p1[1]) #soit y = pente_p1_p2x + b
    pente_p3_p4 = (p3[0]-p4[0])/(p3[1]-p4[1]) #soit y = pente_p3_p4x+ b
    print(pente_p1_p2,"----",pente_p3_p4)


def get_centroid2(p1,p2,p3):
    centre_x = (p1[1]+(p3[1]-p1[1])/2)
    # probleme ici la valeur du centre n'est pas un int just peux donc pas etre afficher 
    centre_y = (p3[0]+(p2[0]-p3[0])/2)
    centroid =centre_y,centre_x

    # il faut danc calculer la difference entre les coordonner centre a un point (peux importe)
    p_ab = (p3[1]-p1[1])-centroid[1]
    p_bc = (p2[0]-p3[0])-centroid[0]
    r = np.sqrt(pow(p_ab,2)+pow(p_bc,2))
    return r, centroid # r pour rayon du cercle 

image =[[0,0,0,0,0,0,0,0,0,0],
        [0,0,0,1,1,0,0,0,0,0],
        [0,0,0,1,1,0,0,0,0,0],
        [0,0,0,1,1,0,0,0,0,0],
        [0,0,0,1,1,0,0,0,0,0],
        [0,0,0,1,1,1,1,1,0,0],
        [0,0,0,1,1,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]]

image = affiche(image)


print(image)
p1,p2 = get_max_min(image)
p3 = (p1[0],p2[1])
p4 = (p2[0],p1[1])

# get_centroid(p1,p2,p3,p4)
rayon, centroid= get_centroid2(p1,p2,p3)

print(*centroid)
print(rayon)
# a,b=centroid(image)
# print(a,b)


#donc jai le centroid de limage + rayon du cercle qui couvre le tout