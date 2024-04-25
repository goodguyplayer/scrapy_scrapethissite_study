from itemloaders.processors import TakeFirst, MapCompose, Join
from scrapy.loader import ItemLoader


class CountryItemLoader(ItemLoader):
    default_output_processor = TakeFirst()
    name_in = MapCompose(lambda x: x.strip(), Join(""))
    #population_in = MapCompose(lambda x: int(x))
    #area_in = MapCompose(lambda x: float(x))
    

class HockeyTeamLoader(ItemLoader):
    default_output_processor = TakeFirst()
    name_in = MapCompose(lambda x: x.strip(), Join(""))
    year_in = MapCompose(lambda x: x.strip(), Join(""))
    wins_in = MapCompose(lambda x: x.strip(), Join(""))
    losses_in = MapCompose(lambda x: x.strip(), Join(""))
    ot_losses_in = MapCompose(lambda x: x.strip(), Join(""))
    win_perc_in = MapCompose(lambda x: x.strip(), Join(""))
    goals_for_in = MapCompose(lambda x: x.strip(), Join(""))
    goals_against_in = MapCompose(lambda x: x.strip(), Join(""))
    more_less_in = MapCompose(lambda x: x.strip(), Join(""))