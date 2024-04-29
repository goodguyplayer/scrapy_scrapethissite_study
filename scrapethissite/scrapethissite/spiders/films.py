from typing import Any, Iterable
import scrapy
from pathlib import Path

from scrapy.http import Response
from scrapethissite.itemloaders import CountryItemLoader
from scrapethissite.items import CountryItem
from scrapy.exceptions import CloseSpider


class FilmsSpider(scrapy.Spider):
    name = "films"
    #custom_settings = {
    #    "ITEM_PIPELINES" : {
    #        'scrapethissite.pipelines.CountriesToMySQLPipeline' : 400
    #    }
    #}
    allowed_domains = ["www.scrapethissite.com"]
    start_urls = ["https://www.scrapethissite.com/pages/ajax-javascript/?ajax=true&year=%s" % page for page in list(range(2010,2016))]
    handle_httpstatus_list = [404]


    def parse(self, response):
        yield response.json()