import scrapy
from pathlib import Path
from scrapethissite.itemloaders import HockeyTeamLoader
from scrapethissite.items import HockeyTeamItem
from scrapy.exceptions import CloseSpider


class HockeyTeamSpider(scrapy.Spider):
    name = "hockey"
    allowed_domains = ["www.scrapethissite.com"]
    start_urls = ["https://www.scrapethissite.com/pages/forms/?page_num=1"]
    handle_httpstatus_list = [404]

    def parse(self, response):
        if response.status == 404:
            raise CloseSpider('Received 404 Response')
        
        for hockey in response.css('tr.team'):
            hockey_team = HockeyTeamLoader(item=HockeyTeamItem(), selector=hockey)
            hockey_team.add_css('name', 'td.name::text')
            hockey_team.add_css('year', 'td.year::text')
            hockey_team.add_css('wins', 'td.wins::text')
            hockey_team.add_css('losses', 'td.losses::text')
            hockey_team.add_css('ot_losses', 'td.ot-losses::text')
            hockey_team.add_css('win_perc', 'td.pct.text-success::text')
            hockey_team.add_css('goals_for', 'td.gf::text')
            hockey_team.add_css('goals_against', 'td.ga::text')
            hockey_team.add_css('more_less', 'diff.text-success')
            yield hockey_team.load_item()
        
        next_page = response.css('[aria-label="Next"]::attr(href)').get()
        if next_page is not None:
            next_page_url = "https://www.scrapethissite.com" + next_page
            yield response.follow(next_page_url, callback=self.parse)