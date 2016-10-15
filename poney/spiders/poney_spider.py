import scrapy


class PoneySpider(scrapy.Spider):
    name = "poney"
    start_urls = [
        'https://ja.wikipedia.org/wiki/マイリトルポニー〜トモダチは魔法〜#.E7.99.BB.E5.A0.B4.E3.82.AD.E3.83.A3.E3.83.A9.E3.82.AF.E3.82.BF.E3.83.BC'
    ]

    def parse(self, response):
        for poney in response.xpath('//*[@id="mw-content-text"]/dl/dt/text()').extract():
            yield {
                'name': poney
            }
