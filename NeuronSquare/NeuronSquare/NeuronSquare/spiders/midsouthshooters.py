import scrapy
from ..items import NeuronsquareItem

class MidsouthshootersSpider(scrapy.Spider):
    name = 'midsouthshooters'
    start_urls = [
        'https://quotes.toscrape.com/'
    ]

    def parse(self, response):
        items = NeuronsquareItem()
        price = response.css('.text::text').extract()
        title = response.css('.text::text').extract()
        maftr = response.css('.text:: text').extract()
        items["price"] = price
        items['title'] = title
        items["maftr"] = maftr
        yield items
