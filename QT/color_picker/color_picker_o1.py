# version on a fait pour une couleur maintenent on vas le fair pour les 2 autre mais le code est plutot redondent donc
import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QColor
from PySide6.QtWidgets import ( QApplication,
                                QWidget,
                                QLabel,
                                QScrollBar,
                                QHBoxLayout)

class ColorPicker(QWidget):

    def __init__(self, parent = None):
        super().__init__(parent)

        red_title = QLabel()
        self.__red_sb = QScrollBar()
        red_value = QLabel()
        self.__red_color = QLabel()

        fixed_width = 35
        red_title.setText('Red')
        red_title.setFixedWidth(fixed_width)

        self.__red_sb.setOrientation(Qt.Horizontal)
        self.__red_sb.setRange(0, 255)
        self.__red_sb.setValue(0)
        self.__red_sb.setMinimumWidth(2 * fixed_width)

        red_value.setNum(0)
        red_value.setAlignment(Qt.AlignCenter)
        red_value.setFixedWidth(fixed_width)

        self.__red_color.setFixedWidth(fixed_width)

        red_layout = QHBoxLayout()
        red_layout.addWidget(red_title)
        red_layout.addWidget(self.__red_sb)
        red_layout.addWidget(red_value)
        red_layout.addWidget(self.__red_color)

        self.setLayout(red_layout)
        #Établissement des connections
        self.__red_sb.valueChanged.connect(red_value.setNum) # "red_sb.valueChanged." = signal est "connect(red_value.setNum)" est la slot 
        self.__red_sb.valueChanged.connect(self.__update_red_color) 
    
    def __update_red_color(self): # elle est prive
        image = QPixmap(self.__red_color.size())
        image.fill(QColor(self.__red_sb.value(),0,0))
        self.__red_color.setPixmap(image)


def main():
    app = QApplication(sys.argv) # ceci est le rapper de l'application c'est ce qui ecoute le imput de l'usager (while action = 0 rien else il dispatch cest info a la bonne place 

    #sys.argv sont les argument passée en ligne de commande quand on lance l'application

    w = ColorPicker() # C'est la fenêtre

    w.show() # Affichage de la fenêtre

    sys.exit(app.exec()) # On roule l'application et quand elle est terminé on fait un exit
    # est aussi comme un blocker 

if __name__ == '__main__':
    main()