import weatherScraper.weatherScraper.spiders.weather_spider
import visualize

if __name__ == "__main__":
    try:
        info = weatherScraper.weatherScraper.spiders.weather_spider.run_spider()
        print("Calling print table info function: ->")
        visualize.print_table_info(info)
        
    except Exception as e:
        print(f'Error in the main script: {e}')
