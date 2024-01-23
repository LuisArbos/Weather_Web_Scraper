from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.exc import IntegrityError
from datetime import datetime, timedelta

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

engine = create_engine('access+pyodbc:///?odbc_connect=DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:/Documentos/VSCODE/Python/Weather Web Scraper/weatherScraper/weather_database.accdb;')
Base.metadata.create_all(engine)

#Create the session
Session = sessionmaker(bind=engine)
session = Session()

def should_run_data_storing():
    last_weather_entry = session.query(Weather).order_by(Weather.Timestamp.desc()).first()
    if not last_weather_entry or last_weather_entry.Timestamp < (datetime.now() - timedelta(hours=2)):
        return True
    return False

def add_data(data):
    for item in data:
        #For the city table
        city_name = item.get('city')
        existing_city = session.query(City).filter(City.CityName == city_name).first()

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

        #For the weather table
        current_temperature = item.get('temp_now')
        current_wind = item.get('wind_now')
        timestamp = datetime.now().replace(minute=0, second=0, microsecond=0)
        
        existing_weather = session.query(Weather).filter(Weather.Timestamp == timestamp, Weather.CityID == city_instance.CityID).first()
        if not existing_weather:
            weather_instance = Weather(CurrentTemperature = current_temperature, CurrentWind = current_wind, CityID = city_instance.CityID, Timestamp = timestamp)
            session.add(weather_instance)
            session.commit()
        else:
            print("Duplicated entry found in weather. Skipping insertion.")

        #For the day table
        day_list = ['day_0', 'day_1', 'day_2', 'day_3', 'day_4', 'day_5', 'day_6']
        for day in day_list:
            date_day = item.get(day, {}).get('date')
            maximum_temperature = item.get(day, {}).get('max_temp')
            minimum_temperature = item.get(day, {}).get('min_temp')
            rain = item.get(day, {}).get('rain')
            snow = item.get(day, {}).get('snow')
            sunrise = item.get(day, {}).get('sunrise')
            sunset = item.get(day, {}).get('sunset')
            existing_day = session.query(Day).filter(Day.WeatherID == weather_instance.WeatherID, Day.Date == date_day).first()
            if not existing_day:
                day_instance = Day(WeatherID = weather_instance.WeatherID, Date = date_day, MaxTemp = maximum_temperature, MinTemp = minimum_temperature, Rain = rain, Snow = snow, Sunrise = sunrise, Sunset = sunset)
                session.add(day_instance)
                session.commit()
            else:
                print("Duplicated entry found in day. Skipping insertion")

        #For the timelapse table
            if item.get(day, {}).get('timelapse', {}).get('date') != None:
                date_timelapse = item.get(day, {}).get('timelapse', {}).get('date')
                h00 = str(item.get(day, {}).get('timelapse', {}).get('h00'))
                h02 = str(item.get(day, {}).get('timelapse', {}).get('h02'))
                h04 = str(item.get(day, {}).get('timelapse', {}).get('h04'))
                h06 = str(item.get(day, {}).get('timelapse', {}).get('h06'))
                h08 = str(item.get(day, {}).get('timelapse', {}).get('h08'))
                h10 = str(item.get(day, {}).get('timelapse', {}).get('h10'))
                h12 = str(item.get(day, {}).get('timelapse', {}).get('h12'))
                h14 = str(item.get(day, {}).get('timelapse', {}).get('h14'))
                h16 = str(item.get(day, {}).get('timelapse', {}).get('h16'))
                h18 = str(item.get(day, {}).get('timelapse', {}).get('h18'))
                h20 = str(item.get(day, {}).get('timelapse', {}).get('h20'))
                h22 = str(item.get(day, {}).get('timelapse', {}).get('h22'))

                timelapse_instance = Timelapse(DayID = day_instance.DayID, Date = date_timelapse, H00 = h00, H02 = h02, H04 = h04, H06 = h06, H08 = h08, H10 = h10, H12 = h12, H14 = h14, H16 = h16, H18 = h18, H20 = h20, H22 = h22)
                session.add(timelapse_instance)
                session.commit()

# Query data
result = session.query(City).all()

# Close the session
session.close()