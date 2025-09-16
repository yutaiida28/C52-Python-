import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QColor
from PySide6.QtWidgets import ( QApplication,
                                QWidget,
                                QLabel,
                                QScrollBar,
                                QHBoxLayout)

class GOLApp(QWidget):
     def __init__(self, parent = None):
        super().__init__(parent)
        extra_size = 35
        game_size = 50

        self.__control = QLabel()
        self.__control.setFixedHeight(extra_size)
        self.__control.setFixedWidth(extra_size)
        self.__control.setStyleSheet("background-color: red;")

        sef.__jeux.s

        game_layout = QHBoxLayout()
        game_layout.addWidget(self.__control)

        self.setLayout(game_layout)
        
   
    



    




def main():
    app = QApplication(sys.argv) # ceci est le rapper de l'application c'est ce qui ecoute le imput de l'usager (while action = 0 rien else il dispatch cest info a la bonne place 

    #sys.argv sont les argument passée en ligne de commande quand on lance l'application

    w = GOLApp() # C'est la fenêtre

    w.show() # Affichage de la fenêtre

    sys.exit(app.exec()) # On roule l'application et quand elle est terminé on fait un exit
    # est aussi comme un blocker 

if __name__ == '__main__':
    main()