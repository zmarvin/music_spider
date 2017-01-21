# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
# more pipelines.py
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import signals
import json
import codecs
from twisted.enterprise import adbapi
from datetime import datetime
from hashlib import md5
import MySQLdb
import MySQLdb.cursors


class MySQLStoreMusicspiderPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(user = 'zmarvin', passwd = 'passwd', db = 'enjoymusicdb', host = 'localhost', charset = 'utf8', use_unicode = True)
        self.cursor = self.conn.cursor()
 
    def process_item(self, item, spider):
        try:
            self.cursor.execute(
                """INSERT IGNORE INTO song (music_id, music_name, artist,special, music_url, pic_url, lrc_url, comments, per_id, per_pic_url,per_title,category)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                (
                    item['music_id'],
                    item['music_name'],
                    item['artist'],
                    item['special'], 
                    item['music_url'],
                    item['pic_url'],
                    item['lrc_url'],
                    item['comments'],
                    item['per_id'],
                    item['per_pic_url'],
                    item['per_title'],
                    item['category']
                )
            )
            self.conn.commit()
        except MySQLdb.Error, e:
            print 'Error %d %s' % (e.args[0], e.args[1])
 
        return item
