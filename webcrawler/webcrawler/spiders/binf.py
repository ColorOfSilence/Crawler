# -*- coding: utf-8 -*-
#start with the 5th element in td to get 'Gene Name'
import scrapy


class BinfSpider(scrapy.Spider):
    name = "binf"
    allowed_domains = ["crdd.osdd.net"]
    start_urls = (
        'http://crdd.osdd.net/raghava/herceptinr/submit_pair_main.php?ran=3102&num=16582&method=exp',
    )
    def start_requests(self):
        urls = [
            'http://crdd.osdd.net/raghava/herceptinr/submit_pair_main.php?ran=3102&num=16582&method=exp'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for data in response.css('td'):
            start = 15
            yield {
                'Gene Name' : response.css('td::text')[(start+=1)].extract(),
                'SKBR3 Expression' : response.css('td::text').extract(),
                'HCC1569 Expression' : response.css('td::text').extract(),
                'SKBR3 Percentile': response.css('td::text').extract(),
                'HCC1569 Percentile': response.css('td::text').extract(),
                'D1/D2': response.css('td::text').extract(),
                'D2/D1': response.css('td::text').extract(),
                'D1-D2': response.css('td::text').extract(),
                'D2-D1': response.css('td::text').extract(),
            }
        # page = response.url.split("/")[-2]
        # filename = 'binf-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)
