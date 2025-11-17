import numpy as np
import random
from copy import deepcopy
from __feature__ import snake_case, true_property
class GOLEngine:

    def __init__(self, width, height):
        self.__width = None
        self.__height = None
        self.__grid = None
        self.__temp = None
        
        # Statistics
        self.__dead_cell = 0
        self.__live_cell = 0
        self.__total_cell = 0
        self.__generation = 0
        
        # Rules as Look-Up Tables (LUT)
        #                    0, 1, 2, 3, 4, 5, 6, 7, 8 <--- Number of living neighbors
        # self.__alive_rule = (0, 0, 1, 1, 0, 0, 0, 0, 0)  # Survive with 2 or 3 neighbors
        # self.__dead_rule  = (0, 0, 0, 1, 0, 0, 0, 0, 0)  # Born with 3 neighbors
        # self.__rules = (self.__dead_rule, self.__alive_rule)
        self.__alive_rule = np.array([0, 0, 1, 1, 0, 0, 0, 0, 0], dtype=np.uint8)
        self.__dead_rule  = np.array([0, 0, 0, 1, 0, 0, 0, 0, 0], dtype=np.uint8)
        self.__rules = np.stack((self.__dead_rule,self.__alive_rule))
        
        self.resize(width, height)
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

    @property
    def cells_alive(self):
        """Number of living cells."""
        return self.__live_cell
    
    @property
    def cells_dead(self):
        """Number of dead cells."""
        return self.__dead_cell
    
    @property
    def cells_count(self):
        """Total number of cells."""
        return self.__total_cell
    
    @property
    def generation(self):
        """Current generation number."""
        return self.__generation
    
    @property
    def alive_percent(self):
        """Percentage of living cells."""
        return (self.__live_cell / self.__total_cell * 100) if self.__total_cell > 0 else 0
    
    @property
    def dead_percent(self):
        """Percentage of dead cells."""
        return (self.__dead_cell / self.__total_cell * 100) if self.__total_cell > 0 else 0
    
    def cell_value(self,j):
        """Get the value of a cell at position (x, y)."""
        data = self.__grid.flatten().astype(np.int32)
        return data[j]
   

    def resize(self, width, height):
        """Resize the grid to the specified dimensions."""
        if width < 3 or height < 3:
            raise ValueError('Width and height must be greater or equal to 3.')

        self.__width = width
        self.__height = height
        
        self.__grid = np.zeros((self.__height, self.__width), dtype=np.uint32)
        self.__temp = deepcopy(self.__grid)
        
        self.__generation = 0
        # self.__update_info()
        self.__update_info(self.__grid)

   
    
    def randomize(self, percent=0.5):
        # place des entite de maniere alleatoire
        for y in range(1, self.__height - 1): 
            for x in range(1, self.__width - 1):
                self.__grid[x][y] = int(random.random() > percent)
        
        self.__generation = 0
        self.__update_info(self.__grid)
        
    def process(self):
        """Process one generation of the Game of Life."""
        h, w = self.__grid.shape
        data = self.__grid.flatten().astype(np.int32)
        # data = np.where(data == 0, 1, 0)
        coord = np.arange(data.size)
        coordActivated = coord[data == True]
        top = data[coordActivated - w]

        top_left, top_right = data[[coordActivated-1, coordActivated+1]]
        left, right = data[[coordActivated - 1, coordActivated + 1]] 
        bottom = data[coordActivated + w]
        bottom_left, bottom_right = data[[coordActivated -1, coordActivated +1]]
        total = top + bottom + left + right + top_left + top_right + bottom_left + bottom_right

        self.__temp[1:-1,1:-1] = self.__rules[coordActivated, total]
        # self.__temp[y][x] = self.__rules[self.__grid[x][y]][neighbours]
        # for x in range(1, self.__width - 1):
        #     for y in range(1, self.__height - 1):
        #         # Count living neighbors using optimized slicing
        #         neighbours = sum(self.__grid[x-1][y-1:y+2]) \
        #                    + sum(self.__grid[x][y-1:y+2:2]) \
        #                    + sum(self.__grid[x+1][y-1:y+2])
                
        #         # Apply rules using LUT
        #         self.__temp[y][x] = self.__rules[self.__grid[x][y]][neighbours]

    def __update_info(self,image : np.array):
        _, w = image.shape
        data = image.flatten().astype(np.int32)
        self.__total_cell = self.__width * self.__height
        vivant = sum(data[:])
        self.__live_cell = vivant
        self.__dead_cell = self.__total_cell - vivant

       
