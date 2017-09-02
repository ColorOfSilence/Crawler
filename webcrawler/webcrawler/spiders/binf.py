# -*- coding: utf-8 -*-
import scrapy


class BinfSpider(scrapy.Spider):
    name = "binf"
    allowed_domains = ["binf.com"]
    start_urls = (
        'http://www.binf.com/',
    )

    def parse(self, response):
        pass
