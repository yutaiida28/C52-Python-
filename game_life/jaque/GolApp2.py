import sys
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QPixmap, QColor, QPainter, QBrush
from PySide6.QtWidgets import (QApplication
                               , QWidget
                               , QLabel
                               , QGroupBox
                               , QScrollBar
                               , QHBoxLayout
                               , QVBoxLayout
                               , QPushButton)

from GolEngine import GOLEngine


class QInfoWidget(QGroupBox):
    def __init__(self):
        super().__init__("Info")  # Initialize the parent QGroupBox with title
        self.setStyleSheet("""
            QGroupBox {
                font-weight: bold;
                border: 2px solid gray;
                border-radius: 5px;
                margin-top: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
            }
        """)
        self.__layout = QVBoxLayout()

        self.__total_label = QLabel("Cells:")
        self.__alive_label = QLabel("Cells alive:")
        self.__dead_label = QLabel("Cells dead:")
        self.__revolution_label = QLabel("Revolution:")  # Fixed typo: lable -> label

        self.__layout.addWidget(self.__total_label)
        self.__layout.addWidget(self.__alive_label)
        self.__layout.addWidget(self.__dead_label)
        self.__layout.addWidget(self.__revolution_label)

        self.setLayout(self.__layout)
    def update_info(self):
        self.__total_label.setText(f"Cells: {self.__engine.cells_count}")
        self.__alive_label.setText(f"Cells alive: {self.__engine.cells_alive}")
        self.__dead_label.setText(f"Cells dead: {self.__engine.cells_dead}")
        self.__revolution_lable.setText(f"Revolution: {self.__revolution}")

        
        

class GolAPP(QWidget):

    def __init__(self,parent = None):
        super().__init__(parent)

        #Sizes
        self.__game_size = 500
        self.__layouts_width = 250



        # self.main_layout = QHBoxLayout
        # self.layout_control = QVBoxLayout()
        # self.layout_game = LayoutGame(self.__game_size, self)
        self.layout_info = QVBoxLayout()

        # self.main_layout.addLayout(self.layout_control)
        # self.main_layout.addLayout(self.layout_game)
        # self.main_layout.addLayout(self.layout_info)

        self.__engine = GOLEngine(100,100)
        self.init_game()


        self.__timeout = 100
        self.__timer = QTimer()
        self.__timer.timeout.connect(self.__update_game_view)
        self.__timer.timeout.connect(self.update_info)




        self.status_button = QPushButton()
        self.status_button.setText("Play")
        self.status_button.clicked.connect(self.update_control)

        step_button = QPushButton()
        step_button.setText("Step")
        step_button.clicked.connect(self.__update_game_view)

        speed_label = QLabel()
        speed_label.setNum(self.__timeout)

        step_scrollbar = QScrollBar()
        step_scrollbar.setOrientation(Qt.Horizontal)
        step_scrollbar.setRange(0,500)
        step_scrollbar.setValue(self.__timeout)
        step_scrollbar.valueChanged.connect(lambda value: self.change_timout(value))
        step_scrollbar.valueChanged.connect(speed_label.setNum)
    
        reset_button = QPushButton()
        reset_button.setText("Reset")
        reset_button.clicked.connect(self.init_game)

        group_control = QGroupBox("Control")

        initial_control = QVBoxLayout()
        initial_control.addWidget(self.status_button)
        initial_control.addWidget(step_button)
        initial_control.addWidget(speed_label)
        initial_control.addWidget(step_scrollbar)
        initial_control.addWidget(reset_button)
        initial_control.setContentsMargins(10, 10, 10, 10)
        initial_control.setSpacing(5)

        group_control.setLayout(initial_control)

        control_layout = QVBoxLayout()
        control_layout.addWidget(group_control)
        control_layout.addStretch(1)




        self.__view = QLabel()



        self._info_widget = QInfoWidget()
        self.layout_info.addStretch(1)
        self.layout_info.addWidget(self._info_widget)     

        
        
        main_layout = QHBoxLayout()
        main_layout.addLayout(control_layout,1)
        main_layout.addWidget(self.__view,2)
        main_layout.addLayout(self.layout_info,1)

        self.setLayout(main_layout)
        self.setMinimumSize(1000,500)


        self.__update_game_view()


    def init_game(self):
        self.__engine.randomize(0.7)
        self.__revolution = 0



    def update_control(self):

        if self.__timer.isActive():
            self.status_button.setText("Play")
            self.__timer.stop()
        else:
            self.status_button.setText("Stop")
            self.__timer.start(self.__timeout)


    def change_timout(self,value):
        self.__timeout = 500-value
        self.__timer.stop()
        self.update_control()


    def update_info(self):
        self.__total_label.setText(f"Cells: {self.__engine.cells_count}")
        self.__alive_label.setText(f"Cells alive: {self.__engine.cells_alive}")
        self.__dead_label.setText(f"Cells dead: {self.__engine.cells_dead}")
        self.__revolution_lable.setText(f"Revolution: {self.__revolution}")

        
    def __update_game_view(self):
        cadre = QPixmap(self.__view.size())
        cadre.fill(Qt.black)
        brush = QPainter(cadre)
        brush.setPen(Qt.black)

        self.__revolution += 1

        view_size = self.__view.size()
        cell_width = view_size.width() / self.__engine.width   
        cell_height = view_size.height() / self.__engine.height
       

       # Refaire avec un QImage de wxh, dessiner par pixel et ensuite rescale l'image
       #Pixmap.from_image() # refaire un pixmap à partir d'une image.
       # i.scaled(params...,voir les params) nouvelle image resized
       # nearest, paramêtre à checker

        for x in range(1,self.__engine.width-1):
            for y in range(1,self.__engine.height-1):
                if self.__engine.cell_value(x, y) == 1:  # Cellule vivante
                    rect_x = x * cell_width
                    rect_y = y * cell_height
                    brush.fillRect(rect_x, rect_y, int(cell_width)+1, int(cell_height)+1, Qt.white)
        
        brush.end()
        self.__view.setPixmap(cadre)
        self.__engine.process()



        
        




def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    g = GolAPP()
    g.show()

    sys.exit(app.exec())




    pass




if __name__ == '__main__':
    main()
    