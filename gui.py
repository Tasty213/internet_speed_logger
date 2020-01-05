#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 12:03:56 2019

@author: tasty
"""
print('importing')
from grapher import networkData
from PyQt5.QtWidgets import QApplication, QLabel, QComboBox, QWidget, QVBoxLayout
from PyQt5.QtCore import QCoreApplication
import sys

print('initialising')
app = QApplication([])
print('initialised app')
data = networkData()
print('initialised data')
window = QWidget()
print('initialised window')
print('program initialised')
print('setting layout')
layout = QVBoxLayout()

layout.addWidget(QLabel('Program to graph network speeds and ping times'))
print('Added label')

QComboBox()
ssids = QComboBox()
ssids.addItems(data.ssids)
layout.addWidget(ssids)

metrics = QComboBox()
metrics.addItems(data.data[data.ssids[0]].columns)
layout.addWidget(metrics)

window.setLayout(layout)
window.show()

app.exec_()


data = networkData()
data.plotter(data.ssids[1])
