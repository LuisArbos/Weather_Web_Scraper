# Weather Web Scraper
This is my first Web Scraping project. For these project I'm using the Scrapy library to extract weather information for different cities, from https://www.eltiempo.es/.

Once I have all the necessary information, I'll print it in a table using the tabulate library. This is a preliminare version.

## Project Organization
This project is organized in different blocks. 
-  Spider configuration: (you can find it inside weatherScraper -> weatherScraper -> spiders)
    - There is one function to let the spider know where it has to start.
    - One function to scrape the main page looking for valid urls.
    - One function to scrape the urls got and extract the infor we want.
-  Visualization file, right now you can find the visualization in the visualize.py file, where you can check the basic table I'm currently using.

## Future Implementations
-  I want to be able to get information from all the cities in Spain with this Spider.
-  Also I want to change the visual output and design a GUI to expose the information.
-  Once all of that is done, I'll need to think about what can I do with the information I'm keeping.
