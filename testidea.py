import numpy as np

def affichePixmap(image):
    image = np.array(image)
    # print(image)
    return image

def get_max_min(image):
    liste_y = np.sum(image,axis=0) #donc l'axis 0 fait reffairence a y 
    liste_x = np.sum(image,axis=1)
    max_Y = np.where(liste_y != 0)[0]
    max_X = np.where(liste_x != 0)[0]
    p_ab = len(max_Y)+2
    p_bc = len(max_X)+2
    centroid = np.sqrt(pow(p_ab,2)+pow(p_bc,2))/2 #ca vas crash ici car il a juste un variable qui est ni z ou y  de plus ce n'est que une maniere de trouver le milieux de Hypoténuse
    print(centroid)
    # print(liste_y)
    # print(max_Y)
    # print("----------------")
    # print(liste_x)
    # print(max_X)
    top_left = (max_X[0]-1,max_Y[0]-1)
    bottom_right = (max_X[-1]+1,max_Y[-1]+1)
    image[*top_left]=3
    image[*bottom_right]=4
    return top_left,bottom_right

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

image = affichePixmap(image)

print(image)
p1,p2 = get_max_min(image)
p3 = (p1[0],p2[1])
image[*p3]=5
print(image)



# fail 