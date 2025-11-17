import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QColor
from PySide6.QtWidgets import ( QApplication,
                                QWidget,
                                QLabel,
                                QScrollBar,
                                QHBoxLayout)

from copy import deepcopy
import random


class GOLEngine:
    def __init__(self, width, height):
        self.__width = None
        self.__height = None
        self.__grid = None
        self.__temp = None
        
        #Approche avec lut 
        self.__alive_rule = (0,0,1,1,0,0,0,0,0)
        self.__dead_rule =  (0,0,0,1,0,0,0,0,0)

        self.__rules = (self.__alive_rule,self.__dead_rule)

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
        
    def cell_value(self, x, y):
        # no input validation for performance consideration
        return self.__grid[x][y]
        
    def set_cell_value(self, x, y, value):
        # no input validation for performance consideration
        self.__grid[x][y] = value
    
    def resize(self, width, height):
        if width < 3 or height < 3:
            raise ValueError('width and height must be greater or equal to 3.')

        self.__width = width
        self.__height = height
        self.__grid = []
        self.__temp = []
        
        # self.__grid = [[0 for _ in range(self.__height)] for _ in range(self.__width)]
        self.__grid = [[0] * self.__height for _ in range(self.__width)]
        self.__temp = deepcopy(self.__grid)
        
        for x in range(width):
            self.__grid.append([])
            self.__temp.append([])
            for _ in range(height):
                self.__grid[x].append(0)
                self.__temp[x].append(0)

    def randomize(self, percent=0.5):
        # petit correctif ici, on ne touche pas aux bords
        for y in range(1, self.__height - 1): 
            for x in range(1, self.__width - 1):
                self.__grid[x][y] = int(random.random() > percent)
        
    def process(self): #ici on a une liste de liste 
        for x in range(1, self.__width-1):
            for y in range(1, self.__height-1):
                neighbours = 0
                neighbours = sum(self.__grid[x-1][y-1:y+2])\
                           + sum(self.__grid[x  ][y-1:y+2:2])\
                           + sum(self.__grid[x+1][y-1:y+2])

                self.__temp[x][y] = self.__rules[self.__grid[x][y]][neighbours]
    
        self.__grid, self.__temp = self.__temp, self.__grid
    
    def print(self):
        for y in range(self.__height):
            for x in range(self.__width):
                print(self.__grid[x][y], end='')
            print()
        print()
    
    
    
    
    
# quelques tests simples    
def main():
    gol = GOLEngine(4, 4)
    
    gol.resize(12, 9)
    # print(f'taille : {gol.width} x {gol.height}')

    # gol.width = 13
    # gol.height = 8
    # print(f'taille : {gol.width} x {gol.height}')

    # gol.set_cell_value(4, 3, 0)
    # gol.set_cell_value(5, 3, 1)
    # print(f'(4, 3) = {gol.cell_value(4, 3)}')
    # print(f'(5, 3) = {gol.cell_value(5, 3)}')

    # gol.randomize(0.95)
    # print(f'(4, 3) = {gol.cell_value(4, 3)}')
    # print(f'(5, 3) = {gol.cell_value(5, 3)}')

    # gol.randomize(0.05)
    # print(f'(4, 3) = {gol.cell_value(4, 3)}')
    # print(f'(5, 3) = {gol.cell_value(5, 3)}')
    
    gol.randomize(0.5)
    gol.print()
    gol.process()
    gol.print()
    


if __name__ == '__main__':
        main()
    
