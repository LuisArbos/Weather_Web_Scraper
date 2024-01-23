# Weather Web Scraper
This is my first Web Scraping project. For these project I'm using the Scrapy library to extract weather information for different cities, from https://www.eltiempo.es/. I keep this information in an MS Access database and after that I show this information also in a small GUI I made with PyQt5.

## Project Organization
This project is organized in different blocks. 
-  Spider configuration: (you can find it inside weatherScraper -> weatherScraper -> spiders)
    - There is one function to let the spider know where it has to start.
    - One function to scrape the main page looking for valid urls.
    - One function to scrape the urls got and extract the infor we want.
-  Visualization file: (you can find it inside weatherScraper -> gui)
    - It contains two main files, gui.py where is all the code, and gui_converted_file.py which is the file I got from the PyQt5 Designer to make the first drawer.
    - I changed the old basic table for a modest GUI I made with PyQt5 library.
    - The GUI has a dropdown list where you can select the city from within the options it has.
    - The GUI will give all the information it has for today and tomorrow, including temperature, rain, snow, wind, and some other weather information.
-  Storaging file:
    - I used the data_storing.py for storage purpose.
    - There you can find the connection to the database which is an MS Access file, but could have been another. (It was easier for me to manage this file)
    - It also contais a small checker function that checks when was the last time all the storaging was executed to avoid executing and storing the same again.

## Main Libraries used for this project
- SQL ALchemy -> for the access and interaction with the Access Database,
- PyQt5 -> for the GUI
- Scrapy -> for the webscraping
  
## Final Version
- I think this project has reached the target. Currently it has a GUI where I can select in a dropdown list, the cities and it give the weather for today and tomorrow. I could have done the hole week but it seemed unnecessary.
