from typing import Any, Iterable
import scrapy
from scrapy.http import Request, Response
from scrapy.item import Item, Field

class Weather(Item):
    city = Field()
    weather_today = Field()
    wind = Field()

class FirstSpider(scrapy.Spider):
    name = "first_spider"
    allowed_domains = ['eltiempo.es']
    start_urls = ['https://www.eltiempo.es/zaragoza.html']
    handle_httpstatus_list = [403, 404, 500]

    def parse(self, response):
        if response.status in self.handle_httpstatus_list:
            self.log(f"Received a {response.status} response for URL: {response.url}")
        else:
            weather_item = Weather()

            city_name = response.xpath('normalize-space(//body[@class="bg bg_general page-city"]//div[@id="page"]//div[@id="main"]//section[@class="modules"]//article[@id="headerCity"]//div[@class="-block-1"]//h1[@class="-h1-title"]/span[@class="-itl"])').get()
            weather_today = response.xpath('normalize-space(//body[@class="bg bg_general page-city"]//div[@id="page"]//div[@id="main"]//section[@class="modules"]//article[@id="headerCity"]//div[@class="-block-3 c-wrapper-pois"]//section[@class="c-pois"]//div[@class="c6 -a-top"]//section[@class="-block-i-1 -b-center temperature"]/span[@class="c-tib-text degrees"])').get()
            wind_today = response.xpath('normalize-space(//body[@class="bg bg_general page-city"]//div[@id="page"]//div[@id="main"]//section[@class="modules"]//article[@id="headerCity"]//div[@class="-block-3 c-wrapper-pois"]//section[@class="c-pois"]//div[@class="c6 -a-top"]//section[@class="-block-i-2"]//p[@class="-itr wind"]/span[@class="wind-text-value velocity"])').get()
            wind_units = response.xpath('normalize-space(//body[@class="bg bg_general page-city"]//div[@id="page"]//div[@id="main"]//section[@class="modules"]//article[@id="headerCity"]//div[@class="-block-3 c-wrapper-pois"]//section[@class="c-pois"]//div[@class="c6 -a-top"]//section[@class="-block-i-2"]//p[@class="-itr wind"]/span[@class="wind-text-unit"])').get()
            
            weather_item['city'] = city_name
            weather_item['weather_today'] = weather_today
            weather_item['wind'] = wind_today + wind_units
            
            parsed_data =  {
                'city': city_name,
                'weather_today': weather_today,
                'wind_today' : wind_today,
                'wind_units' : wind_units,
            }

            print(f'Parsed Data in Item: City: {weather_item["city"]}, Weather: {weather_item["weather_today"]}, Wind Today: {weather_item['wind']}')

            yield {
            'city': weather_item['city'],
            'weather_today': weather_item['weather_today'],
            'wind': weather_item['wind'],
            }
          
            