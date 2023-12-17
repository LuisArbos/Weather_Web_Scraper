from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.exc import IntegrityError

Base = declarative_base()

#Declaring the different tables:

class City(Base):
    __tablename__ = 'City'
    CityID = Column(Integer, primary_key=True)
    CityName = Column(String)

"""class Temperature(Base):
    __tablename__ = 'Temperature'
    TemperatureID = Column(Integer, primary_key=True)
    CityID = Column(Integer, ForeignKey('City.CityID'))
    CurrentTemperature = Column(Integer)
    TodayMaxTemperature = Column(Integer)
    TodayMinTemperature = Column(Integer)
    City = relationship('City', back_populates='temperature')"""


engine = create_engine('access+pyodbc:///?odbc_connect=DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:/Documentos/VSCODE/Python/Weather Web Scraper/weatherScraper/weather_database.accdb;')
Base.metadata.create_all(engine)

#Create the session
Session = sessionmaker(bind=engine)
session = Session()

def add_data(data):
    for item in data:
        city_name = item.get('city')
        try:
            # Try to add the city to the City table
            city = City(CityName=city_name)
            session.add(city)
            session.commit()
        except IntegrityError:
            # If the city already exists, catch the IntegrityError (duplicate entry) and continue
            session.rollback()
            print(f"City '{city_name}' already exists.")

# Query data
result = session.query(City).all()
for row in result:
    print(row.ID, row.Name)

# Close the session
session.close()