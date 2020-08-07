# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'color_test.ui.txt'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QLabel)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(870, 468)
        MainWindow.setMinimumSize(QtCore.QSize(865, 468))
        MainWindow.setMinimumSize(QtCore.QSize(865, 468))
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.drop_shadow_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.drop_shadow_layout.setContentsMargins(0, 0, 0, 0)
        self.drop_shadow_layout.setSpacing(0)
        self.drop_shadow_layout.setObjectName("drop_shadow_layout")
        self.drop_shadow_frame = QtWidgets.QFrame(self.centralwidget)
        self.drop_shadow_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 89, 214, 1) stop:0.591368 rgba(30, 29, 95, 250));")
        self.drop_shadow_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.drop_shadow_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.drop_shadow_frame.setObjectName("drop_shadow_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.drop_shadow_frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title_bar = QtWidgets.QFrame(self.drop_shadow_frame)
        self.title_bar.setMaximumSize(QtCore.QSize(16777215, 50))
        self.title_bar.setStyleSheet("background-color: none;\n"
"border: none;\n"
"background: none;\n"
"\n"
"\n"
"QFrame::down-button {\n"
"    border: none;\n"
"    background: none;\n"
"}\n"
"")
        self.title_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.title_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title_bar.setObjectName("title_bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.title_bar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtWidgets.QFrame(self.title_bar)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.lbl = QtWidgets.QLabel(self.frame_2)
        self.lbl.setStyleSheet("background-color: transparent;"
                               "color: rgb(255,255,255);"
                               "font: bold italic 20pt 'Times New Roman';")

        self.lbl.setGeometry(0, 0, 971, 31)
        self.frame_btns = QtWidgets.QFrame(self.frame_2)
        self.frame_btns.setGeometry(QtCore.QRect(790, 0, 70, 50))
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
        self.dateEdit = QtWidgets.QDateEdit(self.frame_2)
        self.dateEdit.setGeometry(QtCore.QRect(580, 20, 125, 30))
        self.dateEdit.setStyleSheet("QDateEdit\n"
"{\n"
"\n"
"    background-color : transparent;\n"
"    border-width: 4px;\n"
"    font:  11pt \"Yu Gothic UI \";\n"
"    color: white;\n"
"    spacing: 5px; \n"
"}\n"
"\n"
"QDateEdit::up-button {\n"
"}\n"
"\n"
"QDateEdit::down-button {\n"
"}\n"
"\n"
"")
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setWrapping(True)
        self.WeekDay = QtWidgets.QLineEdit(self.frame_2)
        self.WeekDay.setGeometry(QtCore.QRect(340, 19, 160, 30))
        self.WeekDay.setAlignment(QtCore.Qt.AlignCenter)
        self.WeekDay.setStyleSheet("background-color : transparent;\n"
"    \n"
"    font: 11pt \"Yu Gothic UI Bold\";\n"
"    color : rgb(255, 255, 255);\n"
"    \n"
"")
        self.WeekDay.setObjectName("WeekDay")
        self.WeekDay.setDisabled(True)
        self.Location = QtWidgets.QLineEdit(self.frame_2)
        self.Location.setGeometry(QtCore.QRect(2, 0, 400, 51))
        self.Location.setAlignment(QtCore.Qt.AlignCenter)
        self.Location.setStyleSheet("background-color : transparent;\n"
"    \n"
"    font: 18pt \"Yu Gothic UI\";\n"
"    color : rgb(255, 255, 255);\n"
"    \n"
"")
        self.Location.setObjectName("Location")
        self.horizontalLayout.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.title_bar)
        self.content_bar = QtWidgets.QFrame(self.drop_shadow_frame)
        self.content_bar.setMinimumSize(QtCore.QSize(0, 313))
        self.content_bar.setStyleSheet("background-color: none;")
        self.content_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.content_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content_bar.setObjectName("content_bar")
        self.frame = QtWidgets.QFrame(self.content_bar)
        self.frame.setGeometry(QtCore.QRect(10, 140, 841, 391))
        self.frame.setStyleSheet("QLabel {    \n"
"\n"
"    \n"
"    font: 14pt \"Yu Gothic UI\";\n"
"    color : rgb(255, 255, 255)\n"
"    \n"
"    \n"
"\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 10, 831, 213))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.forecastTime1 = QtWidgets.QLabel(self.layoutWidget)
        self.forecastTime1.setAlignment(QtCore.Qt.AlignCenter)
        self.forecastTime1.setObjectName("forecastTime1")
        self.gridLayout_2.addWidget(self.forecastTime1, 0, 0, 1, 1)

        self.forecastTime3 = QtWidgets.QLabel(self.layoutWidget)
        self.forecastTime3.setAlignment(QtCore.Qt.AlignCenter)
        self.forecastTime3.setObjectName("forecastTime3")
        self.gridLayout_2.addWidget(self.forecastTime3, 0, 2, 1, 1)
        self.forecastTime2 = QtWidgets.QLabel(self.layoutWidget)
        self.forecastTime2.setAlignment(QtCore.Qt.AlignCenter)
        self.forecastTime2.setObjectName("forecastTime2")
        self.gridLayout_2.addWidget(self.forecastTime2, 0, 1, 1, 1)
        self.forecastTemp6 = QtWidgets.QLabel(self.layoutWidget)
        self.forecastTemp6.setAlignment(QtCore.Qt.AlignCenter)
        self.forecastTemp6.setObjectName("forecastTemp6")
        self.gridLayout_2.addWidget(self.forecastTemp6, 2, 5, 1, 1)
        self.forecastTemp5 = QtWidgets.QLabel(self.layoutWidget)
        self.forecastTemp5.setAlignment(QtCore.Qt.AlignCenter)
        self.forecastTemp5.setObjectName("forecastTemp5")
        self.gridLayout_2.addWidget(self.forecastTemp5, 2, 4, 1, 1)
        self.forecastTemp4 = QtWidgets.QLabel(self.layoutWidget)
        self.forecastTemp4.setAlignment(QtCore.Qt.AlignCenter)
        self.forecastTemp4.setObjectName("forecastTemp4")
        self.gridLayout_2.addWidget(self.forecastTemp4, 2, 3, 1, 1)
        self.forecastTemp3 = QtWidgets.QLabel(self.layoutWidget)
        self.forecastTemp3.setAlignment(QtCore.Qt.AlignCenter)
        self.forecastTemp3.setObjectName("forecastTemp3")
        self.gridLayout_2.addWidget(self.forecastTemp3, 2, 2, 1, 1)
        self.forecastTemp2 = QtWidgets.QLabel(self.layoutWidget)
        self.forecastTemp2.setAlignment(QtCore.Qt.AlignCenter)
        self.forecastTemp2.setObjectName("forecastTemp2")
        self.gridLayout_2.addWidget(self.forecastTemp2, 2, 1, 1, 1)
        self.forecastIcon4 = QtWidgets.QLabel(self.layoutWidget)
        self.forecastIcon4.setText("")
        self.forecastIcon4.setPixmap(QtGui.QPixmap("images/tstorms.png"))
        self.forecastIcon4.setObjectName("forecastIcon4")
        self.gridLayout_2.addWidget(self.forecastIcon4, 1, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.forecastIcon5 = QtWidgets.QLabel(self.layoutWidget)
        self.forecastIcon5.setText("")
        self.forecastIcon5.setPixmap(QtGui.QPixmap("images/cloudy.png"))
        self.forecastIcon5.setObjectName("forecastIcon5")
        self.gridLayout_2.addWidget(self.forecastIcon5, 1, 4, 1, 1, QtCore.Qt.AlignHCenter)
        self.forecastIcon6 = QtWidgets.QLabel(self.layoutWidget)
        self.forecastIcon6.setText("")
        self.forecastIcon6.setPixmap(QtGui.QPixmap("images/cloudy.png"))
        self.forecastIcon6.setObjectName("forecastIcon6")
        self.gridLayout_2.addWidget(self.forecastIcon6, 1, 5, 1, 1, QtCore.Qt.AlignHCenter)
        self.forecastIcon1 = QtWidgets.QLabel(self.layoutWidget)
        self.forecastIcon1.setText("")
        self.forecastIcon1.setPixmap(QtGui.QPixmap("images/rain.png"))
        self.forecastIcon1.setObjectName("forecastIcon1")
        self.gridLayout_2.addWidget(self.forecastIcon1, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.forecastIcon2 = QtWidgets.QLabel(self.layoutWidget)
        self.forecastIcon2.setText("")
        self.forecastIcon2.setPixmap(QtGui.QPixmap("images/snow.png"))
        self.forecastIcon2.setObjectName("forecastIcon2")
        self.gridLayout_2.addWidget(self.forecastIcon2, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.forecastIcon3 = QtWidgets.QLabel(self.layoutWidget)
        self.forecastIcon3.setText("")
        self.forecastIcon3.setPixmap(QtGui.QPixmap("images/snow.png"))
        self.forecastIcon3.setObjectName("forecastIcon3")
        self.gridLayout_2.addWidget(self.forecastIcon3, 1, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.forecastTime4 = QtWidgets.QLabel(self.layoutWidget)
        self.forecastTime4.setAlignment(QtCore.Qt.AlignCenter)
        self.forecastTime4.setObjectName("forecastTime4")
        self.gridLayout_2.addWidget(self.forecastTime4, 0, 3, 1, 1)
        self.forecastTime5 = QtWidgets.QLabel(self.layoutWidget)
        self.forecastTime5.setAlignment(QtCore.Qt.AlignCenter)
        self.forecastTime5.setObjectName("forecastTime5")
        self.gridLayout_2.addWidget(self.forecastTime5, 0, 4, 1, 1)
        self.forecastTime6 = QtWidgets.QLabel(self.layoutWidget)
        self.forecastTime6.setAlignment(QtCore.Qt.AlignCenter)
        self.forecastTime6.setObjectName("forecastTime5")
        self.gridLayout_2.addWidget(self.forecastTime6, 0, 5, 1, 1)
        self.forecastTemp1 = QtWidgets.QLabel(self.layoutWidget)
        self.forecastTemp1.setEnabled(False)
        self.forecastTemp1.setAlignment(QtCore.Qt.AlignCenter)
        self.forecastTemp1.setObjectName("forecastTemp1")
        self.gridLayout_2.addWidget(self.forecastTemp1, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.content_bar)
        self.label.setGeometry(QtCore.QRect(20, 10, 811, 121))
        self.label.setStyleSheet("QLabel {    \n"
"\n"
"    \n"
"    font: 14pt \"Yu Gothic UI\";\n"
"    color : rgb(255, 255, 255)\n"
"    \n"
"    \n"
"\n"
"}")
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.gridLayoutWidget = QtWidgets.QWidget(self.content_bar)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(385, 10, 401, 131))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Humidity = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Humidity.setObjectName("Humidity")
        self.gridLayout.addWidget(self.Humidity, 1, 1, 1, 1)
        self.sunriseLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.sunriseLabel.setObjectName("sunriseLabel")
        self.gridLayout.addWidget(self.sunriseLabel, 0, 0, 1, 1)
        self.sunsetLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.sunsetLabel.setObjectName("sunsetLabel")
        self.gridLayout.addWidget(self.sunsetLabel, 0, 1, 1, 1)
        self.WindLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.WindLabel.setObjectName("WindLabel")
        self.gridLayout.addWidget(self.WindLabel, 1, 0, 1, 1)
        self.gridLayoutWidget.setStyleSheet("background-color : transparent;\n"
"    font: 12pt \"Yu Gothic UI\";\n"
"    color : rgb(255, 255, 255);\n"
"    \n"
"")
        self.WeatherDescription = QtWidgets.QLabel(self.content_bar)
        self.WeatherDescription.setGeometry(QtCore.QRect(95, 50, 230, 101))
        self.WeatherDescription.setStyleSheet("background-color : transparent;\n"
"    \n"
"    font: 17pt \"Yu Gothic UI\";\n"
"    color : rgb(255, 255, 255);\n"
"    \n"
"")
        self.WeatherDescription.setAlignment(QtCore.Qt.AlignCenter)
        self.WeatherDescription.setObjectName("WeatherDescription")
        self.TemperatureLabel= QtWidgets.QLabel(self.content_bar)
        self.TemperatureLabel.setGeometry(QtCore.QRect(120, 10, 165, 51))
        self.TemperatureLabel.setStyleSheet("background-color : transparent;\n"
"    \n"
"    font: 32pt \"Yu Gothic UI\";\n"
"    color : rgb(255, 255, 255);\n"
"    \n"
"")
        self.TemperatureLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.TemperatureLabel.setObjectName("TemperatureLabel")
        self.verticalLayout.addWidget(self.content_bar)
        self.credits_bar = QtWidgets.QFrame(self.drop_shadow_frame)
        self.credits_bar.setMaximumSize(QtCore.QSize(16777215, 30))
        self.credits_bar.setStyleSheet("background-color: rgb(33, 33, 75);")
        self.credits_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.credits_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.credits_bar.setObjectName("credits_bar")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.credits_bar)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_label_credits = QtWidgets.QFrame(self.credits_bar)
        self.frame_label_credits.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_label_credits.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_label_credits.setObjectName("frame_label_credits")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_label_credits)
        self.verticalLayout_3.setContentsMargins(15, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_credits = QtWidgets.QLabel(self.frame_label_credits)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.label_credits.setFont(font)
        self.label_credits.setStyleSheet("color: rgb(128, 102, 168);")
        self.label_credits.setObjectName("label_credits")
        self.verticalLayout_3.addWidget(self.label_credits)
        self.horizontalLayout_2.addWidget(self.frame_label_credits)
        self.frame_grip = QtWidgets.QFrame(self.credits_bar)
        self.frame_grip.setMinimumSize(QtCore.QSize(30, 30))
        self.frame_grip.setMaximumSize(QtCore.QSize(30, 30))
        self.frame_grip.setStyleSheet("padding: 5px;")
        self.frame_grip.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_grip.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_grip.setObjectName("frame_grip")
        self.horizontalLayout_2.addWidget(self.frame_grip)
        self.verticalLayout.addWidget(self.credits_bar)
        self.drop_shadow_layout.addWidget(self.drop_shadow_frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.WeekDay.setText(datetime.today().strftime('%A'))
        self.btn_minimize.setToolTip(_translate("MainWindow", "Minimize"))
        self.btn_close.setToolTip(_translate("MainWindow", "Close"))
        self.Location.setText(_translate("MainWindow", "Kuala Lumpur Malaysia"))
        self.forecastTime1.setText(_translate("MainWindow", "-- "))
        self.forecastTime2.setText(_translate("MainWindow", "-- "))
        self.forecastTime3.setText(_translate("MainWindow", "-- "))
        self.forecastTime4.setText(_translate("MainWindow", "-- "))
        self.forecastTime5.setText(_translate("MainWindow", "-- "))
        self.forecastTime6.setText(_translate("MainWindow", "-- "))
        self.forecastTemp1.setText(_translate("MainWindow", "--°C"))
        self.forecastTemp2.setText(_translate("MainWindow", "--°C"))
        self.forecastTemp3.setText(_translate("MainWindow", "--°C"))
        self.forecastTemp4.setText(_translate("MainWindow", "--°C "))
        self.forecastTemp5.setText(_translate("MainWindow", "--°C"))
        self.forecastTemp6.setText(_translate("MainWindow", "--°C"))
        self.Humidity.setText(_translate("MainWindow", "Humidity"))
        self.sunriseLabel.setText(_translate("MainWindow", "TextLabel"))
        self.sunsetLabel.setText(_translate("MainWindow", "TextLabel"))
        self.WindLabel.setText(_translate("MainWindow", "TextLabel"))
        self.WeatherDescription.setText(_translate("MainWindow", "Thunderstorms"))
        self.TemperatureLabel.setText(_translate("MainWindow", "32 °C"))
        self.label_credits.setText(_translate("MainWindow", "By: Zhang Xhin Tan"))
