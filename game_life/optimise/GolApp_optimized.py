import sys
from PySide6.QtCore import Qt, QTimer, Slot, Signal
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QGroupBox,
    QScrollBar,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton
)
import numpy as np
# from GolEngine_optimized import GOLEngine
from GoLEngineNP import GOLEngine


class GameInfo:
    """Data class to hold game statistics."""
    
    def __init__(self, alive, dead, total, generation, alive_pct, dead_pct):
        self.alive = alive
        self.dead = dead
        self.total = total
        self.generation = generation
        self.alive_pct = alive_pct
        self.dead_pct = dead_pct


class QControlWidget(QGroupBox):
    """Control panel for game execution."""
    
    tick = Signal()
    
    def __init__(self, parent=None):
        super().__init__("Control", parent)
        self.__setup_ui()
        self.__timer = QTimer()
        self.__timer.timeout.connect(self.__on_tick)
    
    def __setup_ui(self):
        """Setup the control panel UI."""
        layout = QVBoxLayout()
        
        # Play/Pause button
        self.status_button = QPushButton("Play")
        self.status_button.clicked.connect(self.__toggle_play)
        
        # Step button
        step_button = QPushButton("Step")
        step_button.clicked.connect(self.__on_tick)
        
        # Speed control
        speed_layout = QHBoxLayout()
        self.speed_label = QLabel("100")
        
        self.speed_scrollbar = QScrollBar(Qt.Horizontal)
        self.speed_scrollbar.setRange(0, 500)
        self.speed_scrollbar.setValue(100)
        self.speed_scrollbar.valueChanged.connect(self.__update_speed)
        self.speed_scrollbar.valueChanged.connect(self.speed_label.setNum)
        
        speed_layout.addWidget(QLabel("Speed:"))
        speed_layout.addWidget(self.speed_scrollbar)
        speed_layout.addWidget(self.speed_label)
        
        # Add widgets to main layout
        layout.addWidget(self.status_button)
        layout.addWidget(step_button)
        layout.addLayout(speed_layout)
        
        self.setLayout(layout)
    
    def __toggle_play(self):
        """Toggle play/pause state."""
        if self.__timer.isActive():
            self.__timer.stop()
            self.status_button.setText("Play")
        else:
            timeout = 500 - self.speed_scrollbar.value()
            self.__timer.start(timeout)
            self.status_button.setText("Pause")
    
    def __on_tick(self):
        """Emit tick signal."""
        self.tick.emit()
    
    def __update_speed(self, value):
        """Update timer speed."""
        was_active = self.__timer.isActive()
        self.__timer.stop()
        if was_active:
            self.__timer.start(500 - value)


class QInfoWidget(QGroupBox):
    """Information panel displaying game statistics."""
    
    def __init__(self, parent=None):
        super().__init__("Information", parent)
        self.__setup_ui()
    
    def __setup_ui(self):
        """Setup the information panel UI."""
        layout = QVBoxLayout()
        
        self.__total_label = QLabel("Total cells: 0")
        self.__alive_label = QLabel("Alive: 0 (0.0%)")
        self.__dead_label = QLabel("Dead: 0 (0.0%)")
        self.__generation_label = QLabel("Generation: 0")
        
        layout.addWidget(self.__total_label)
        layout.addWidget(self.__alive_label)
        layout.addWidget(self.__dead_label)
        layout.addWidget(self.__generation_label)
        
        self.setLayout(layout)
    
    @Slot(GameInfo)
    def update_info(self, info):
        """Update displayed information."""
        self.__total_label.setText(f"Total cells: {info.total}")
        self.__alive_label.setText(f"Alive: {info.alive} ({info.alive_pct:.1f}%)")
        self.__dead_label.setText(f"Dead: {info.dead} ({info.dead_pct:.1f}%)")
        self.__generation_label.setText(f"Generation: {info.generation}")


class GameOfLifeApp(QWidget):
    """Main Game of Life application."""
    
    info_updated = Signal(GameInfo)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Game of Life - Optimized")
        
        # Initialize engine
        # self.__engine = GOLEngine(200, 200)
        self.__engine = GOLEngine(20, 20)
        self.__engine.randomize(0.7)
        
        self.__setup_ui()
        self.__update_game_view()
    
    def __setup_ui(self):
        """Setup the main application UI."""
        # Control panel
        control_layout = QVBoxLayout()
        self.control_widget = QControlWidget()
        self.control_widget.tick.connect(self.__update_game_view)
        
        reset_button = QPushButton("Reset")
        reset_button.clicked.connect(self.__reset_game)
        
        control_layout.addWidget(self.control_widget)
        control_layout.addWidget(reset_button)
        control_layout.addStretch(1)
        
        # Game view
        self.__view = QLabel()
        self.__view.setMinimumSize(500, 500)
        self.__view.setStyleSheet("background-color: black;")
        
        # Info panel
        info_layout = QVBoxLayout()
        info_layout.addStretch(1)
        self.info_widget = QInfoWidget()
        self.info_updated.connect(self.info_widget.update_info)
        info_layout.addWidget(self.info_widget)
        
        # Main layout
        main_layout = QHBoxLayout()
        main_layout.addLayout(control_layout, 1)
        main_layout.addWidget(self.__view, 2)
        main_layout.addLayout(info_layout, 1)
        
        self.setLayout(main_layout)
        self.setMinimumSize(1000, 500)
    
    def __reset_game(self):
        """Reset the game to a new random state."""
        self.__engine.randomize(0.7)
        self.__update_game_view()
    
    def __update_game_view(self):
        """Update the game view with optimized rendering."""
        # Create QImage with exact engine size
        img = QImage(self.__engine.width, self.__engine.height, QImage.Format_RGB32)
        img.fill(Qt.black)
        
        # Draw pixels directly (very fast)

        for x in range(self.__engine.width-1):
            for y in range(self.__engine.height - 1):
                j = x + y
                if self.__engine.cell_value(j) == 1:
                    img.setPixel(x, y, 0xFFFFFF)  # White
        
        # Scale once to view size
        scaled_img = img.scaled(
            self.__view.size(),
            Qt.KeepAspectRatio,
            Qt.FastTransformation
        )
        
        # Convert to pixmap and display
        self.__view.setPixmap(QPixmap.fromImage(scaled_img))
        
        # Process next generation
        self.__engine.process()
        
        # Update statistics
        info = GameInfo(
            self.__engine.cells_alive,
            self.__engine.cells_dead,
            self.__engine.cells_count,
            self.__engine.generation,
            self.__engine.alive_percent,
            self.__engine.dead_percent
        )
        self.info_updated.emit(info)


def main():
    """Application entry point."""
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    
    window = GameOfLifeApp()
    window.show()
    
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
