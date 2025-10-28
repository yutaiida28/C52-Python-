import numpy as np

image =[[0,0,0,0,0,0,0,0,0,0],
        [0,0,0,1,1,0,0,0,0,0],
        [0,0,0,1,1,0,0,0,0,0],
        [0,0,0,1,1,0,0,0,0,0],
        [0,0,0,1,1,0,0,0,0,0],
        [0,0,0,1,1,1,1,1,1,0],
        [0,0,0,1,1,1,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]]


imag2 =[[0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,1,0,0,0,0,0,0],
        [0,0,0,1,0,0,0,0,0,0],
        [0,0,0,1,1,1,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]]


imag3 =[[0,0,0,0,0,0,0,0,0,0],
        [0,0,1,1,0,0,0,0,0,0],
        [0,0,1,1,0,0,0,0,0,0],
        [0,0,1,1,0,0,0,0,0,0],
        [0,0,1,1,0,0,0,0,0,0],
        [0,0,1,1,1,1,1,1,0,0],
        [0,0,1,1,1,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]]

def affiche(image):
    image = np.array(image)
    return image

def area(image):
  return np.sum(image)

def get_centroid(image):
  c, r = np.meshgrid(np.arange(image.shape[1]), np.arange(image.shape[0]))
  return (np.sum(r * image), np.sum(c * image)) / area(image)

def _get_perimeter_flat(image:np.array) -> np.array:
    h, w = image.shape
    data = image.flatten().astype(np.int8)
    
    data = np.where(data == 0, 1, 0)

    coord = np.arange(data.size)
    coordActivated = coord[data == False]

    top = data[coordActivated - w]
    left, right = data[[coordActivated - 1, coordActivated + 1]]
    bottom = data[coordActivated + w]

    total = top + bottom + left + right

    return coordActivated[total > 0]

    # Return the coordinate of all points included in the perimeter of an image
def get_perimeter_coord(image:np.array) -> np.array:
    h, w = image.shape
    coordActivated = _get_perimeter_flat(image)

    y = coordActivated // w
    x = coordActivated % w

    return np.stack((y, x), axis=1)

def get_rayon(distance):
    rayon_max = max(distance)
    rayon_min = min(distance)
    return rayon_max, rayon_min

def proportion(rayon,image):
    air = np.pi*rayon*rayon
    areas = area(image)
    return areas*100/air

def premier_metric(image,data,centroid):
    distance = np.sqrt(pow(data[:,0]-centroid[0],2)+pow(data[:,1]-centroid[1],2))
    rayon = get_rayon(distance)
    return proportion(rayon[0],image)


def deuxiem_metric(data,centroid):
    distance = np.sqrt(pow(data[:,0]-centroid[0],2)+pow(data[:,1]-centroid[1],2))
    rayon = get_rayon(distance)
    return rayon[1]/rayon[0]

image = affiche(image)
data = get_perimeter_coord(image)
centroid1 = get_centroid(image)
# distance = np.sqrt(pow(data[:,0]-centroid1[0],2)+pow(data[:,1]-centroid1[1],2))
# rayon = get_rayon(distance)
# metric1 = proportion(rayon,image)

metric1 = premier_metric(image,data,centroid1)
metric2 = deuxiem_metric(data,centroid1)

print (metric1)
print(metric2)

print("-------------")

image2 = affiche(imag2)
data2 = get_perimeter_coord(image2)
centroid2 = get_centroid(image2)

metric1_2 = premier_metric(image2,data2,centroid2)
metric2_2 = deuxiem_metric(data2,centroid2)

print (metric1_2)
print(metric2_2)












"""
def premier_metric(image, data, centroid):
    distance = np.sqrt((data[:,0]-centroid[0])**2 + (data[:,1]-centroid[1])**2)
    rayon_max = np.max(distance)
    rayon_min = np.min(distance)

    # Normalize everything by rayon_max
    distance /= rayon_max
    rayon_min /= rayon_max

    # compute proportion using normalized radius (rayon_max = 1)
    normalized_area = area(image) / (np.pi * (rayon_max**2))
    return normalized_area * 100

"""