from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from ui_weather import Ui_MainWindow
from enter_location import Ui_Dialog
from urllib.parse import urlencode
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import (QLabel)
from datetime import datetime, timedelta
import json
import os
import sys
import time
import requests
from pathlib import Path
from pprint import pprint
from twilio.rest import Client

##############CREATE YOUR TWILIO ACCOUNT###############
account_sid = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth_token = 'XXXXXXXXXXXXXXXXXXXXXXX'
from_telephone='+XXXXXXXXXXXXX'
to_telephone= '+XXXXXXXXX'
#######################################################

##############CREATE OPENWEATHERMAPAPI ACCOUNT###############
OPENWEATHERMAPAPI_KEY= 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
#######################################################

searchWithBar= False
globLocationString=''
forecastTimeList=[]
forecastTempList=[]
forecastIconList=[]
innerTimeList=[]
innerTempList=[]
innerIconList=[]
forecasts_global=''


def ts_to_time_of_day(ts):
    dt = datetime.fromtimestamp(ts)
    return dt.strftime("%I%p").lstrip("0")

def getLocation():
    path= Path( "chromedriver.exe" )
    options = Options()
    options.add_argument("--use-fake-ui-for-media-stream")
    timeout = 20
    browser=webdriver.Chrome(path.absolute(),options=options)
    browser.set_window_position(150,200)
    browser.get("https://mycurrentlocation.net/")
    wait = WebDriverWait(browser, timeout)
    time.sleep(3)
    latitude = browser.find_elements_by_xpath('//*[@id="latitude"]')
    latitude = [x.text for x in latitude]
    latitude = str(latitude[0])
    longitude= browser.find_elements_by_xpath('//*[@id="longitude"]')
    longitude = [x.text for x in longitude]
    longitude = str(longitude[0])
    return(latitude,longitude)
    browser.quit()


