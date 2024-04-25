from itemloaders.processors import TakeFirst, MapCompose, Join
from scrapy.loader import ItemLoader


class CountryItemLoader(ItemLoader):
    default_output_processor = TakeFirst()
    name_in = MapCompose(lambda x: x.strip(), Join(""))
    
