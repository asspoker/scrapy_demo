# coding=utf-8
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Request, CrawlSpider, Rule

from logindemo.items import CateGoryItem


class WendaSpider(CrawlSpider):
    name = 'wenda'
    start_urls = [
        'http://app.jzb.com/xadmin/wenda/questioncategory/',
        'http://app.jzb.com/xadmin/wenda/question/',
    ]

    rules = (
        Rule(LinkExtractor(allow=('app\.jzb\.com/xadmin/wenda/question/\d+/update/$',)), callback='parse_page',
             follow=True, process_request='process_request'),
        Rule(LinkExtractor(allow=('app\.jzb\.com/xadmin/wenda/questioncategory/\d+/update/$',)),
             callback='parse_category', follow=True, process_request='process_request'),

    )

    cookies = None

    def process_request(self, request):
        request = request.replace(**{'cookies': self.cookies})
        return request

    def start_requests(self):
        for url in self.start_urls:
            if not self.cookies:
                self.cookies = self.post_login(url)  # 得到该url下的cookie
            yield Request(url, dont_filter=True, cookies=self.cookies, meta={'cookiejar': 1})  # 这里填入保存的cookies

    def post_login(self, response):
        return {
            'sessionid': "zekfd90rw21a1biw5i0uiyj8i5pbb5we",
        }

    def parse(self, response):
        print response.url
        return super(WendaSpider, self).parse(response)

    def parse_page(self, response):
        # inspect_response(response, self)
        print "url: %s" % response.url

    def parse_category(self, response):
        img = response.xpath("//img[@class='field_img']/@src").extract()
        ci = CateGoryItem()
        ci['image_urls'] = img
        return ci
