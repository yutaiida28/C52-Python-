import numpy as np

class Calcule:
    @staticmethod
    def area(image):
        return np.sum(image)
    @staticmethod
    def proportion(self, rayon,image):
        air = np.pi*rayon*rayon
        areas = self.area(image)
        return areas*100/air
    
    @staticmethod
    def get_rayon(distance):
        rayon_max = max(distance)
        rayon_min = min(distance)
        return rayon_max, rayon_min
    @staticmethod
    def affiche(image):
        image = np.array(image)
        return image
    @staticmethod
    def get_centroid(self,image):
        c, r = np.meshgrid(np.arange(image.shape[1]), np.arange(image.shape[0]))
        return (np.sum(r * image), np.sum(c * image)) / self.area(image)
    @staticmethod
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
    @staticmethod
    def get_perimeter_coord(self, image:np.array) -> np.array:
        _, w = image.shape
        coordActivated = self.get_perimeter_flat(image)
        y = coordActivated // w
        x = coordActivated % w
        return np.stack((y, x), axis=1)
    @staticmethod
    @staticmethod
    @staticmethod
    @staticmethod
    @staticmethod
    @staticmethod