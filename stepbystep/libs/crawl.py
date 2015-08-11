from billiard import Process

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.utils.log import configure_logging  # noqa

settings = get_project_settings()


class AccountCrawler():

    def __init__(self):
        self.crawler = CrawlerProcess(settings)

    def _crawl(self, origin_oj, username):
        self.crawler.crawl(
            origin_oj + '_user',
            username=username,
        )
        self.crawler.start()
        self.crawler.stop()

    def crawl(self, origin_oj, username):
        p = Process(
            target=self._crawl,
            args=[
                origin_oj,
                username,
            ]
        )
        p.start()
        p.join()
