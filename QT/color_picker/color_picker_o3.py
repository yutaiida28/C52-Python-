# ici on modifie les code pour quil y a seulement un convantion decriture
import sys
from PySide6.QtCore import Qt, Slot, Signal
from PySide6.QtGui import QPixmap, QColor
from PySide6.QtWidgets import ( QApplication,
                                QWidget,
                                QLabel,
                                QScrollBar,
                                QHBoxLayout,
                                QVBoxLayout)

from __feature__ import snake_case, true_property

class ColorPicker(QWidget):
    
    colorChanged = Signal(QColor)

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
    
    @Slot()
    def __update_colors(self):
        r = self.__red_sb.value()
        g = self.__green_sb.value()
        b = self.__blue_sb.value()
        self.__update_color(self.__red_color,r,0,0)
        self.__update_color(self.__green_color,0,g,0)
        self.__update_color(self.__blue_color,0,0,b)
        self.__update_color(self.__mixed_color,r,g,b)

        #emission explicite du signial colorChanged
        self.colorChanged.emit(self.color)

    @override
    def showEvent(self, event):
        super().showEvent(event)
        self.__update_colors()

    @property
    def color(self):
        r = self.__red_sb.value()
        g = self.__green_sb.value()
        b = self.__blue_sb.value()
        return QColor(r,g,b)
    
    @color.setter
    def color(self, value):
        if value != self.color:
            self.__red_sb.value() = value.red()
            self.__green_sb.value() = value.green()
            self.__blue_sb.value() = value.blue()

class DemoColorPickers(QWidget):

    def __init__(self):
        super().__init__()

        self._color_pickers = [ColorPicker() for _ in range(5)]

        self._color_pickers[0].colorChanged.connect(self._color_pickers[2].set_color)

        layout = QVBoxLayout()
        for color_picker in self._color_pickers:
            layout.add_widget(color_picker)

        layout.add_stretch()

        self.set_layout(layout)


def main():
    app = QApplication(sys.argv) # ceci est le rapper de l'application c'est ce qui ecoute le imput de l'usager (while action = 0 rien else il dispatch cest info a la bonne place 

    w = DemoColorPickers(QWidget) 
    w.show() 

    sys.exit(app.exec()) 

if __name__ == '__main__':
    main()