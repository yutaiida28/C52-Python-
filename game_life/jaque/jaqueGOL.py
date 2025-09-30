import sys
from __feature__ import snake_case, true_property

from PySide6.QtCore import Qt, QTimer, Slot, Signal
from PySide6.QtGui import QPixmap, QPainter, QBrush, QImage
from PySide6.QtWidgets import (QApplication
                               , QWidget
                               , QLabel
                               , QGroupBox
                               , QScrollBar
                               , QHBoxLayout
                               , QVBoxLayout
                               , QPushButton)

from GolEngine import GOLEngine



class Infos():
    def __init__(self,alive,dead,total,revolution):
        self.__alive = alive
        self.__dead = dead
        self.__total = total
        self.__revolution = revolution

    @property
    def alive(self):
        return self.__alive

    @property
    def dead(self):
        return self.__dead
    
    @property
    def total(self):
        return self.__total
    
    @property
    def revolution(self):
        return self.__revolution
    
class QClockWidget(QGroupBox):

    tick = Signal()

    def __init__(self, parent = None):
        super().__init__(parent)
        main_layout = QVBoxLayout()
        self.status_button = QPushButton("Play")
        self.status_button.clicked.connect(self.switch)
        step_button = QPushButton("Step")
        step_button.clicked.connect(self.maj)

        __timeout = 100
        speed_layout = QHBoxLayout()
        speed_sb = QScrollBar(Qt.Horizontal)
        speed_sb.set_range(0,500)
        speed_sb.set_value(__timeout)
        speed_label = QLabel()
        speed_layout.add_widget(speed_sb)
        speed_sb.valueChanged.connect(speed_label.set_num)
        speed_sb.valueChanged.connect(self.update_speed)
        speed_layout.add_widget(speed_label)

        main_layout.add_widget(self.status_button)
        main_layout.add_widget(step_button)
        main_layout.add_layout(speed_layout)

        self.title ="Control"
        self.set_layout(main_layout)




        self.__timer = QTimer()
        self.__timer.timeout.connect(self.maj)

        
    def switch(self):
        if self.__timer.is_active:
            self.__timer.stop()
            self.status_button.text = "Play"
        else:
            self.__timer.start()
            self.status_button.text = "Pause"

    def maj(self):
        self.tick.emit()

    def update_speed(self, value):
        was_active = self.__timer.is_active
        self.__timer.stop()
        if was_active:
            self.__timer.start(500-value)

            
    



class QInfoWidget(QGroupBox):
    def __init__(self,parent = None):
        super().__init__(parent)
        self.title ="Informations"
        self.__layout = QVBoxLayout()

        self.__total_label = QLabel("Cells:")
        self.__alive_label = QLabel("Cells alive:")
        self.__dead_label = QLabel("Cells dead:")
        self.__revolution_lable = QLabel("Revolution:")


        self.__layout.add_widget(self.__total_label)
        self.__layout.add_widget(self.__alive_label)
        self.__layout.add_widget(self.__dead_label)
        self.__layout.add_widget(self.__revolution_lable)

        self.set_layout(self.__layout)


    @Slot(Infos)
    def update(self,values):
        self.__total_label.text = (f"Cells: {values.total}")
        self.__alive_label.text = (f"Cells alive: {values.alive}")
        self.__dead_label.text = (f"Cells dead: {values.dead}")
        self.__revolution_lable.text = (f"Revolution: {values.revolution}")


        
        

class GolAPP(QWidget):
    game_update = Signal(Infos)

    def __init__(self,parent = None):
        super().__init__(parent)

      
        self.layout_info = QVBoxLayout()

      

        self.__engine = GOLEngine(200,200)
        self.init_game()

        control_layout = QVBoxLayout()
        timer_widget = QClockWidget()
        timer_widget.tick.connect(self.__update_game_view)
        control_layout.add_widget(timer_widget)
        control_layout.add_stretch(1)

        self.__view = QLabel()

        self._info_widget = QInfoWidget()
        self.layout_info.add_stretch(1)
        self.layout_info.add_widget(self._info_widget)     

        main_layout = QHBoxLayout()
        main_layout.add_layout(control_layout,1)
        main_layout.add_widget(self.__view,2)
        main_layout.add_layout(self.layout_info,1)

        self.set_layout(main_layout)
        self.set_minimum_size = (1000, 500) 


        self.__update_game_view()
        self.game_update.connect(self._info_widget.update)

    def init_game(self):
        self.__engine.randomize(0.7)
        self.__revolution = 0

    def __update_game_view(self):
        # Créer une QImage de la taille exacte du moteur
        img = QImage(self.__engine.width, self.__engine.height, QImage.Format_RGB32)
        img.fill(Qt.black)

        # Dessiner pixel par pixel (très rapide)
        for x in range(1, self.__engine.width-1):
            for y in range(1, self.__engine.height-1):
                if self.__engine.cell_value(x, y) == 1:
                    img.set_pixel(x, y, 0xFFFFFF)  # Blanc

        # Redimensionner une seule fois
        scaled_img = img.scaled(self.__view.size, Qt.KeepAspectRatio, Qt.FastTransformation)

        # Convertir en pixmap et afficher
        self.__view.pixmap = QPixmap.from_image(scaled_img)  


        self.__revolution += 1

        self.__engine.process()

        self.game_update.emit(self.game_info)

    @property
    def game_info(self):
        alive = self.__engine.cells_alive
        dead = self.__engine.cells_dead
        total = self.__engine.cells_count
        rev = self.__revolution
        return Infos(alive,dead,total,rev)



        
        




def main():
    app = QApplication(sys.argv)
    app.set_style("Fusion")
    g = GolAPP()
    g.show()

    sys.exit(app.exec())




    pass




if __name__ == '__main__':
    main()
    