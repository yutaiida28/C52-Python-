# Moteur de jeu de la vie (Game Of Life).
#
# Version préliminaire simple et fonctionnelle.
#
# Cette implémentation respecte l'encapsulation et l'utilisaiton des propriétés.
#
# Toutefois, elle est sans :  
#  - documentation
#  - tests
#  - optimisation
#  - interface graphique (c'est désirée puisque c'est un moteur)


import random
from copy import deepcopy

class GOLEngine:
    def __init__(self, width, height):
        self.__width = None
        self.__height = None
        self.__grid = None
        self.__temp = None

        self.__dead_cell = 0
        self.__live_cell = 0
        self.__total_cell = 0


 # Approche avec une table de recherche : LUT (Look-Up Table)
        #                    0, 1, 2, 3, 4, 5, 6, 7, 8 <--- Nbr de voisins vivants
        self.__alive_rule = (0, 0, 1, 1, 0, 0, 0, 0, 0)
        self.__dead_rule  = (0, 0, 0, 1, 0, 0, 0, 0, 0)

        #                           0   ,       1
        self.__rules = (self.__dead_rule,self.__alive_rule)
        
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
        return self.__live_cell
    
    @property
    def cells_dead(self):
        return self.__dead_cell
    
    @property
    def cells_count(self):
        return self.__total_cell
        
    def cell_value(self, x, y):
        return self.__grid[x][y]
        
    def set_cell_value(self, x, y, value):
        self.__grid[x][y] = value
    
    def resize(self, width, height):
        if width < 3 or height < 3:
            raise ValueError('width and height must be greater or equal to 3.')

        self.__width = width
        self.__height = height
        self.__grid = []
        self.__temp = []
        
        self.__grid = [ [0]* self.__height for _ in range(self.__width)]
        self.__temp = deepcopy(self.__grid)
        self.__update_info()
    


    def randomize(self, percent=0.5):
        for y in range(1, self.__height - 1): 
            for x in range(1, self.__width - 1):
                self.__grid[x][y] = int(random.random() > percent)
        self.__update_info()

        
    def process(self):
        for x in range(1, self.__width-1):
            for y in range(1, self.__height-1):
                neighbours = sum(self.__grid[x-1][y-1:y+2])\
                           + sum(self.__grid[x][y-1:y+2:2])\
                           + sum(self.__grid[x+1][y-1:y+2])

                self.__temp[x][y] = self.__rules[self.__grid[x][y]][neighbours]
                #
                    
        
        self.__grid, self.__temp = self.__temp, self.__grid
        self.__update_info()


        
        

    def __update_info(self):
        self.__total_cell = self.__width*self.__height
        vivant = 0
        for x in range(self.__width):
            # for y in range(self.__height):
            vivant += sum(self.__grid[x][:])
        self.__live_cell = vivant
        self.__dead_cell = self.__total_cell -vivant


    




    def fill(self,value = 0):
        num = int(value == 1)
        self.__grid = [[num for _ in range(self.__height)] for _ in range(self.__width)]
        self.__update_info()

    
    def print(self):
        for y in range(self.__height):
            for x in range(self.__width):
                print(self.__grid[x][y], end='')
            print()
        print()

    
    
    @property
    def total_cells(self):
        return self.__total_cell
    
    @property
    def live_cells(self):
        return 

    
       
    
    
    
    
# quelques tests simples    
def main():
    gol = GOLEngine(12, 10)
    
    gol.resize(12, 9)
    print(f'taille : {gol.width} x {gol.height}')

    gol.width = 13
    gol.height = 8
    print(f'taille : {gol.width} x {gol.height}')

    gol.set_cell_value(4, 3, 0)
    gol.set_cell_value(5, 3, 1)
    print(f'(4, 3) = {gol.cell_value(4, 3)}')
    print(f'(5, 3) = {gol.cell_value(5, 3)}')

    gol.randomize(0.95)
    print(f'(4, 3) = {gol.cell_value(4, 3)}')
    print(f'(5, 3) = {gol.cell_value(5, 3)}')

    gol.randomize(0.05)
    print(f'(4, 3) = {gol.cell_value(4, 3)}')
    print(f'(5, 3) = {gol.cell_value(5, 3)}')
    
    gol.randomize(0.5)
    gol.print()
    gol.process()
    gol.print()

    gol.fill()
    gol.print()
    # print(GOLEngine.cell_total)
    print(gol.total_cells())
    print(gol.live_cells())

    pass


if __name__ == '__main__':
    main()
    


# ---------------------------------------------------------
### Proposition d'exercices
# ---------------------------------------------------------
# 1. Tentez d'améliorer le moteur afin de le rendre plus performant.
#    Par exemple, on peut éviter des allocations mémoire inutiles, des conditions inutiles et des boucles explicites en Python.
# 2. Ajouter une méthode 'fill(cell_value)' qui remplit toute la grille avec la valeur donnée (0 ou 1).
# 2. Changer le code pour qu'on puisse changer la règle du jeu (naissance et survie).
#    Par exemple, la règle actuelle est : naissance = 3, survie = 2 ou 3.
#    On pourrait imaginer une règle comme : naissance = 3 ou 6, survie = 2, 3 ou 4.
#    Faites en sorte qu'on puisse définir ces deux groupes de conditions, que vous donnez accès à des propriétés et que la fonction process les utilise.
# 3. Ajouter dans le moteurs des propriétés en lecture seule pour donner accès à ces statistiques :
#    - nombre de cellules totales
#    - nombre de cellules vivantes (en absolu et en relatif)
#    - nombre de cellules mortes (en absolu et en relatif)
#    - nombre de générations (nombre d'appels à process) 
#      Attention, dès que la grille change (resize, randomize ou fill), le compteur doit être remis à zéro.
#



