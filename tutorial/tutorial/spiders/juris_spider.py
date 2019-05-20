import scrapy

from tutorial.items import Item
from builtins import enumerate, range, str


class JurisSpider(scrapy.Spider):
    name = "juris"

    def get_text(self, response, path):
        return response.xpath(path).extract_first().strip()

    def start_requests(self):
        urls = []
        path = 'https://stj.jusbrasil.com.br/jurisprudencia/'
        for i in range(1, 10):
            urls.append(path + str(i))

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        item = Item()

        pa = '//*[@id="app-root"]/div/div[2]/div/div/div/div[1]/div[1]/div/div[5]/div/div/div/article/'
        th1 = 'div[1]/div'
        th2 = 'div[2]'

        item['processo'] = self.get_text(response, pa + th1 + '[1]/div[2]/text()')
        item['orgao'] = self.get_text(response, pa + th1 + '[2]/div[2]/text()')
        item['publicacao'] = self.get_text(response, pa + th1 + '[3]/div[2]/text()')
        item['julgador'] = self.get_text(response, pa + th1 + '[4]/div[2]/text()')
        item['relator'] = self.get_text(response, pa + th1 + '[5]/div[2]/text()')

        selector = response.xpath(pa + th2 + '/*')
        conteudoj = {}
        for cnt, h in enumerate(selector.css('h3'), start=1):
            chave = h.xpath('string()').extract_first()
            lista = [p.xpath('string()').extract_first() for p in h.xpath(
                '''./following-sibling::p[count(preceding-sibling::h3) = %d]''' % cnt)]
            conteudoj[chave] = lista
            item['elementos'] = conteudoj
        yield item
