#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 12:03:56 2019

@author: tasty
"""
from grapher import networkData
from PyQt5.QtWidgets import QApplication, QLabel, QComboBox, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtCore import QCoreApplication
import sys

verbose = False
for i in range(1, len(sys.argv)):
    current = sys.argv[i]
    if current == "-v" or current == "--verbose":
        verbose = True
    else:
        print("Flag not recognised: ", sys.argv[i])

if verbose:
    print('initialising')
app = QApplication([])
if verbose:
    print('initialised app')
data = networkData()
if verbose:
    print('initialised data')
window = QWidget()
if verbose:
    print('initialised window')
    print('program initialised')
    print('setting layout')
layout = QVBoxLayout()

layout.addWidget(QLabel('Program to graph network speeds and ping times'))
if verbose:
    print('Added label')

QComboBox()
ssids = QComboBox()
ssids.addItems(data.ssids)
layout.addWidget(ssids)

metrics = QComboBox()
metrics.addItems(data.data[data.ssids[0]].columns)
layout.addWidget(metrics)

button = QPushButton('PyQt5 button')
layout.addWidget(button)

window.setLayout(layout)
window.show()

app.exec_()


data = networkData()
data.plotter(data.ssids[1])
