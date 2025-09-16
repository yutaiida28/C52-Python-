import sys
from PySide6.QtWidgets import ( QApplication,
                                QWidget,
                                QLabel,
                                QScrollBar,
                                QHBoxLayout)

class ColorPicker(QWidget):

    def __init__(self, parent = None):
        super().__init__(parent)

        red_title = QLabel()
        red_sb = QScrollBar()
        red_value = QLabel()
        red_color = QLabel()

        red_layout = QHBoxLayout()
        red_layout.addWidget(red_layout)
        red_layout.addWidget(red_sb)
        red_layout.addWidget(red_value)
        red_layout.addWidget(red_color)

def main():
    app = QApplication(sys.argv) # ceci est le rapper de l'application c'est ce qui ecoute le imput de l'usager (while action = 0 rien else il dispatch cest info a la bonne place 

    #sys.argv sont les argument passée en ligne de commande quand on lance l'application

    w = ColorPicker() # C'est la fenêtre

    w.show # Affichage de la fenêtre

    sys.exit(app.exec()) # On roule l'application et quand elle est terminé on fait un exit
    # est aussi comme un blocker 

if __name__ == 'main':
    main()