class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.
    '''
    finished = pyqtSignal()
    error = pyqtSignal(str)
    result = pyqtSignal(dict)   #This will define a signal with two dictionary, and a slot could connect to either one


class WeatherWorker(QRunnable):
    signals = WorkerSignals()
    is_interrupted = False

    def __init__(self, location):
        super(WeatherWorker, self).__init__()
        self.location = location

    @pyqtSlot()
    def run(self):
        try:
            global searchWithLatLon

            '''
            If we are searching with automatic location
            '''

            if (searchWithLatLon==True):
                global lat,lon
                forecasts= getWeather_lat_lon(lat, lon)
                pprint(forecasts)
                if forecasts['cod'] == '400' or forecasts['cod'] == '404' :
                    raise Exception(forecasts['message'])
                client = Client(account_sid, auth_token)
                weather_string=forecasts['list'][0]['weather'][0]['description']
                quote='Happiness lies in the joy of achievement and the thrill of creative effort.'
                message = client.messages \
                .create(
                     body= "******************************\n" "Weather around you : \n" + weather_string.title() +  '\n\n'+ quote + '\n ******************************',
                    from_= from_telephone ,
                     to=to_telephone
                 )
                self.signals.result.emit(forecasts)
                searchWithLatLon=False;
                '''
                If we are searching with manual search location
                '''
            else:

                url_2 ='http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}'.format(self.location,OPENWEATHERMAPAPI_KEY)
                r = requests.get(url_2)
                weather = json.loads(r.text)
                client = Client(account_sid, auth_token)
                weather_string=weather['weather'][0]['description']
                quote='Happiness lies in the joy of achievement and the thrill of creative effort.'
                message = client.messages \
                    .create(
                         body= "******************************\n" "Weather in "+ self.location +": \n" + weather_string.title() +  '\n\n'+ quote + ' \n ******************************',
                         from_= from_telephone ,
                         to=to_telephone
                     )

                url = ' http://api.openweathermap.org/data/2.5/forecast?q={}&units=metric&appid={}'.format(self.location,OPENWEATHERMAPAPI_KEY)
                r = requests.get(url)
                forecasts=r.json()

                print('Done With Search')
                print((forecasts)['cod'])
                if forecasts['cod'] == '400' or forecasts['cod'] == '404':
                    raise Exception(forecasts['message'])
                pprint(forecasts)

                self.signals.result.emit(forecasts)


        except Exception as e:
            self.signals.error.emit(str(e))

        self.signals.finished.emit()

def getWeather_lat_lon(lat,lon):
    url_weather = ' http://api.openweathermap.org/data/2.5/forecast?lat={}&lon={}&units=metric&appid={}'.format(lat,lon,OPENWEATHERMAPAPI_KEY)
    res_weather = requests.get(url_weather)
    forecasts = res_weather.json()
    return forecasts


class MainWindow(QMainWindow, Ui_MainWindow):
    switch_window = QtCore.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.__press_pos = None
        self.setupUi(self)
        self.threadpool = QThreadPool()
        self.btn_close.clicked.connect(self.close) #customized closed and minimize buttons
        self.btn_minimize.clicked.connect(self.minimize)
        global searchWithLatLon, globLocationString
        global searchWithBar
        if searchWithLatLon==False and searchWithBar==False :
            self.Location.setText(globLocationString)
        self.update_weather()
        self.Location.returnPressed.connect(self.PressedReturn)# if Enter is pressed
        self.dateEdit.dateChanged.connect(self.checkDifference)# if Date is changed

    def checkDifference(self) :
        current_date=(QtCore.QDate.currentDate())
        dayz=(current_date).daysTo(self.dateEdit.date())
        dt=(datetime.today()+timedelta(days=dayz))
        self.WeekDay.setText(dt.strftime('%A'))
        print(dt)
        if dayz >3 or dayz <0 :
            msg='Exceeded Date Range'
            QMessageBox.warning(self, "Warning", msg)
        if dayz >= 0 :
            self.set_weather_result(dayz)

    def PressedReturn(self) :
        searchWithBar==True;
        self.update_weather()

    '''
    Deals with Frameless Window Movement
    '''
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.__press_pos = event.pos()  # remember starting position


    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.__press_pos = None


    def mouseMoveEvent(self, event):
        if self.__press_pos:  # follow the mouse
            self.move(self.pos() + (event.pos() - self.__press_pos))

    def minimize(self) :
        self.showMinimized()


    def alert(self, message):
        alert = QMessageBox.warning(self, "Warning", message)

    def update_weather(self):
        self.Location.setDisabled(True)
        Worker = WeatherWorker(self.Location.text())
        Worker.signals.result.connect(self.weather_result)
        Worker.signals.error.connect(self.alert)
        self.threadpool.start(Worker)
        self.Location.setDisabled(False)


    def weather_result(self, forecasts):
        self.Location.setText(forecasts['city']['name'])
        num=1;
        qt_date=self.dateEdit.date()
        global forecastTimeList
        global forecastIconList
        global forecastTempList
        global innerTimeList
        global innerTempList
        global innerIconList
        qtest_date=qt_date.addDays(-1)
        for n, forecast in enumerate(forecasts['list'], 1):
            if qt_date.toString('yyyy-MM-dd')==forecast['dt_txt'].split(' ')[0]  :
                innerTimeList.append(ts_to_time_of_day(forecast['dt']))
                innerTempList.append(forecast['main']['temp'])
                innerIconList.append(forecast['weather'][0])

                # print(' im here')
            elif qtest_date.toString('yyyy-MM-dd')==forecast['dt_txt'].split(' ')[0] :
                pass
            else :
                forecastTimeList.append(innerTimeList)
                forecastTempList.append(innerTempList)
                forecastIconList.append(innerIconList)
                innerTimeList=[]
                innerTempList=[]
                innerIconList=[]

                qt_date=qt_date.addDays(1)


        self.WeatherDescription.setText(forecasts['list'][0]['weather'][0]['description'].title())
        self.Humidity.setText("Humidity : %d" % (forecasts['list'][0]['main']['humidity']))
        self.sunriseLabel.setText("Sunrise : %s" % ts_to_time_of_day(forecasts['city']['sunrise']))
        self.sunsetLabel.setText("Sunset : %s" % ts_to_time_of_day(forecasts['city']['sunset']))
        self.WindLabel.setText("Wind : %.2f m/s" % forecasts['list'][0]['wind']['speed'])
        self.TemperatureLabel.setText("%.1f°C" % forecasts['list'][0]['main']['temp'])
        global forecasts_global
        forecasts_global=forecasts
        self.set_weather_result(i=0)

    def average_temp(self,l) :
        return sum(l) / len(l)

    def set_weather_result(self, i) :
        print('once')
        global innerIconList
        global innerTempList
        global innerTimeList
        global forecastIconList
        global forecastTimeList
        global forecastTempList
        '''
        Deals with the logic on printing forecasts day by day on the UI
        '''
        if(i<1) :
            j=0
            self.WeatherDescription.setText(forecasts_global['list'][0]['weather'][0]['description'].title())
            self.Humidity.setText("Humidity : %d" % (forecasts_global['list'][0]['main']['humidity']))
            self.sunriseLabel.setText("Sunrise : %s" % ts_to_time_of_day(forecasts_global['city']['sunrise']))
            self.sunsetLabel.setText("Sunset : %s" % ts_to_time_of_day(forecasts_global['city']['sunset']))
            self.WindLabel.setText("Wind : %.2f m/s" % forecasts_global['list'][0]['wind']['speed'])
            self.TemperatureLabel.setText("%.1f°C" % (self.average_temp(forecastTempList[i])))
            while j<len(forecastTimeList[i]):
                if forecastTimeList[0][j] == '2AM' or forecastTimeList[0][j] =='5AM':
                    forecastTimeList[0].pop()
                    forecastIconList[0].pop()
                    forecastTempList[0].pop()
                else :
                    # print(forecastTimeList)
                    getattr(self, 'forecastTime%d' % (j+1)).setText(forecastTimeList[i][j])
                    self.set_weather_icon(getattr(self, 'forecastIcon%d' % (j+1)), forecastIconList[i][j])
                    getattr(self, 'forecastTemp%d' % (j+1)).setText("%.1f°C" % forecastTempList[i][j])
                    j=j+1;
        else :
            j=0
            self.WeatherDescription.setText('-')
            self.Humidity.setText('Humidity : -')
            self.sunriseLabel.setText('Sunrise : -')
            self.sunsetLabel.setText('Sunset : -')
            self.WindLabel.setText('Wind : -')
            self.TemperatureLabel.setText("%.1f°C" % (self.average_temp(forecastTempList[i])))
            while j<len(forecastTimeList[i]):
                if(len(forecastTimeList[i])>6):
                    forecastTimeList[i].pop()
                    forecastIconList[i].pop()
                    forecastTempList[i].pop()
                    print(forecastTimeList)
                else :
                    getattr(self, 'forecastTime%d' % (j+1)).setText(forecastTimeList[i][j])
                    self.set_weather_icon(getattr(self, 'forecastIcon%d' % (j+1)), forecastIconList[i][j])
                    getattr(self, 'forecastTemp%d' % (j+1)).setText("%.1f°C" % forecastTempList[i][j])
                    j=j+1;


    def set_weather_icon(self, label, forecastIconList):
        label.setPixmap(
            QPixmap(os.path.join('images', "%s.png" %
                                 forecastIconList['icon']
                                 )
                    )

        )


class MainDialog(QDialog,Ui_Dialog):
    switch_window = QtCore.pyqtSignal()
    def __init__(self, *args, **kwargs):
        super(MainDialog, self).__init__(*args, **kwargs)
        self.__press_pos = None
        self.setupUi(self)
        my_file = open("cities.txt", "r")
        content=my_file.read()
        uncomplete_cities_list= content.splitlines()
        my_file.close()
        city_list = []
        for word in uncomplete_cities_list:
            word = word.split(',',1)
            city_list.append(word[0])  # <----
        completer = QCompleter(city_list)
        self.firstLocation2.setCompleter(completer)
        global searchWithLatLon
        searchWithLatLon=False
        self.checkBox.stateChanged.connect(self.clickBox)
        self.btn_close.clicked.connect(self.close)
        self.btn_minimize.clicked.connect(self.minimize)
        self.firstLocation2.returnPressed.connect(self.switch)


    def clickBox(self,state):
        if(state==QtCore.Qt.Checked):
            self.firstLocation2.setDisabled(True)
            self.firstLocation2.setText('')
            self.firstLocation2.setStyleSheet("font: 8pt \"Yu Gothic UI\";\n"
            "background-color: transparent;")
            global searchWithLatLon
            searchWithLatLon= True
            self.switch_auto_location()

    def switch_auto_location(self):
        global lat, lon
        lat, lon = getLocation()
        self.switch_window.emit()

    def switch(self):
        global globLocationString
        globLocationString=self.firstLocation2.text()
        print(globLocationString)
        self.switch_window.emit()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.__press_pos = event.pos()  # remember starting position


    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.__press_pos = None


    def mouseMoveEvent(self, event):
        if self.__press_pos:  # follow the mouse
            self.move(self.pos() + (event.pos() - self.__press_pos))

    def minimize(self) :
        self.showMinimized()

    def alert(self, message):
        alert = QMessageBox.warning(self, "Warning", message)


    '''
    Manages which window shold be displayed
    '''
class Controller:
    def __init__(self):
        pass

    def show_main_dialog(self):
        self.main_dialog= MainDialog()
        self.main_dialog.switch_window.connect(self.show_main)  #connecting a signal to self.show_main, once emit happens switching of windows will happen
        self.main_dialog.show()

    def show_main(self):
        self.window = MainWindow()
        self.main_dialog.close()
        self.window.show()

if __name__ == '__main__':

    app = QApplication([])
    controller = Controller()
    controller.show_main_dialog()
    app.exec_()
