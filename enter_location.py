# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'enter_location.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QCompleter
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(574, 302)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(-10, -10, 931, 500))
        self.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 89, 214, 1) stop:0.591368 rgba(30, 29, 90, 255));")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.firstLocation2 = QtWidgets.QLineEdit(self.frame)
        self.firstLocation2.setGeometry(QtCore.QRect(110, 210, 401, 22))
        self.firstLocation2.setStyleSheet("font: 8pt \"Yu Gothic UI\";\n"
"background-color: rgb(255, 255, 255);")
        self.firstLocation2.setObjectName("firstLocation2")
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setGeometry(QtCore.QRect(110, 250, 300, 20))
        self.checkBox.setStyleSheet("background-color : transparent;\n"
"font: 8pt \"Yu Gothic UI\";\n"
"color: rgb(255, 255, 255);")
        self.checkBox.setObjectName("checkBox")
        self.Logo = QtWidgets.QLabel(self.frame)
        self.Logo.setGeometry(QtCore.QRect(30, 210, 71, 21))
        self.Logo.setStyleSheet("background-color : transparent;\n"
"font: 10pt \"Yu Gothic UI\";\n"
"color: rgb(255, 255, 255);")
        self.Logo.setObjectName("Logo")
        self.weather_ly = QtWidgets.QLabel(self.frame)
        self.weather_ly.setGeometry(QtCore.QRect(0, 20, 581, 141))
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic Semilight")
        font.setPointSize(36)
        self.weather_ly.setFont(font)
        self.weather_ly.setStyleSheet("background-color: transparent;\n"
"color: rgb(85, 255, 127);\n"
"")
        self.weather_ly.setAlignment(QtCore.Qt.AlignCenter)
        self.weather_ly.setWordWrap(False)
        self.weather_ly.setObjectName("weather_ly")
        self.plan_ahead = QtWidgets.QLabel(self.frame)
        self.plan_ahead.setGeometry(QtCore.QRect(120, 120, 331, 71))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(20)
        self.plan_ahead.setFont(font)
        self.plan_ahead.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.plan_ahead.setStyleSheet("background-color: transparent;\n"
"color:white\n"
"")
        self.plan_ahead.setAlignment(QtCore.Qt.AlignCenter)
        self.plan_ahead.setObjectName("plan_ahead")
        self.frame_btns = QtWidgets.QFrame(Dialog)
        self.frame_btns.setGeometry(QtCore.QRect(505, 0, 65, 50))
        self.frame_btns.setMaximumSize(QtCore.QSize(100, 16777215))
        self.frame_btns.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_btns.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_btns.setObjectName("frame_btns")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_btns)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_minimize = QtWidgets.QPushButton(self.frame_btns)
        self.btn_minimize.setMinimumSize(QtCore.QSize(16, 16))
        self.btn_minimize.setMaximumSize(QtCore.QSize(17, 17))
        self.btn_minimize.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    border-radius: 8px;    \n"
"    background-color: rgb(85, 255, 127);\n"
"}\n"
"QPushButton:hover {    \n"
"    background-color: rgba(85, 255, 127, 150);\n"
"}")
        self.btn_minimize.setText("")
        self.btn_minimize.setObjectName("btn_minimize")
        self.horizontalLayout_3.addWidget(self.btn_minimize)
        self.btn_close = QtWidgets.QPushButton(self.frame_btns)
        self.btn_close.setMinimumSize(QtCore.QSize(16, 16))
        self.btn_close.setMaximumSize(QtCore.QSize(17, 17))
        self.btn_close.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    border-radius: 8px;        \n"
"    background-color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:hover {        \n"
"    background-color: rgba(255, 0, 0, 150);\n"
"}")
        self.btn_close.setText("")
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout_3.addWidget(self.btn_close)


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.show()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.checkBox.setText(_translate("Dialog", "Automatically Find Your Location"))
        self.Logo.setText(_translate("Dialog", "City:"))
        self.weather_ly.setText(_translate("Dialog", "Weather.ly"))
        self.plan_ahead.setText(_translate("Dialog", "Plan Ahead"))
