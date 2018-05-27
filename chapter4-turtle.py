import turtle
import sys
from PySide.QtCore import *
from PySide.QtGui import *


class TurtleControl(QWidget):  # inherit from Qt class,satisfy all basic requirements.
    def __init__(self, turtle):
        super(TurtleControl, self).__init__()
        self.turtle = turtle
        # 3 buttons and 1 int spin box
        self.left_btn = QPushButton("Left", self)
        self.right_btn = QPushButton("Right", self)
        self.move_btn = QPushButton("Move", self)
        self.distance_spin = QSpinBox()
        self.color_r_spin = QSpinBox()
        self.color_g_spin = QSpinBox()
        self.color_b_spin = QSpinBox()
        self.color_btn = QPushButton("C_Color", self)
        self.color_dialog_btn = QPushButton("Color", self)  # complete exercise 2
        # add a layout,type: QGridLayout
        self.controlsLayout = QGridLayout()
        self.controlsLayout.addWidget(self.left_btn, 0, 0)
        self.controlsLayout.addWidget(self.right_btn, 0, 1)
        self.controlsLayout.addWidget(self.distance_spin, 1, 0)
        self.controlsLayout.addWidget(self.move_btn, 1, 1)
        self.controlsLayout.addWidget(self.color_r_spin, 2, 0)
        self.controlsLayout.addWidget(self.color_g_spin, 2, 1)
        self.controlsLayout.addWidget(self.color_b_spin, 3, 0)
        self.controlsLayout.addWidget(self.color_btn, 3, 1)
        self.controlsLayout.addWidget(self.color_dialog_btn, 4, 0)  # complete exercise 2
        # after add all widgets to layout, we can use it by setLayout
        self.setLayout(self.controlsLayout)

        self.distance_spin.setRange(0, 100)
        self.distance_spin.setSingleStep(5)
        self.distance_spin.setValue(20)

        self.color_r_spin.setRange(0, 255)
        self.color_r_spin.setSingleStep(5)
        self.color_r_spin.setValue(0)
        self.color_g_spin.setRange(0, 255)
        self.color_g_spin.setSingleStep(5)
        self.color_g_spin.setValue(0)
        self.color_b_spin.setRange(0, 255)
        self.color_b_spin.setSingleStep(5)
        self.color_b_spin.setValue(0)

        # connect a corresponding method to click event
        self.move_btn.clicked.connect(self.move_turtle)
        self.right_btn.clicked.connect(self.turn_turtle_right)
        self.left_btn.clicked.connect(self.turn_turtle_left)
        self.color_btn.clicked.connect(self.change_color)
        self.color_dialog_btn.clicked.connect(self.change_t_color)  # complete exercise 2

    def turn_turtle_left(self):
        self.turtle.left(45)

    def turn_turtle_right(self):
        self.turtle.right(45)

    def move_turtle(self):
        self.turtle.forward(self.distance_spin.value())

    def change_color(self):
        self.turtle.color(self.color_r_spin.value(), self.color_g_spin.value(), self.color_b_spin.value())

    def change_t_color(self):  # complete exercise 2
        self.turtle.color(QColorDialog.getColor().getRgb()[:3])


# setup turtle
window = turtle.Screen()
babbage = turtle.Turtle()
window.colormode(255)

# Create a Qt application
app = QApplication(sys.argv)
control_window = TurtleControl(babbage)
control_window.show()

# Enter Qt application main loop
app.exec_()
sys.exit()
