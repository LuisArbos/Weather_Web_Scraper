from scrapy.utils.reactor import install_reactor
install_reactor('twisted.internet.asyncioreactor.AsyncioSelectorReactor')

from scrapy.crawler import CrawlerRunner, CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.item import Item, Field
from twisted.internet import reactor
from weatherScraper.spiders.first_spider import FirstSpider

def stop_reactor(_):
    if reactor.running:
        reactor.stop()

def run_spider():

    custom_settings = {
        'USER_AGENT' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'REQUEST_FINGERPRINTER_IMPLEMENTATION' : '2.7',
        'LOG_LEVEL' : 'DEBUG',
    }
    process_settings = get_project_settings()
    process_settings.update(custom_settings)
    
    runner = CrawlerRunner(process_settings)
    
    def crawler_results(output):
        cities = []
        weathers = []
        winds = []
        print("Crawler Results Output:")
        print(output)
        for data in output:
            if data:
                cities.append(data.get("city"))
                weathers.append(data.get("weather_today"))
                winds.append(f'{data.get("wind_today")} {data.get("wind_units")}')
            else:
                print("Warning: Empty Data")
        reactor.stop()

    d = runner.crawl(FirstSpider)
    d.addCallback(crawler_results)
    d.addBoth(stop_reactor)
    
    # Start the reactor (twisted event loop)
    reactor.run()

    return cities, weathers, winds

if __name__ == "__main__":
    try:
        cities, weathers, winds = run_spider()
        for city, weather, wind in zip(cities, weathers, winds):
            print(f'City: {city}, Weather: {weather}, Wind Today: {wind}')
        for city in cities:
            print(city)
    except Exception as e:
        print(f'Error in the main script: {e}')
