# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class BasicSpiderItem(Item):
    # define the fields for your item here like:
    # name = Field()

    #   Website: http://sfbay.craigslist.org/npo/
    #   The page is the list of items, each item consist of the following
    #   - Title
    #   - Link

    title = Field()
    link = Field()
