# -*- coding: utf-8 -*-
import scrapy


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.com']
    start_urls = ["https://www.amazon.com/Apple-iPhone-Pacific-Carrier-Subscription/dp/B08L5NRZNW/ref=sr_1_1_sspa?dchild=1&keywords=iphone+12"]

    def parse(self, response):
        test1 = response.xpath('//a/text()').extract()
        test2 = response.xpath('/html/body/div/text()').extract()
        test3 = response.xpath('.//*[@class="navFooterDescItem"]')
        print("test1 is:", test1)
        print("test2 is:", test2)
        print("test3 is:", test3)
        print("response is:", response.text)
