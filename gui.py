#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 12:03:56 2019

@author: tasty
"""
from grapher import networkData
from PyQt5.QtWidgets import QApplication, QLabel, QComboBox, QWidget, QGridLayout, QPushButton
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon, QPixmap
import sys
from os.path import exists

data = networkData()

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Network Speed Grapher'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
        self.initUI()

    def initUI(self):
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.ssid_selector = QComboBox()
        self.ssid_selector.addItems(data.ssids)
        self.grid.addWidget(self.ssid_selector, 0, 0)

        self.metrics = QComboBox()
        self.metrics.addItems(data.data[data.ssids[0]].columns)
        self.grid.addWidget(self.metrics, 1, 0)

        display_graph = QPushButton('Display graph', self)
        display_graph.setToolTip('Displays the graph selected')
        display_graph.clicked.connect(self.display)
        self.grid.addWidget(display_graph, 2, 0)

        save_graph = QPushButton('Save curently displayed graph', self)
        save_graph.setToolTip('Saves the graph currently displayed to the right')
        save_graph.clicked.connect(self.save)
        self.grid.addWidget(save_graph, 3, 0)

        self.show()

    @pyqtSlot()
    def display(self):
        print("button clicked")
        print(self.ssid_selector.currentText())
        data.plotter(self.ssid_selector.currentText(),
                    self.metrics.currentText())

        while not exists('.temp_display.png'):
            print('no image ready')

        # Create widget
        label = QLabel(self)
        pixmap = QPixmap('.temp_display.png')
        label.setPixmap(pixmap)
        self.resize(pixmap.width(),pixmap.height())
        self.grid.addWidget(label, 0, 1, 4, 1)

    @pyqtSlot()
    def save(self):
        pass



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
