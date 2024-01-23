"""OLD VERSION
from tabulate import tabulate

def print_table_info(data):
    sorted_data = sorted(data, key=lambda x: x['city'])
    headers = sorted_data[0].keys()
    table = tabulate([item.values() for item in sorted_data], headers=headers, tablefmt='grid')
    print(table)
    
    """

import sys
from PyQt5 import QtWidgets, QtCore
import weatherScraper.gui.gui_converted_file as gui_converted_file

from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, Float, DateTime, desc, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Assuming you have a City model mapped to your database
Base = declarative_base()

class City(Base):
    __tablename__ = 'City'
    CityID = Column(Integer, primary_key=True, autoincrement=True)
    CityName = Column(String)
    weather = relationship('Weather', back_populates='city')

class Weather(Base):
    __tablename__ = 'Weather'
    WeatherID = Column(Integer, primary_key=True, autoincrement=True)
    CityID = Column(Integer, ForeignKey('City.CityID'))
    CurrentTemperature = Column(Float)
    CurrentWind = Column(Float)
    Timestamp = Column(DateTime)
    city = relationship('City', back_populates='weather')
    day_info = relationship('Day', back_populates='weather')

class Day(Base):
    __tablename__ = 'Day_Info'
    DayID = Column(Integer, primary_key=True, autoincrement=True)
    WeatherID = Column(Integer, ForeignKey('Weather.WeatherID'))
    Date = Column(DateTime)
    MaxTemp = Column(Float)
    MinTemp = Column(Float)
    Rain = Column(Integer)
    Snow = Column(Integer)
    Sunrise = Column(DateTime)
    Sunset = Column(DateTime)
    weather = relationship('Weather', back_populates='day_info')
    timelapse = relationship('Timelapse', back_populates='day_info')

class Timelapse(Base):
    __tablename__ = 'Timelapse'
    TimelapseID = Column(Integer, primary_key=True, autoincrement=True)
    DayID = Column(Integer, ForeignKey('Day_Info.DayID'))
    Date = Column(DateTime)
    H00 = Column(String)
    H02 = Column(String)
    H04 = Column(String)
    H06 = Column(String)
    H08 = Column(String)
    H10 = Column(String)
    H12 = Column(String)
    H14 = Column(String)
    H16 = Column(String)
    H18 = Column(String)
    H20 = Column(String)
    H22 = Column(String)
    day_info = relationship('Day', back_populates='timelapse')

