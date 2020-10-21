# -*- coding: utf-8 -*-
import scrapy


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.com']
    start_urls = ["https://www.amazon.com/Apple-iPhone-Locked-Carrier-Subscription/dp/B08L5RZTTK/ref=sr_1_1_sspa?dchild=1&keywords=iphone+12&qid=1603233489&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzQkJUVDlYREZJNEYyJmVuY3J5cHRlZElkPUEwMTY2MzkwMzNHNEJOSkxJWU5ORiZlbmNyeXB0ZWRBZElkPUEwOTA5MzE1RFg5S0k0RkVFRE5TJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="]

    def parse(self, response):
        productTitle = response.xpath('//*[@class="a-link-normal"]/text()').extract_first()
        productPrice = response.xpath('//*[@id="priceblock_ourprice"]/text()').extract_first()
        print(productTitle, productPrice)
        yield{"ProductTitle": productTitle, "ProductPrice": productPrice}
