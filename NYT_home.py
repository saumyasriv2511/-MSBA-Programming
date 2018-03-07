import scrapy
from scrapy.crawler import CrawlerProcess
from fake_useragent import UserAgent


ua = UserAgent()

class NYTSpider(scrapy.Spider):
    name = "home"
    def start_requests(self):
        urls = ['https://www.nytimes.com/']
    
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
            
    def parse(self, response):
        # for key in response.css('meta.keywords'):
        filename = 'NYT.txt'
        
        f=open(filename,'a')  
        yield {
                f.write(response.css('meta ::attr(content)')[23].extract())
        
        }

       
        # next_page = response.css('li.next a::attr(href)').extract_first()
        # if next_page is not None:
        #     yield response.follow(next_page, self.parse)
        # for a in response.css('li.next a'):
        #     yield response.follow(a, self.parse)


class NewsSpider(scrapy.Spider):
    name = "News"
    start_urls = [
        'https://www.nytimes.com/',
    ]

    def parse(self, response):
        for article in response.css('h2.story-heading'):
            next_page = article.css('a::attr(href)').extract_first()
            if next_page is not None:
                yield response.follow(next_page, callback=self.parse_author)
    
    def parse_author(self, response):
        def extract_with_css(query):
            return response.css(query).extract_first().strip()
        
        filename = 'wordcloud_NYT.txt'
        
        # f=open(filename,'a')    
        # yield {
        #         f.write(extract_with_css('p.story-body-text story-content::text'))
        # }
        # f.close()
        yield {
                'text':extract_with_css('p.story-body-text story-content::text')
        }

process = CrawlerProcess({
    'USER_AGENT': ua.chrome
})

process.crawl(NYTSpider)
process.start()#stop_after_crawl=False) # the script will block here until the crawling is finished