class MyWindow(QtWidgets.QMainWindow, gui_converted_file.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_database()

        self.populate_combo_box()
        self.update_date_labels()
        self.comboBox.currentIndexChanged.connect(self.update_weather_labels)
        self.update_ui_for_selected_city()
        self.translator = QtCore.QTranslator()
        
    def init_database(self):
        engine = create_engine('access+pyodbc:///?odbc_connect=DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:/Documentos/VSCODE/Python/Weather Web Scraper/weatherScraper/weather_database.accdb;')  # Replace with your actual database file
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()
        
    def populate_combo_box(self):
        city_names = [city.CityName for city in self.session.query(City).all()]
        self.comboBox.clear()
        self.comboBox.addItems(city_names)

    def update_date_labels(self):
        current_date = QtCore.QDate.currentDate()
        self.label_8.setText(current_date.toString(QtCore.Qt.DefaultLocaleLongDate))
        tomorrow_date = current_date.addDays(1)
        self.label_9.setText(tomorrow_date.toString(QtCore.Qt.DefaultLocaleLongDate))

    def update_weather_labels(self):
        selected_city = self.comboBox.currentText()
        weather_info = self.get_weather_info(selected_city)
        _translate = QtCore.QCoreApplication.translate
        #text for hours:
        self.label_5.setText(_translate("MyWindow", weather_info.get("th08", "")))
        self.label_10.setText(_translate("MyWindow", weather_info.get("t2h08", "")))
        self.label_19.setText(_translate("MyWindow", weather_info.get("t2h12", "")))
        self.label_20.setText(_translate("MyWindow", weather_info.get("th12", "")))
        self.label_23.setText(_translate("MyWindow", weather_info.get("th16", "")))
        self.label_24.setText(_translate("MyWindow", weather_info.get("t2h16", "")))
        self.label_21.setText(_translate("MyWindow", weather_info.get("t2h20", "")))
        self.label_22.setText(_translate("MyWindow", weather_info.get("th20", "")))
        #additional information
        self.label_27.setText(_translate("MyWindow", str(weather_info.get("train", ""))))
        self.label_28.setText(_translate("MyWindow", str(weather_info.get("t2rain", ""))))
        self.label_25.setText(_translate("MyWindow", str(weather_info.get("t2snow", ""))))
        self.label_26.setText(_translate("MyWindow", str(weather_info.get("tsnow", ""))))
        self.label_29.setText(_translate("MyWindow", str(weather_info.get("twind", ""))))
        self.label_30.setText(_translate("MyWindow", str(weather_info.get("t2wind", ""))))
        self.label_31.setText(_translate("MyWindow", str(weather_info.get("t2sunrise", ""))))
        self.label_32.setText(_translate("MyWindow", str(weather_info.get("tsunrise", ""))))
        self.label_33.setText(_translate("MyWindow", str(weather_info.get("t2sunset", ""))))
        self.label_34.setText(_translate("MyWindow", str(weather_info.get("tsunset", ""))))
        self.label_36.setText(_translate("MyWindow", str(weather_info.get("tmaxtemp", ""))))
        self.label_37.setText(_translate("MyWindow", str(weather_info.get("t2maxtemp", ""))))
        self.label_39.setText(_translate("MyWindow", str(weather_info.get("tmintemp", ""))))
        self.label_40.setText(_translate("MyWindow", str(weather_info.get("t2mintemp", ""))))
        
    def get_weather_info(self, city_name):
        city = self.session.query(City).filter_by(CityName=city_name).first()
        if city:
            weather = self.session.query(Weather).filter_by(CityID=city.CityID).order_by(Weather.Timestamp.desc()).first()
            if weather:
                today_info = self.session.query(Day).filter_by(WeatherID=weather.WeatherID).order_by(Day.DayID).first()
                today_info_dayID = today_info.DayID
                tomorrow_info_dayID = today_info_dayID +1
                tomorrow_info = self.session.query(Day).filter_by(WeatherID=weather.WeatherID, DayID = tomorrow_info_dayID).first()
                today_timelapse = self.session.query(Timelapse).filter_by(DayID=today_info.DayID).first()
                tomorrow_timelapse = self.session.query(Timelapse).filter_by(DayID=tomorrow_info.DayID).first()

                if today_info and tomorrow_info:
                    return {
                        "th08": today_timelapse.H08,
                        "t2h08": tomorrow_timelapse.H08,
                        "th12": today_timelapse.H12,
                        "t2h12": tomorrow_timelapse.H12,
                        "th16": today_timelapse.H16,
                        "t2h16": tomorrow_timelapse.H16,
                        "th20": today_timelapse.H20,
                        "t2h20": tomorrow_timelapse.H20,
                        
                        "tmaxtemp": today_info.MaxTemp,
                        "t2maxtemp": tomorrow_info.MaxTemp,
                        "tmintemp": today_info.MinTemp,
                        "t2mintemp": tomorrow_info.MinTemp,
                        "train": today_info.Rain,
                        "t2rain": tomorrow_info.Rain,
                        "tsnow": today_info.Snow,
                        "t2snow": tomorrow_info.Snow,
                        "twind": weather.CurrentWind,
                        "t2wind": "Not enough information",
                        "tsunrise": today_info.Sunrise.strftime("%H:%M:%S"),
                        "t2sunrise": tomorrow_info.Sunrise.strftime("%H:%M:%S"),
                        "tsunset": today_info.Sunset.strftime("%H:%M:%S"),
                        "t2sunset": tomorrow_info.Sunset.strftime("%H:%M:%S"),
                    }
        return {}
    
    def update_ui_for_selected_city(self):
        selected_city = self.comboBox.currentText()
        self.get_weather_info(selected_city)
        self.update_weather_labels()

    def retranslateUi(self, MyWindow):
        _translate = QtCore.QCoreApplication.translate
        MyWindow.setWindowTitle(_translate("MyWindow", "MyWindow"))

        self.label_4.setText(_translate("MyWindow", "TODAY"))
        self.label_6.setText(_translate("MyWindow", "TOMORROW"))
        self.label_3.setText(_translate("MyWindow", "08:00"))
        self.label_11.setText(_translate("MyWindow", "12:00"))
        self.label_12.setText(_translate("MyWindow", "16:00"))
        self.label_13.setText(_translate("MyWindow", "20:00"))
        self.label_14.setText(_translate("MyWindow", "RAIN"))
        self.label_15.setText(_translate("MyWindow", "SNOW"))
        self.label_16.setText(_translate("MyWindow", "WIND"))
        self.label_17.setText(_translate("MyWindow", "SUNRISE"))
        self.label_18.setText(_translate("MyWindow", "SUNSET"))
        self.label_35.setText(_translate("MyWindow", "MAX TEMP"))
        self.label_38.setText(_translate("MyWindow", "MIN TEMP"))

    
def run_visualization():  
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle('My Weather App')
    window.setFixedWidth(800)
    window.setFixedHeight(600)
    window.setStyleSheet("background: #A9A9A9;")
    
    window.show()
    app.installTranslator(window.translator)
    sys.exit(app.exec_())