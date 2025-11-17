import numpy as np

def create_image(size):
  return np.zeros((size[1], size[0]), dtype=np.uint8)


def draw_rectangle(image, top_left, bottom_right):
    top_left = (max(0,top_left[0]), max(0,top_left[1]))
    bottom_right = (min(image.shape[1],bottom_right[0]), min(image.shape[0],bottom_right[1]))
    image[top_left[1]:bottom_right[1],top_left[0]:bottom_right[0]] = 1

def get_perimeter_flat(image):
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

def get_perimeter_coord(image):
    _, w = image.shape
    coordActivated = get_perimeter_flat(image)
    y = coordActivated // w
    x = coordActivated % w
    return np.stack((y, x), axis=1)





im = create_image((20,20))

print(im)



"""
print()
print(im.shape[1])
draw_rectangle(im, (2,3), (8,6))
print(im)
print()
data = get_perimeter_coord(im)

print(data)
"""