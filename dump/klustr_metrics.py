import numpy as np
class Clculer:
    # trianing 
    # nom nparry label
    def area(image):
        return np.sum(image)
    
    def proportion(self, rayon,image):
        air = np.pi*rayon*rayon
        areas = self.area(image)
        return areas*100/air
    
    def get_rayon(distance):
        rayon_max = max(distance)
        rayon_min = min(distance)
        return rayon_max, rayon_min

    def premier_metric(self, image, data, centroid):
        distance = np.sqrt(pow(data[:,0]-centroid[0],2)+pow(data[:,1]-centroid[1],2))
        rayon = self.get_rayon(distance)
        return self.proportion(rayon[0],image)

    def deuxiem_metric(self, data, centroid):
        distance = np.sqrt(pow(data[:,0]-centroid[0],2)+pow(data[:,1]-centroid[1],2))
        rayon = self.get_rayon(distance)
        return rayon[1]/rayon[0]
    
    def affiche(image):
        image = np.array(image)
        return image
       
    def get_centroid(self,image):
        c, r = np.meshgrid(np.arange(image.shape[1]), np.arange(image.shape[0]))
        return (np.sum(r * image), np.sum(c * image)) / self.area(image)
    
    # - PERIMETER - #
    # Return the flatten coordinate of an image
    def get_perimeter_flat(image:np.array) -> np.array:
        # Get the shape (only need the width)
        _, w = image.shape

        # Flatten the image
        data = image.flatten().astype(np.int8)
        
        # Inverse 1 and 0
        data = np.where(data == 0, 1, 0)

        # Get all the coordinate inside a array
        coord = np.arange(data.size)

        # Give all activated coordinate (Activated = forme)
        coordActivated = coord[data == False]

        # Get array of neighbor top line
        top = data[coordActivated - w]

        # Get array of neighbor left and right line
        left, right = data[[coordActivated - 1, coordActivated + 1]]

        # Get array of neighbor the bottom line
        bottom = data[coordActivated + w]

        # The sum of each neighbor
        total = top + bottom + left + right

        # Return the coordinate of perimeter (flat)
        return coordActivated[total > 0]

    # Return the coordinate of all points included in the perimeter of an image
    def get_perimeter_coord(self, image:np.array) -> np.array:
        _, w = image.shape
        coordActivated = self.get_perimeter_flat(image)
        y = coordActivated // w
        x = coordActivated % w
        return np.stack((y, x), axis=1)

    def training(self,nom,image,label):
        self.data = self.get_perimeter_coord(image)
        self.centroid = self.get_centroid(image)

        densite = self.premier_metric(image, self.data, self.centroid)
        distance_centroid = self.deuxiem_metric(self.data, self.centroid)
        metrix=


    
