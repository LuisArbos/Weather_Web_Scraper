from typing import Any, Iterable
import scrapy
from scrapy.http import Request, Response
from scrapy.item import Item, Field
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

class Conditions(Item):
    date = Field()
    max_temp = Field()
    min_temp = Field()
    rain = Field()
    snow = Field()
    wind = Field()
    sunrise = Field()
    sunset = Field()
    

class Weather(Item):
    city = Field()
    temp_now = Field()
    wind_now = Field()
    day_0 = Field()
    day_1 = Field()
    day_2 = Field()
    day_3 = Field()
    day_4 = Field()
    day_5 = Field()
    day_6 = Field()

global li
li = []


class MySpider(scrapy.Spider):
    name = "second_spider"
    allowed_domains = ['eltiempo.es']
    start_urls = ['https://www.eltiempo.es/leon.html', 'https://www.eltiempo.es/zaragoza.html', 'https://www.eltiempo.es/tarragona.html']
    rules = (
        Rule(LinkExtractor(allow="castilla-y-leon"))
    )
    
    handle_httpstatus_list = [403, 404, 500]

    def parse(self, response):
        if response.status in self.handle_httpstatus_list:
            self.log(f"Received a {response.status} response for URL: {response.url}")
        else:  
            global weather_item
            global day_0_cond
            global  day_1_cond     
            weather_item = Weather()
            day_0_cond, day_1_cond, day_2_cond, day_3_cond, day_4_cond, day_5_cond, day_6_cond = Conditions(), Conditions(), Conditions(), Conditions(), Conditions(), Conditions(), Conditions()             

            weather_item['city'] = response.css(".-itl::text").get().replace(" ", "").replace("\n", "")
            weather_item['temp_now'] = response.css("span.c-tib-text.degrees::text").get()
            weather_item['wind_now'] = response.css('span.wind-text-value.velocity::text')[0].get() + response.css('span.wind-text-unit::text')[0].get()

            day_0_cond['date'] = response.css('.datetime').css('.text-roboto-condensed::text')[0].get().replace("\n", "").lstrip().rstrip()
            day_0_cond['max_temp'] = response.css('div.text-poppins-medium.header-max-min').css('div.max-temperature')[0].css('span::text').get()
            day_0_cond['min_temp'] = response.css('div.text-poppins-medium.header-max-min').css('div.min-temperature')[0].css('span::text').get()
            day_0_cond['rain'] = response.css('tbody tr:nth-child(4)').css('td::text')[1].get()
            day_0_cond['snow'] = response.css('tbody tr:nth-child(5)').css('td::text')[1].get()
            day_0_cond['wind'] = response.css('tbody tr:nth-child(6)').css('.wind').css('.velocity')[0].css('span.wind-text-value::text').get() + response.css('tbody tr:nth-child(6)').css('.wind').css('.velocity')[0].css('span.wind-text-unit::text').get()
            day_0_cond['sunrise'] = response.css('tbody tr:nth-child(7)').css('td::text')[0].get()
            day_0_cond['sunset'] = response.css('tbody tr:nth-child(8)').css('td::text')[0].get()

            day_1_cond['date'] = response.css('.datetime').css('.text-roboto-condensed::text')[1].get().replace("\n", "").lstrip().rstrip()
            day_1_cond['max_temp'] = response.css('div.text-poppins-medium.header-max-min').css('div.max-temperature')[1].css('span::text').get()
            day_1_cond['min_temp'] = response.css('div.text-poppins-medium.header-max-min').css('div.min-temperature')[1].css('span::text').get()
            day_1_cond['rain'] = response.css('tbody tr:nth-child(4)').css('td::text')[2].get()
            day_1_cond['snow'] = response.css('tbody tr:nth-child(5)').css('td::text')[2].get()
            day_1_cond['wind'] = response.css('tbody tr:nth-child(6)').css('.wind').css('.velocity')[1].css('span.wind-text-value::text').get() + response.css('tbody tr:nth-child(6)').css('.wind').css('.velocity')[1].css('span.wind-text-unit::text').get()
            day_1_cond['sunrise'] = response.css('tbody tr:nth-child(7)').css('td::text')[1].get()
            day_1_cond['sunset'] = response.css('tbody tr:nth-child(8)').css('td::text')[1].get()

            day_2_cond['date'] = response.css('.datetime').css('.text-roboto-condensed::text')[2].get().replace("\n", "").lstrip().rstrip()
            day_2_cond['max_temp'] = response.css('div.text-poppins-medium.header-max-min').css('div.max-temperature')[2].css('span::text').get()
            day_2_cond['min_temp'] = response.css('div.text-poppins-medium.header-max-min').css('div.min-temperature')[2].css('span::text').get()
            day_2_cond['rain'] = response.css('tbody tr:nth-child(4)').css('td::text')[3].get()
            day_2_cond['snow'] = response.css('tbody tr:nth-child(5)').css('td::text')[3].get()
            day_2_cond['wind'] = response.css('tbody tr:nth-child(6)').css('.wind').css('.velocity')[2].css('span.wind-text-value::text').get() + response.css('tbody tr:nth-child(6)').css('.wind').css('.velocity')[2].css('span.wind-text-unit::text').get()
            day_2_cond['sunrise'] = response.css('tbody tr:nth-child(7)').css('td::text')[2].get()
            day_2_cond['sunset'] = response.css('tbody tr:nth-child(8)').css('td::text')[2].get()

            day_3_cond['date'] = response.css('.datetime').css('.text-roboto-condensed::text')[3].get().replace("\n", "").lstrip().rstrip()
            day_3_cond['max_temp'] = response.css('div.text-poppins-medium.header-max-min').css('div.max-temperature')[3].css('span::text').get()
            day_3_cond['min_temp'] = response.css('div.text-poppins-medium.header-max-min').css('div.min-temperature')[3].css('span::text').get()
            day_3_cond['rain'] = response.css('tbody tr:nth-child(4)').css('td::text')[4].get()
            day_3_cond['snow'] = response.css('tbody tr:nth-child(5)').css('td::text')[4].get()
            day_3_cond['wind'] = response.css('tbody tr:nth-child(6)').css('.wind').css('.velocity')[3].css('span.wind-text-value::text').get() + response.css('tbody tr:nth-child(6)').css('.wind').css('.velocity')[3].css('span.wind-text-unit::text').get()
            day_3_cond['sunrise'] = response.css('tbody tr:nth-child(7)').css('td::text')[3].get()
            day_3_cond['sunset'] = response.css('tbody tr:nth-child(8)').css('td::text')[3].get()

            day_4_cond['date'] = response.css('.datetime').css('.text-roboto-condensed::text')[4].get().replace("\n", "").lstrip().rstrip()
            day_4_cond['max_temp'] = response.css('div.text-poppins-medium.header-max-min').css('div.max-temperature')[4].css('span::text').get()
            day_4_cond['min_temp'] = response.css('div.text-poppins-medium.header-max-min').css('div.min-temperature')[4].css('span::text').get()
            day_4_cond['rain'] = response.css('tbody tr:nth-child(4)').css('td::text')[5].get()
            day_4_cond['snow'] = response.css('tbody tr:nth-child(5)').css('td::text')[5].get()
            day_4_cond['wind'] = response.css('tbody tr:nth-child(6)').css('.wind').css('.velocity')[4].css('span.wind-text-value::text').get() + response.css('tbody tr:nth-child(6)').css('.wind').css('.velocity')[4].css('span.wind-text-unit::text').get()
            day_4_cond['sunrise'] = response.css('tbody tr:nth-child(7)').css('td::text')[4].get()
            day_4_cond['sunset'] = response.css('tbody tr:nth-child(8)').css('td::text')[4].get()

            day_5_cond['date'] = response.css('.datetime').css('.text-roboto-condensed::text')[5].get().replace("\n", "").lstrip().rstrip()
            day_5_cond['max_temp'] = response.css('div.text-poppins-medium.header-max-min').css('div.max-temperature')[5].css('span::text').get()
            day_5_cond['min_temp'] = response.css('div.text-poppins-medium.header-max-min').css('div.min-temperature')[5].css('span::text').get()
            day_5_cond['rain'] = response.css('tbody tr:nth-child(4)').css('td::text')[6].get()
            day_5_cond['snow'] = response.css('tbody tr:nth-child(5)').css('td::text')[6].get()
            day_5_cond['wind'] = response.css('tbody tr:nth-child(6)').css('.wind').css('.velocity')[5].css('span.wind-text-value::text').get() + response.css('tbody tr:nth-child(6)').css('.wind').css('.velocity')[5].css('span.wind-text-unit::text').get()
            day_5_cond['sunrise'] = response.css('tbody tr:nth-child(7)').css('td::text')[5].get()
            day_5_cond['sunset'] = response.css('tbody tr:nth-child(8)').css('td::text')[5].get()

            day_6_cond['date'] = response.css('.datetime').css('.text-roboto-condensed::text')[6].get().replace("\n", "").lstrip().rstrip()
            day_6_cond['max_temp'] = response.css('div.text-poppins-medium.header-max-min').css('div.max-temperature')[6].css('span::text').get()
            day_6_cond['min_temp'] = response.css('div.text-poppins-medium.header-max-min').css('div.min-temperature')[6].css('span::text').get()
            day_6_cond['rain'] = response.css('tbody tr:nth-child(4)').css('td::text')[7].get()
            day_6_cond['snow'] = response.css('tbody tr:nth-child(5)').css('td::text')[7].get()
            day_6_cond['wind'] = response.css('tbody tr:nth-child(6)').css('.wind').css('.velocity')[6].css('span.wind-text-value::text').get() + response.css('tbody tr:nth-child(6)').css('.wind').css('.velocity')[6].css('span.wind-text-unit::text').get()
            day_6_cond['sunrise'] = response.css('tbody tr:nth-child(7)').css('td::text')[6].get()
            day_6_cond['sunset'] = response.css('tbody tr:nth-child(8)').css('td::text')[6].get()

            weather_item['day_0'] = day_0_cond
            weather_item['day_1'] = day_1_cond
            weather_item['day_2'] = day_2_cond
            weather_item['day_3'] = day_3_cond
            weather_item['day_4'] = day_4_cond
            weather_item['day_5'] = day_5_cond
            weather_item['day_6'] = day_6_cond

            # print(f'City: {weather_item["city"]}, Temperature Now: {weather_item["temp_now"]}, Max Temp for Today: {weather_item["today"]["max_temp"]}, Min Temp for Today: {weather_item["today"]["min_temp"]}, Current Wind Speed: {weather_item["wind_now"]}, Date: {weather_item["today"]["date"]}')
            # print(f'City: {weather_item["city"]}, Temperature Now: {weather_item["temp_now"]}, Max Temp for Tomorrow: {weather_item["tomorrow"]["max_temp"]}, Min Temp for Tomorrow: {weather_item["tomorrow"]["min_temp"]}, Current Wind Speed: {weather_item["wind_now"]}, Date: {weather_item["tomorrow"]["date"]}')
            
            item = {}
            item = {
                'city' : weather_item['city'],
                'temp_now': weather_item['temp_now'],
                'wind_now': weather_item['wind_now'],
                'today': weather_item['day_0'],
                'tomorrow' : weather_item['day_1'],
                'day_2': weather_item['day_2'],
                'day_3': weather_item['day_3'],
                'day_4': weather_item['day_4'],
                'day_5': weather_item['day_5'],
                'day_6': weather_item['day_6'],
            }
            li.append(item)
            print(item)
            yield li
            
def run_spider():
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })
    process.crawl(MySpider)
    # the script will block here until the crawling is finished
    process.start()
    
    return li

if __name__ == "__main__":
    run_spider()
    