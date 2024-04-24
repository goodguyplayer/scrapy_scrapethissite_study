from itemloaders.processors import TakeFirst, MapCompose
from scrapy.loader import ItemLoader


class CountryItemLoader(ItemLoader):
    default_output_processor = TakeFirst()
    
