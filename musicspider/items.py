# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MusicspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    music_id = scrapy.Field()
    music_name = scrapy.Field()
    artist = scrapy.Field()
    special = scrapy.Field()
    music_url= scrapy.Field()
    pic_url = scrapy.Field()
    lrc_url = scrapy.Field()
    comments = scrapy.Field()
    music_id = scrapy.Field()
    per_id = scrapy.Field()
    per_title = scrapy.Field()
    per_pic_url = scrapy.Field()
    category = scrapy.Field()
    


    
