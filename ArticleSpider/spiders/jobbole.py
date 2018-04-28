# -*- coding: utf-8 -*-
import scrapy


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/110287']

    def parse(self, response):
        # re_selector = response.xpath('//*[@id="post-110287"]/div[1]/h1/text()')
        re_selector = response.xpath('//html/body/div[1]/div[3]/div[1]/div[1]/h1')
        time = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/text()').extract()[0].strip().replace(" ·","").strip()
        pass
