''' Scrapping the Weather Forecast Details from the https://weather.com '''

import sys
import requests
from selenium import webdriver



def weather_forecast_details(city):
    ''' To get the weather forecast details for a particular city '''
    try:
        weatherdetails = {}

        response = requests.get(
            'https://api.weather.com/v3/location/search?apiKey=d522aa97197fd864d36b418f39ebb323&format=json&language=en-IN&locationType=locale&query=' + city)  # pylint: disable=line-too-long
        response_data = response.json()

        placeid = response_data.get('location').get('placeId')[0]

        driver = webdriver.Chrome()
        driver.get('https://weather.com/en-IN/weather/today/l/' + placeid)

        weatherdetails['loc'] = driver.find_element_by_class_name('today_nowcard-location').text
        weatherdetails['time'] = driver.find_element_by_class_name('today_nowcard-timestamp').text
        weatherdetails['temp'] = driver.find_element_by_class_name('today_nowcard-temp').text
        weatherdetails['phrase'] = driver.find_element_by_class_name('today_nowcard-phrase').text
        weatherdetails['degrees'] = driver.find_element_by_class_name('deg-feels').text

        driver.close()
        print(weatherdetails)
    except:                                            # pylint:disable=bare-except
        print("No City Found!")


if __name__ == '__main__':
    weather_forecast_details(sys.argv[1])
