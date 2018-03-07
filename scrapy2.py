# attempt at using scrapy

import scrapy
from scrapy.crawler import CrawlerProcess
from fake_useragent import UserAgent
ua = UserAgent()

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        url = 'http://quotes.toscrape.com/'
        tag = getattr(self, 'tag', None)
        if tag is not None:
            url = url + 'tag/' + tag
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
            }
        # page = response.url.split("/")[-2]
        # filename = 'quotes-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.css('div.quote'))
        # self.log('Saved file %s' % filename)
            # print "QUOTE IS.....",quote
        # next_page = response.css('li.next a::attr(href)').extract_first()
        # if next_page is not None:
        #     yield response.follow(next_page, self.parse)
        for a in response.css('li.next a'):
            yield response.follow(a, self.parse)


process = CrawlerProcess({
    'USER_AGENT': ua.chrome
})

process.crawl(QuotesSpider)
process.start() # the script will block here until the crawling is finished
