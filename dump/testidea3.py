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

def affiche(image):
    image = np.array(image)
    return image

def get_boundery_corner(image):
    liste_y = np.sum(image,axis=0)
    liste_x = np.sum(image,axis=1)
    max_Y = np.where(liste_y != 0)[0]
    max_X = np.where(liste_x != 0)[0]
    p1 = (max_X[0],max_Y[0])
    p3 = (max_X[-1],max_Y[-1])
    # p2 = (p1[0],p3[1])
    # p4 = (p3[0],p1[1])
    # return p1,p2,p3,p4
    print("---------------")
    print("",liste_y, "liste_y\n", max_Y , "max_Y")
    print("---------------")
    print("",liste_x, "liste_x\n", max_X, "max_X")
    print("---------------")
    print(*p1,"top_left")
    print(*p2,"top_right")
    print(*p3,"bottom_right")
    print(*p4,"bottom_left")
    return p1,p3


def get_centroid2(p1,p3,p2):
    centre_x = (p1[1]+(p2[1]-p1[1])/2)
    # probleme ici la valeur du centre n'est pas un int just peux donc pas etre afficher 
    centre_y = (p2[0]+(p3[0]-p2[0])/2)
    centroid =centre_y,centre_x

    # il faut danc calculer la difference entre les coordonner centre a un point (peux importe)
    p_ab = (p2[1]-p1[1])-centroid[1]
    p_bc = (p3[0]-p2[0])-centroid[0]
    r = np.sqrt(pow(p_ab,2)+pow(p_bc,2))
    return r, centroid # r pour rayon du cercle 

# def get_centroid3(image,p1,p3):
#     cx = np.mean(image,axis=1)
#     cy = np.mean(image,axis=0)
#     centroid = cy,cx
#     p2 = p1[1],p3[0]
#     p4 = p2[1]+((p3[1]-p2[1])/2)
#     p_ab = p4-p2[1]
#     p_bc = 
#     # p_ab = (p3[1]-p1[1])-centroid[1]
#     p_bc = (p3[0]-p3[0])-centroid[0]

#     r = np.sqrt(pow(p_ab,2)+pow(p_bc,2))



image = affiche(image)

print(image)
# p1,p2,p3,p4 = get_boundery_corner(image)
p1,p3 = get_boundery_corner(image)
# rayon, centroid= get_centroid2(p1,p3,p2)

print(*centroid)
print(rayon)
# a,b=centroid(image)
# print(a,b)


#donc jai le centroid de limage + rayon du cercle qui couvre le tout