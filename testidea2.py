import numpy as np

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

imag2 =[[0,0,0,0,0,0,0,0,0,0],
        [0,0,1,1,0,0,0,0,0,0],
        [0,0,1,1,0,0,0,0,0,0],
        [0,0,1,1,0,0,0,0,0,0],
        [0,0,1,1,0,0,0,0,0,0],
        [0,0,1,1,1,1,1,0,0,0],
        [0,0,1,1,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]]

def affiche(image, image2):
    image = np.array(image)
    image2 = np.array(image2)
    return image, image2

def get_boundery_corner(image):
    liste_y = np.sum(image,axis=0)
    liste_x = np.sum(image,axis=1)
    max_Y = np.where(liste_y != 0)[0]
    max_X = np.where(liste_x != 0)[0]
    p1 = (max_X[0],max_Y[0])
    p3 = (max_X[-1],max_Y[-1])
    p2 = (p1[0],p3[1])
    p4 = (p3[0],p1[1])
    image[*p1] = 5
    image[*p2] = 6
    image[*p3] = 7
    image[*p4] = 8
    print(image)
    return p1,p3

def get_centroid(p1,p3,p2,p4): # version ou on trouve le  pente puis trouver le point d'intersection jsp comment faire
    pente_p1_p3 = (p3[0]-p1[0])/(p3[1]-p1[1]) #soit y = pente_p1_p3x + b
    pente_p2_p4 = (p2[0]-p4[0])/(p2[1]-p4[1]) #soit y = pente_p2_p4x+ b
    print(pente_p1_p3,"----",pente_p2_p4)

def area(image):
  return np.sum(image)

def get_centroid2(p1,p3,p2):
    centre_x = (p1[1]+(p2[1]-p1[1])/2)
    
    # probleme ici la valeur du centre n'est pas un int just peux donc pas etre afficher 
    centre_y = (p2[0]+(p3[0]-p2[0])/2)
    centroid =centre_y,centre_x

    # il faut danc calculer la difference entre les coordonner centre a un point (peux importe)
    p_ab = (p2[1]-p1[1])-centroid[1]
    p_bc = (p3[0]-p2[0])-centroid[0]
    print(p_ab,p_bc)
    r = np.sqrt(pow(p_ab,2)+pow(p_bc,2))
    return r, centroid # r pour rayon du cercle 

def air_cercle(rayon):
    air = np.pi*rayon*rayon
    return air

image, imag2 = affiche(image,imag2)

# print(image)
# print("-----------")
# print(imag2)

p1,p3 = get_boundery_corner(image)
print("-----------")
p12,p32 = get_boundery_corner(imag2)

p2 = (p1[0],p3[1])
p4 = (p3[0],p1[1])

p22 = (p1[0],p3[1])
p42 = (p3[0],p1[1])

# get_centroid(p1,p3,p2,p4)
rayon, centroid= get_centroid2(p1,p3,p2)
print("-----------")
rayon2, centroid2= get_centroid2(p12,p32,p22)

# print(*centroid)
# print("-----------")
# print(*centroid2)
print(rayon)
print("-----------")
print(rayon2)

air = air_cercle(rayon)
areas = area(image)
print (areas)
print(areas*100/air)



#donc jai le centroid de limage + rayon du cercle qui couvre le tout