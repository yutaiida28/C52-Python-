
# version on a fait pour une couleur maintenent on vas le fair pour les 2 autre mais le code est plutot redondent donc 


import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QColor
from PySide6.QtWidgets import ( QApplication,
                                QWidget,
                                QLabel,
                                QScrollBar,
                                QHBoxLayout,
                                QVBoxLayout)

class ColorPicker(QWidget):
    
    def __init__(self, parent = None):
        super().__init__(parent)
        
        fixed_width = 35
        self.__red_sb = QScrollBar()
        self.__red_color = QLabel()
        self.__green_sb = QScrollBar()
        self.__green_color = QLabel()
        self.__blue_sb = QScrollBar()
        self.__blue_color = QLabel()
        self.__mixed_color = QLabel()
        self.__mixed_color.setFixedWidth(fixed_width)
        
        red_layout = self.__create_channel(self.__red_sb, self.__red_color, 'Red', fixed_width)
        green_layout = self.__create_channel(self.__green_sb, self.__green_color, 'Green',fixed_width)
        blue_layout = self.__create_channel(self.__blue_sb, self.__blue_color, 'Blue',fixed_width)
        
        channel_layout = QVBoxLayout()
        channel_layout.addLayout(red_layout)
        channel_layout.addLayout(green_layout)
        channel_layout.addLayout(blue_layout)

        layout = QHBoxLayout()
        layout.addLayout(channel_layout)
        layout.addWidget(self.__mixed_color)
        
        self.setLayout(layout)


    def __create_channel(self, sb, color, title_text, fixed_width):
        title = QLabel()
        value = QLabel()
        
        title.setText(title_text)
        title.setFixedWidth(fixed_width)
        
        sb.setOrientation(Qt.Horizontal)
        sb.setRange(0, 255)
        sb.setValue(0)
        sb.setMinimumWidth(2 * fixed_width)
        
        value.setNum(0)
        value.setFixedWidth(fixed_width)
        value.setAlignment(Qt.AlignCenter)
        
        title.setFixedWidth(fixed_width)
        
        channel_layout = QHBoxLayout()
        channel_layout.addWidget(title)
        channel_layout.addWidget(sb)
        channel_layout.addWidget(value)
        channel_layout.addWidget(color)
        
        # Etablissement des connexions
        sb.valueChanged.connect(value.setNum)
        sb.valueChanged.connect(self.__update_colors)# "red_sb.valueChanged." = signal est "connect(red_value.setNum)" est la slot 
        
        return channel_layout
        
    
    def __update_color(self, color_widget,r,g,b): # elle est prive
        image = QPixmap(color_widget.size())
        image.fill(QColor(r,g,b))
        color_widget.setPixmap(image)
    
    def __update_colors(self):
        r = self.__red_sb.value()
        g = self.__green_sb.value()
        b = self.__blue_sb.value()
        self.__update_color(self.__red_color,r,0,0)
        self.__update_color(self.__green_color,0,g,0)
        self.__update_color(self.__blue_color,0,0,b)
        self.__update_color(self.__mixed_color,r,g,b)

    def showEvent(self, event):
        super().showEvent(event)
        self.__update_colors()


def main():
    app = QApplication(sys.argv) # ceci est le rapper de l'application c'est ce qui ecoute le imput de l'usager (while action = 0 rien else il dispatch cest info a la bonne place 

    #sys.argv sont les argument passée en ligne de commande quand on lance l'application

    w = ColorPicker() # C'est la fenêtre

    w.show() # Affichage de la fenêtre

    sys.exit(app.exec()) # On roule l'application et quand elle est terminé on fait un exit
    # est aussi comme un blocker 

if __name__ == '__main__':
    main()