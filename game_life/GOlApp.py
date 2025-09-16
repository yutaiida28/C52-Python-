import sys
from copy import deepcopy
import random
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QColor
from PySide6.QtWidgets import ( QApplication,
                                QWidget,
                                QLabel,
                                QScrollBar,
                                QHBoxLayout,
                                QVBoxLayout)

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

class GOLApp(QWidget):
    
    def __init__(self, parent = None):
        super().__init__(parent)
        extra_size = 170
        game_size = 500
        #layout principal 
        screen_layout = QHBoxLayout()
        #les trois layout intern
        control_layout = QVBoxLayout()
        game_layout = QVBoxLayout()
        info_layout = QVBoxLayout()

        #appel de fonction pour fair les deux case extrat
        #parrametre
        self.__control = self.__extra_layout(extra_size,"setting")
        control_layout.addWidget(self.__control )
        control_layout.addStretch()
        #info
        self.__info = self.__extra_layout(extra_size,"info")
        info_layout.addStretch()
        info_layout.addWidget(self.__info)


        self.__jeu = QLabel()
        self.__jeu.setMinimumSize(game_size, game_size)
        self.__jeu.setStyleSheet("background-color: yellow;")
        game_layout.addWidget(self.__jeu)
        screen_layout.addLayout(control_layout)
        screen_layout.addLayout(game_layout)
        screen_layout.addLayout(info_layout)

        self.setLayout(screen_layout)
    
    def __extra_layout(self, extra_size, nom):

        layout = QLabel()
        layout.setMinimumSize(extra_size, extra_size)
        layout.setMaximumSize(extra_size, extra_size)
        if nom == "setting":
            layout.setStyleSheet("background-color: red;")
        elif nom == "info":
             layout.setStyleSheet("background-color: blue;")
        return layout
    
        
   
def main():
    app = QApplication(sys.argv) # ceci est le rapper de l'application c'est ce qui ecoute le imput de l'usager (while action = 0 rien else il dispatch cest info a la bonne place 
    gol = GOLEngine(4, 4)

    #sys.argv sont les argument passée en ligne de commande quand on lance l'application
    gol.randomize(0.5)
    w = GOLApp() # C'est la fenêtre

    w.show() # Affichage de la fenêtre

    sys.exit(app.exec()) # On roule l'application et quand elle est terminé on fait un exit
    # est aussi comme un blocker 

if __name__ == '__main__':
    main()