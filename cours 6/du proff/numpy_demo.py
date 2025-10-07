import numpy as np






























def create_img(size):
    # np.bool n'est pas un bon choix recomander 
    # je trouve que c'est melangent que le x,y est invercer dans numpy donc aulieux de dire data [y,x] on dit data [r,c] row = ligne col = col
    # return np.zeros(size, dtype= np.uint8)
    # ceci est la cersion inversser 
    return np.zeros((size[1],size[0]), dtype= np.uint8)

def fill(image, color = 1):
    image[:]= color

def randomize(image, percent=0.5):
    rng = np.random.default_rng()
    n = rng.random()
    c = 0 if n <= percent else 1
    image[0, 0] = c  
    #maintenent il faut faire les trois ligne precedente dans une double boucle for  voir v2 
    

def randomizeV2(image, percent=0.5):
    rng = np.random.default_rng()
    n = rng.random(image.shape)
    t = n <= percent
    c = t.astype(image.dtype)
    image[:] = c  

def randomizeV3(image, percent=0.5):
    rng = np.random.default_rng()
    image[:] = (rng.random(image.shape) <= percent).astype(image.dtype)

def reset_border(image):
    image[:,  0] = 0 
    image[:, -1] = 0

    image[0,  :] = 0 
    image[-1, :] = 0


def reset_borderV2(image):
    # image[:,  0] = 0 
    # image[:, -1] = 0
    image[ :, [0,-1]]= 0
    # image[0,  :] = 0 
    # image[-1, :] = 0
    image[[0,-1]]= 0

#formule de pythagore c = (6,2) r =3  utilise mesh grid
def draw_circle(image, center, radius): #c=centre  r=radius 
    xr = np.arange(image.shape[1])
    yr = np.arange(image.shape[0])
    xi,yi = np.meshgrid(xr,yr)
    cx,cy = center
    dx = xi -cx
    dy = yi -cy
    dist = np.sqrt(dx ** 2 + dy ** 2) #dist2 = (dx ** 2 + dy ** 2) ** 0.5
    d = np.round(dist, 1).astype(np.int32)
    trace = (dist <= radius).astype(np.int32)
    new_im = np.logical_or(image, trace)
    image[:] = new_im
    pass

def draw_circleV2(image, center, radius): #c=centre  r=radius 
    cx,cy = center
    r2 = radius ** 2
    c,r = np.meshgrid(np.arange(image.shape[1]),np.arange(image.shape[0]))
    image[(c - cx) ** 2 + (r - cy) ** 3 <= r2] = 1



im =  create_img((10,8))

fill(im,0)
print(im)
print("-------------")

# randomizeV3(im, 0.25)
print(im)
print("-------------")

reset_borderV2(im)
print(im)
print("-------------")

# draw_circle(im,(6,2),3)
print(im)
print("-------------")

draw_circle(im,(4,5),2)
print(im)
print("-------------")