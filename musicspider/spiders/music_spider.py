import scrapy
from musicspider.items import MusicspiderItem 

class QuotesSpider(scrapy.Spider):
    name = "musicspider"
    domain = 'http://www.luoo.net'
    def start_requests(self):
        urls = []
        for i in range(1,90):
            urls.append('http://www.luoo.net/tag/?p='+str(i))
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
        
    def parse(self, response):
        items=[]
        s= response.xpath('//div[@class="vol-list"]/div/a/@href').extract()
        for i in range(0,len(s)):
            item = MusicspiderItem()
            suburl =response.xpath('//div[@class="vol-list"]/div/a/@href').extract()[i]
            item['per_id'] = suburl[-3:]
            item['per_title'] = response.xpath('//div[@class="vol-list"]/div/a/@title').extract()[i]
            item['per_pic_url'] = response.xpath('//div[@class="vol-list"]/div/a/img/@src').extract()[i]
            item['category'] = response.xpath('//meta[@name="keywords"]/@content').extract_first().split(",")[-1]
            items.append(item)
            request = scrapy.Request(str(suburl), callback= self.subparse)
            request.meta['item'] = item
            yield request

    def subparse(self, response):
        item = response.meta['item']
        sels = response.xpath('//div[@class="track-wrapper clearfix"]').extract()
        for i in range(0,len(sels)):    
            item['music_name'] =response.xpath('//div[@class="track-wrapper clearfix"]/a/text()').extract()[i]
            item['artist'] =response.xpath('//div[@class="track-wrapper clearfix"]/span[2]/text()').extract()[i]
            item['music_id'] = "%02d" % (i+1)
            item['music_url'] ='http://mp3-cdn.luoo.net/low/luoo/radio'+item['per_id']+'/'+item['music_id']+'.mp3' 
            item['pic_url'] = response.xpath('//div[@class="track-wrapper clearfix"]/a[3]/@data-img').extract()[i]
            item['special'] = response.xpath('//div[@class="track-wrapper clearfix"]/a[3]/@data-text').extract()[i]
            lrc_id = response.xpath('//div[@class="track-wrapper clearfix"]/a[2]/@data-sid').extract()[i]
            item['lrc_url'] = 'http://www.luoo.net/single/lyric/'+lrc_id
            item['comments']= response.xpath('//p[@class="the-comment"]/text()').extract_first()
            item['category'] = response.xpath('//meta[@name="keywords"]/@content').extract_first().split(",")[-1].lower()
            yield item 


