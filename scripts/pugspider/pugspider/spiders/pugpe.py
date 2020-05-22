import scrapy


class PugSpider(scrapy.Spider):
    name = 'pugpe'
    allowed_domains = ['pug.pe']

    start_urls = ['http://pycon.pug.pe/archive/past_events/']

    def parse(self, response):
        event = response.xpath('//h2[@id="home"]/text()').get()
        talks = response.xpath('//h2[@id="talks"]/following-sibling::div')
        for talk in talks:
            title = talk.xpath('.//h4/text()').get()
            author = talk.xpath('.//h6/text()').get()

            yield {
                'evento': event,
                'titulo': title,
                'autor': author
            }

        if 'archive/past_events/' in response.url:
            past_urls = response.xpath(
                '//div[@class="panel"]//a/@href').getall()
            for next_url in past_urls:
                yield response.follow(next_url, callback=self.parse)
