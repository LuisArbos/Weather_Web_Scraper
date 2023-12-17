from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.exc import IntegrityError

Base = declarative_base()

#Declaring the different tables:

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

engine = create_engine('access+pyodbc:///?odbc_connect=DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:/Documentos/VSCODE/Python/Weather Web Scraper/weatherScraper/weather_database.accdb;')
Base.metadata.create_all(engine)

#Create the session
Session = sessionmaker(bind=engine)
session = Session()

def add_data(data):
    for item in data:
        #For the city table
        city_name = item.get('city')
        
        #For the weather table
        current_temperature = item.get('temp_now')
        current_temperature = current_temperature
        current_wind = item.get('wind_now')
        current_wind = current_wind.split(" ")
        
        #For the day table
        date = item.get('day_0', {}).get('date')
        maximum_temperature = item.get('day_0', {}).get('max_temp')
        minimum_temperature = item.get('day_0', {}).get('min_temp')
        rain = item.get('day_0', {}).get('rain')
        snow = item.get('day_0', {}).get('snow')
        sunrise = item.get('day_0', {}).get('sunrise')
        sunset = item.get('day_0', {}).get('sunset')
        print(date, "-", maximum_temperature, "-", minimum_temperature, "-", rain, "-", snow, "-", sunrise, "-", sunset)
        #For the timelapse table

        """existing_city = session.query(City).filter(City.CityName == city_name).first()
        if existing_city:
            city_instance = existing_city
        else:
            try:
                city_instance = City(CityName=city_name)
                session.add(city_instance)
                session.commit()            
            except IntegrityError:
                session.rollback()
                print(f"City '{city_name}' already exists.")

        weather_instance = Weather(CurrentTemperature = current_temperature, CurrentWind = current_wind, CityID = city_instance.CityID)
        session.add(weather_instance)
        session.commit()"""

# Query data
result = session.query(City).all()
for row in result:
    print(row.CityID, row.CityName)

# Close the session
session.close()