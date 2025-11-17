import numpy as np
import random

class GOLEngine:
    def __init__(self, width, height):
        self.__width = None
        self.__height = None
        self.__grid = None
        self.__temp = None

        # neighbour LUT rules
        self.__alive_rule = np.array([0, 0, 1, 1, 0, 0, 0, 0, 0], dtype=np.uint8)
        self.__dead_rule  = np.array([0, 0, 0, 1, 0, 0, 0, 0, 0], dtype=np.uint8)
        self.__rules = np.stack((self.__dead_rule, self.__alive_rule))

        self.resize(width, height)

    # ---------------------------------------------------------------------
    # Properties
    # ---------------------------------------------------------------------
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        self.resize(value, self.__height)
    
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.resize(self.__width, value)

    # ---------------------------------------------------------------------
    # Cell access
    # ---------------------------------------------------------------------
    def cell_value(self, x, y):
        return self.__grid[x, y]

    def set_cell_value(self, x, y, value):
        self.__grid[x, y] = value

    # ---------------------------------------------------------------------
    # Resize
    # ---------------------------------------------------------------------
    def resize(self, width, height):
        if width < 3 or height < 3:
            raise ValueError("width and height must be >= 3")

        self.__width = width
        self.__height = height

        # Initialize NumPy arrays
        self.__grid = np.zeros((width, height), dtype=np.uint8)
        self.__temp = np.zeros_like(self.__grid)

    # ---------------------------------------------------------------------
    # Random fill
    # ---------------------------------------------------------------------
    def randomize(self, percent=0.5):
        # Random values inside inner area only
        self.__grid[1:-1, 1:-1] = (np.random.random((self.__width - 2, self.__height - 2)) > percent).astype(np.uint8)

    # ---------------------------------------------------------------------
    # Process one step of Game of Life
    # ---------------------------------------------------------------------
    def process(self):
        g = self.__grid

        # Count neighbors using slicing (super fast)
        neighbours = (
            g[:-2, :-2] +
            g[:-2, 1:-1] + 
            g[:-2, 2:] +
            g[1:-1, :-2] +                  
            g[1:-1, 2:] +
            g[2: , :-2] + 
            g[2: , 1:-1] + 
            g[2: , 2:]
        )

        center = g[1:-1, 1:-1]

        # apply rule LUT: rules[state][neighbor_count]
        self.__temp[1:-1, 1:-1] = self.__rules[center, neighbours]

        # swap buffers
        self.__grid, self.__temp = self.__temp, self.__grid

    # ---------------------------------------------------------------------
    # Print grid
    # ---------------------------------------------------------------------
    def print(self):
        for y in range(self.__height):
            for x in range(self.__width):
                print(self.__grid[x, y], end="")
            print()
        print()

# -------------------------------------------------------------------------
# Test
# -------------------------------------------------------------------------
def main():
    gol = GOLEngine(12, 10)
    gol.print()
    print()
    gol.randomize(0.5)
    gol.print()
    gol.process()
    gol.print()
    gol.process()
    gol.print()
    gol.process()
    gol.print()
    gol.process()
    gol.print()
if __name__ == "__main__":
    main()
