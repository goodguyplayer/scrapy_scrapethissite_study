import scrapy
from pathlib import Path
from scrapethissite.itemloaders import HockeyTeamLoader
from scrapethissite.item import HockeyTeamItem
from scrapy.exceptions import CloseSpider


class HockeyTeamSpider(scrapy.Spider):
    name = "hockey"
    allowed_domains = ["www.scrapethissite.com"]
    start_urls = ["https://www.scrapethissite.com/pages/forms/"]
    handle_httpstatus_list = [404]

    def parse(self, response):
        if response.status == 404:
            raise CloseSpider('Received 404 Response')
        
        for hockey in response.css(''):
            hockey_team = HockeyTeamLoader(item=HockeyTeamItem(), selector=hockey)

            hockey_team.add_css('name', '')
            hockey_team.add_css('year', '')
            hockey_team.add_css('wins', '')
            hockey_team.add_css('losses', '')
            hockey_team.add_css('ot_losses', '')
            hockey_team.add_css('win_perc', '')
            hockey_team.add_css('goals_for', '')
            hockey_team.add_css('goals_against', '')
            hockey_team.add_css('more_less', '')

            yield hockey_team.load_item()
