import sys
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QPixmap, QColor, QPainter, QBrush
from PySide6.QtWidgets import (QApplication
                               , QWidget
                               , QLabel
                               , QScrollBar
                               , QHBoxLayout
                               , QVBoxLayout
                               , QPushButton)

from GolEngine import GOLEngine


class GolAPP(QWidget):

    def __init__(self,parent = None):
        super().__init__(parent)

        self.init_game()

        self.__timeout = 100
        self.__timer = QTimer()
        self.__timer.timeout.connect(self.__update_game_view)
        self.__timer.timeout.connect(self.update_info)



        control_title = QLabel()
        control_title.setText("Control")
        control_title.setAlignment(Qt.AlignLeft)

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


        initial_control = QVBoxLayout()
        initial_control.addWidget(control_title)
        initial_control.addWidget(self.status_button)
        initial_control.addWidget(step_button)
        initial_control.addWidget(speed_label)
        initial_control.addWidget(step_scrollbar)
        initial_control.addWidget(reset_button)
        initial_control.setContentsMargins(10, 10, 10, 10)
        initial_control.setSpacing(5)

        control_layout = QVBoxLayout()
        control_layout.addLayout(initial_control)
        control_layout.addStretch(1)




        self.__view = QLabel()

        

        info_title = QLabel()
        info_title.setText("Information")
        info_title.setAlignment(Qt.AlignLeft)

        self.__total_label = QLabel("Cells:")
        self.__alive_label = QLabel("Cells alive:")
        self.__dead_label = QLabel("Cells dead:")
        self.__revolution_lable = QLabel("Revolution:")


        initial_info = QVBoxLayout()
        initial_info.addWidget(info_title)
        initial_info.addWidget(self.__total_label)
        initial_info.addWidget(self.__alive_label)
        initial_info.addWidget(self.__dead_label)
        initial_info.addWidget(self.__revolution_lable)

        info_layout = QVBoxLayout()
        info_layout.addStretch(1)
        info_layout.addLayout(initial_info)
        
        
        main_layout = QHBoxLayout()
        main_layout.addLayout(control_layout,1)
        main_layout.addWidget(self.__view,2)
        main_layout.addLayout(info_layout,1)

        self.setLayout(main_layout)
        self.setMinimumSize(1000,500)


        self.__update_game_view()


    def init_game(self):
        self.__engine = GOLEngine(100,100)
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
    