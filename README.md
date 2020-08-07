# Weather.ly
A simplistic GUI built with the PyQt5 framework. Supports SMS weather reminders and 3 days-ahead forecasts.

Sign up a twilio account to receive a SMS reminder of the weather : 
https://www.twilio.com/try-twilio

Enter your twilio credentials and mobile number into weather.py

Sign up a OpenWeatherMapApi account and input your API key into weather.py to  retrieve free weather forecasts : 
https://openweathermap.org/api

Notes

*Make sure dependencies in requirements.txt are installed

1)Automatic Location Detection is only supported if user has a Chrome Broweser version 84 if you don't have it search city location manually

2)To use automatic location detection add full path of chromedriver.exe within the folder to PATH variable.

3)Uncomment the code for twilio after entering Twilio account credentials on line 107-114  and  129-135

4)You can edit the Location even within the MainWindow by clicking on the City Name !

If there is any issue with the application contact me by sending me an email :
zxt18@ic.ac.uk

