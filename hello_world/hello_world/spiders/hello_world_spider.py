__author__ = 'devilo'

from scrapy.spider import Spider

class HelloWorldSpider(Spider):
    name = "hello_world_spider"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]


    def parse(self, response):
        filename = response.url.split("/")[-2]
        open(filename , "wb" ).write(response.body)
