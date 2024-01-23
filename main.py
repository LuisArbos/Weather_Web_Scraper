import weatherScraper.weatherScraper.spiders.weather_spider
import weatherScraper.gui.gui as gui
import data_storing
import weatherScraper.gui.gui_converted_file as gui2

if __name__ == "__main__":
    try:
        if data_storing.should_run_data_storing():
            info = weatherScraper.weatherScraper.spiders.weather_spider.run_spider()
            data_storing.add_data(info)
            print("Data stored successfully.")
        else:
            print("Skipping data storing as it was executed recently.")
        
        gui.run_visualization()
    except Exception as e:
        print(f'Error in the main script: {e}')
