# -*- coding: utf-8 -*-

from scrapy.spiders import Spider
from scrapy.http import Request
from scrapy.selector import Selector
from ojcc.items import AccountItem


class HduAccountSpider(Spider):
    name = 'hduoj_user'
    allowed_domains = ['acm.hdu.edu.cn']

    accepted_url = \
        'http://acm.hdu.edu.cn/status.php?\
        first=&pid=&user=%s&lang=0&status=5'

    solved = {}

    def __init__(self, username, *args, **kwargs):
        super(HduAccountSpider, self).__init__(*args, **kwargs)

        self.username = username
        self.start_urls = [
            'http://acm.hdu.edu.cn/userstatus.php?user=%s' % username
        ]

    def parse(self, response):

        sel = Selector(response)

        self.item = AccountItem()
        self.item['origin_oj'] = 'hduoj'
        self.item['username'] = self.username

        self.item['nickname'] = sel.xpath('//h1/text()').extract()[0]
        self.nickname = self.item['nickname']
        self.item['rank'] = sel.xpath('//table')[4].\
            xpath('./tr')[1].xpath('./td/text()')[1].extract()
        self.item['accept'] = sel.xpath('//table')[4].\
            xpath('./tr')[3].xpath('./td/text()')[1].extract()
        self.item['submit'] = sel.xpath('//table')[4].\
            xpath('./tr')[4].xpath('./td/text()')[1].extract()
        yield Request(
            self.accepted_url % self.username,
            callback=self.accepted
        )

        yield self.item

    def accepted(self, response):

        sel = Selector(response)

        next_url = sel.xpath('.//p/a/@href')[2].extract()
        table_tr = sel.xpath('//table[@class="table_text"]/tr')[1:]
        for tr in table_tr:
            name = tr.xpath('.//td/a/text()').extract()[-1]
            problem_id = tr.xpath('.//td[4]/a/text()').extract()[0]
            submit_time = tr.xpath('.//td/text()').extract()[1]

            if name == self.nickname:
                self.solved[problem_id] = submit_time
                self.item['solved'] = self.solved

        if table_tr:
            yield Request(
                'http://' + self.allowed_domains[0] + next_url,
                callback=self.accepted
            )

        yield self.item
