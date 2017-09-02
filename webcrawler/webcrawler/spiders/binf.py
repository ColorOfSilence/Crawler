# -*- coding: utf-8 -*-
#response.xpath('//div[@id="mainHolder"]/table/tr/td/text()')[0].extract()
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
            yield scrapy.Request(url=url, callback=self.parse_data)

    def parse_data(self, response):
        start = -1
        for data in response.xpath('//div[@id="mainHolder"]/table/tr/td'):
            yield {
                'Gene Name' : response.xpath('//div[@id="mainHolder"]/table/tr/td/text()')[(start+1)].extract(),
                'SKBR3 Expression' : response.xpath('//div[@id="mainHolder"]/table/tr/td/text()')[start+2].extract(),
                'HCC1569 Expression' : response.xpath('//div[@id="mainHolder"]/table/tr/td/text()')[start+3].extract(),
                'SKBR3 Percentile': response.xpath('//div[@id="mainHolder"]/table/tr/td/text()')[start+4].extract(),
                'HCC1569 Percentile': response.xpath('//div[@id="mainHolder"]/table/tr/td/text()')[start+5].extract(),
                'D1/D2': response.xpath('//div[@id="mainHolder"]/table/tr/td/text()')[start+6].extract(),
                'D2/D1': response.xpath('//div[@id="mainHolder"]/table/tr/td/text()')[start+7].extract(),
                'D1-D2': response.xpath('//div[@id="mainHolder"]/table/tr/td/text()')[start+8].extract(),
                'D2-D1': response.xpath('//div[@id="mainHolder"]/table/tr/td/text()')[start+9].extract(),
            }
            start += 9
        # page = response.url.split("/")[-2]
        # filename = 'binf-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)