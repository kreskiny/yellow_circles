import sys
import io
from random import randint

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QDialog, QApplication

template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Dialog</class>
 <widget class="QDialog" name="Dialog">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>580</width>
    <height>464</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Dialog</string>
  </property>
  <widget class="QPushButton" name="pushButton">
   <property name="geometry">
    <rect>
     <x>200</x>
     <y>360</y>
     <width>141</width>
     <height>51</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <pointsize>10</pointsize>
    </font>
   </property>
   <property name="text">
    <string>Нарисовать</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class Yellow(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi(io.StringIO(template), self)
        self.pushButton.clicked.connect(self.toggle_drawing)
        self.drawing_enabled = False  # Флаг для отслеживания, нужно ли рисовать

    def toggle_drawing(self):
        self.drawing_enabled = True
        self.update()

    def paintEvent(self, event):
        self.qp = QPainter(self)
        if self.drawing_enabled:
            self.draw()
        self.qp.end()

    def draw(self):
        R = randint(20, 100)
        x = randint(0, self.width() - R)
        y = randint(0, self.height() - R)
        self.qp.setBrush(QColor(252, 237, 63))
        self.qp.drawEllipse(x, y, R, R)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Yellow()
    ex.show()
    sys.exit(app.exec_())
