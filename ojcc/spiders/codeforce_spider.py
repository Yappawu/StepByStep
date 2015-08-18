# -*- coding: utf-8 -*-

from scrapy.spiders import Spider
from scrapy.selector import Selector
from ojcc.items import AccountItem


class CodeforcesAccountSpider(Spider):
    name = 'codeforces_user'
    allowed_domains = ['codeforces.com']

    def __init__(self, username, *args, **kwargs):
        super(CodeforcesAccountSpider, self).__init__(*args, **kwargs)

        self.username = username
        self.start_urls = [
                'http://codeforces.com/profile/%s' %
                username
        ]

    def parse(self, response):

        sel = Selector(response)

        item = AccountItem()
        item['origin_oj'] = 'codeforces'
        item['username'] = self.username

        item['rating'] = sel.xpath('//span[@class="user-violet"]/text()').\
            extract()[1]
        return item
