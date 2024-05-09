import requests
from selectorlib import Extractor

class Temperature:
    """
    Scrapes and returns the temperature value for a given
    city from the timeanddate.com/weather webpage.
    """
    base_url = 'https://www.timeanddate.com/weather/'
    yml_path = 'temperature.yaml'

    def __init__(self, country, city):
        self.country = country.replace(' ', '-')
        self.city = city.replace(' ', '-')

    def _build_url(self):
        """Builds the url string adding country and city"""
        url = f'{self.base_url}{self.country}/{self.city}'
        return url

    def _scrape(self):
        url =self._build_url()
        extractor = Extractor.from_yaml_file('temperature.yaml')
        r = requests.get(url)
        full_content = r.text
        raw_content = extractor.extract(full_content)
        return raw_content


    def get(self):
        scraped_content = self._scrape()
        return float(scraped_content['temp'].replace('°C', '').strip())


if __name__ == "__main__":
    temperature = Temperature(country='usa', city='san francisco')
    print(temperature.get())