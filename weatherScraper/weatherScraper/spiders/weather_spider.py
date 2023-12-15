from typing import Any, Iterable
import scrapy
import re
from scrapy.http import Response
from scrapy.item import Item, Field
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

global url_li
url_li = []
global li
li = []

class Timelapse(Item):
    date = Field()
    h00 = Field()
    h02 = Field()
    h04 = Field()
    h06 = Field()
    h08 = Field()
    h10 = Field()
    h12 = Field()
    h14 = Field()
    h16 = Field()
    h18 = Field()
    h20 = Field()
    h22 = Field()
    

class Conditions(Item):
    date = Field()
    max_temp = Field()
    min_temp = Field()
    rain = Field()
    snow = Field()
    wind = Field()
    sunrise = Field()
    sunset = Field()
    timelapse = Field()
    

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




class WeatherSpider(scrapy.Spider):
    name = "weather_spider"
    allowed_domains = ['eltiempo.es']
    start_urls = ['https://www.eltiempo.es'] # ['https://www.eltiempo.es/zaragoza.html']
    
    handle_httpstatus_list = [403, 404, 500]

    def start_requests(self):
        yield scrapy.Request(self.start_urls[0], callback=self.parse_urls)

    def parse_urls(self, response):
        urls = response.css('a::attr(href)').extract()

        # This one is to get the urls that are city.html and the ones that start with https://www.eltiempo.es/something.html
        city_pattern = re.compile(r'^/(.+)\.html$|https://www\.eltiempo\.es/(.+)\.html$') 
                
        city_urls = [url for url in urls if city_pattern.match(url)]

        filtered_urls = [url for url in city_urls if "/legal/" not in url]
        global final_urls
        final_urls = [f'https://www.eltiempo.es{url}' if url.startswith('/') else url for url in filtered_urls]

        for url in final_urls:
            url_li.append(url)
            url2 = url + '?v=por_hora'
            yield scrapy.Request(url2, callback=self.parse_city_hour)

    def parse_city_hour(self, response):
        global timelapse_list
        timelapse_list = []
        # day_0_tlapse, day_1_tlapse, day_2_tlapse, day_3_tlapse = Timelapse(), Timelapse(), Timelapse(), Timelapse()
        # timelapse_list = [day_0_tlapse, day_1_tlapse, day_2_tlapse, day_3_tlapse]

        hour_check = response.css('ul.days').css('li').css('p.text-roboto-condensed.hours::text').getall()
        hour_img_val = response.css('ul.days').css('li').css('img::attr(src)').getall()
        hour_date = response.css('h2.days-title.text-poppins-bold::attr(id)').getall()
        
        timelapse_list = [
            Timelapse(date=hour_date[0]),
            Timelapse(date=hour_date[1]),
            Timelapse(date=hour_date[2]),
            Timelapse(date=hour_date[3]),
        ]

        replacements = { # Pending
            "https://statics.eltiempo.es/images/weather/svg/v1/32/d000.svg": "Despejado",
            "https://statics.eltiempo.es/images/weather/svg/v1/32/d100.svg": "Poco nuboso",
            "https://statics.eltiempo.es/images/weather/svg/v1/32/d200.svg": "Poco nuboso",
            "https://statics.eltiempo.es/images/weather/svg/v1/32/d210.svg": "Lluvias", # ????
            "https://statics.eltiempo.es/images/weather/svg/v1/32/d300.svg": "Nuboso",
            "https://statics.eltiempo.es/images/weather/svg/v1/32/n000.svg": "Despejado",
            "https://statics.eltiempo.es/images/weather/svg/v1/32/n100.svg": "Poco nuboso",
            "https://statics.eltiempo.es/images/weather/svg/v1/32/n200.svg": "Intervalos nubosos",
            "https://statics.eltiempo.es/images/weather/svg/v1/32/n210.svg": "Lluvias", # ????
            "https://statics.eltiempo.es/images/weather/svg/v1/32/n300.svg": "Nuboso",
            } 
        updated_img_val = [replacements.get(link, link) for link in hour_img_val]
        combined_keys = []
        current_date_index = 0

        for hour in hour_check:
            combined_key = hour_date[current_date_index] + "-" + hour
            combined_keys.append(combined_key)
            if hour == "00:00":
                current_date_index += 1

        hour_updated_dict = dict(zip(combined_keys, updated_img_val))
        # print(hour_updated_dict)
        key_list = [combined_key for combined_key in hour_updated_dict.keys() if int(combined_key.split('-')[1].split(':')[0]) % 2 == 0]
        filtered_dict = {combined_key: hour_updated_dict[combined_key] for combined_key in key_list}
        # print(filtered_dict)

        hour_to_field_mapping = {
            "00:00": "h00",
            "02:00": "h02",
            "04:00": "h04",
            "06:00": "h06",
            "08:00": "h08",
            "10:00": "h10",
            "12:00": "h12",
            "14:00": "h14",
            "16:00": "h16",
            "18:00": "h18",
            "20:00": "h20",
            "22:00": "h22",
        }

        for combined_key, value in filtered_dict.items():
            field_name = hour_to_field_mapping.get(combined_key.split('-')[1], None)
            date = combined_key.split('-')[0]
            if field_name is not None:
                # Find the index of the date in timelapse_list
                index = [item['date'] for item in timelapse_list].index(date)
                timelapse_list[index][field_name] = value
        print(timelapse_list)
        for url in final_urls:
            yield  scrapy.Request(url, callback=self.parse_city)
        
    
    def parse_city(self, response):
        if response.status in self.handle_httpstatus_list:
            self.log(f"Received a {response.status} response for URL: {response.url}")
        else:  
            weather_item = Weather()
            day_0_cond, day_1_cond, day_2_cond, day_3_cond, day_4_cond, day_5_cond, day_6_cond = Conditions(), Conditions(), Conditions(), Conditions(), Conditions(), Conditions(), Conditions()             
            

            day_list = [day_0_cond, day_1_cond, day_2_cond, day_3_cond, day_4_cond, day_5_cond, day_6_cond]
            
            weather_item['city'] = response.css(".-itl::text").get().replace("\n", "").lstrip().rstrip()
            weather_item['temp_now'] = response.css("span.c-tib-text.degrees::text").get()
            weather_item['wind_now'] = response.css('span.wind-text-value.velocity::text')[0].get() + response.css('span.wind-text-unit::text')[0].get()
            
            for i in range(len(day_list)):
                day_list[i]['date'] = response.css('.datetime').css('.text-roboto-condensed::text')[i].get().replace("\n", "").lstrip().rstrip()
                day_list[i]['max_temp'] = response.css('div.text-poppins-medium.header-max-min').css('div.max-temperature')[i].css('span::text').get()
                day_list[i]['min_temp'] = response.css('div.text-poppins-medium.header-max-min').css('div.min-temperature')[i].css('span::text').get()
                day_list[i]['rain'] = response.css('tbody tr:nth-child(4)').css('td::text')[i+1].get()
                day_list[i]['snow'] = response.css('tbody tr:nth-child(5)').css('td::text')[i+1].get()
                day_list[i]['wind'] = response.css('tbody tr:nth-child(6)').css('.wind').css('.velocity')[i].css('span.wind-text-value::text').get() + response.css('tbody tr:nth-child(6)').css('.wind').css('.velocity')[i].css('span.wind-text-unit::text').get()
                day_list[i]['sunrise'] = response.css('tbody tr:nth-child(7)').css('td::text')[i].get()
                day_list[i]['sunset'] = response.css('tbody tr:nth-child(8)').css('td::text')[i].get()
                if i<=3:
                    day_list[i]['timelapse'] = timelapse_list[i]

            weather_item['day_0'] = day_0_cond
            weather_item['day_1'] = day_1_cond
            weather_item['day_2'] = day_2_cond
            weather_item['day_3'] = day_3_cond
            weather_item['day_4'] = day_4_cond
            weather_item['day_5'] = day_5_cond
            weather_item['day_6'] = day_6_cond
          
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
            # yield li   


def run_spider():
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })
    process.crawl(WeatherSpider)
    # the script will block here until the crawling is finished
    process.start()
    print(li)
    return li

if __name__ == "__main__":    
    run_spider()
    