__author__ = 'devilo'


from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from basic_spider.items import BasicSpiderItem

class BasicSpider(BaseSpider):
    name = "based_spider"
    allowed_domains = ["craigslist.org"]
    start_urls = [
        "http://sfbay.craigslist.org/npo/"
    ]

    def parse(self , response):
        hxs = Selector(response)
        titles = hxs.xpath('//span[@class="pl"]')

        items = []

        for titles in titles:

            item = BasicSpiderItem()

            item["title"] = titles.xpath('a/text()').extract()
            item["link"]  = titles.xpath('a/@href').extract()
            items.append(item)

        return items
