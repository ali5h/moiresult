# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field


class MoiRecord(Item):
    rec_id = Field()
    province = Field()
    county = Field()
    township = Field()
    name = Field()
    votes = Field()
