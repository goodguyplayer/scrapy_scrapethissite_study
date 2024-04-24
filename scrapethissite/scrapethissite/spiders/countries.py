import scrapy
from pathlib import Path
from scrapethissite.itemloaders import CountryItemLoader
from scrapethissite.items import CountryItem
from scrapy.exceptions import CloseSpider


class CountriesSpider(scrapy.Spider):
    name = "countries"
    allowed_domains = ["www.scrapethissite.com"]
    start_urls = ["https://www.scrapethissite.com/pages/simple/"]
    handle_httpstatus_list = [404]

    def parse(self, response):
        if response.status == 404:
            raise CloseSpider('Received 404 Response')
        
        for country in response.css('div.col-md-4.country'):
            country_item = CountryItemLoader(item=CountryItem(), selector=country)

            country_item.add_css('name', 'h3.country-name::text')
            country_item.add_css('capital', 'span.country-capital::text')
            country_item.add_css('population', 'span.country-population::text')
            country_item.add_css('area', 'span.country-area::text')
            yield country_item.load_item()
