from click import argument, command

from scrapy import Request
from scrapy import Spider
from scrapy.crawler import CrawlerProcess


class PugSpider(Spider):
    name = 'pugpe'
    allowed_domains = ['pug.pe']

    def parse(self, response):
        event = response.xpath('//h2[@id="home"]/text()').get()
        talks = response.xpath('//h2[@id="talks"]/following-sibling::div')
        place = response.xpath(
            '//h2[@id="local"]/following-sibling::h5').re_first('Local:(.*)')
        event_time = response.xpath(
            '//h2[@id="local"]/following-sibling::h5').re_first('Horário:(.*)')
        for talk in talks:
            title = talk.xpath('.//h4/text()').get()
            author = talk.xpath('.//h6/text()').get()
            abstract = talk.css('p::text').get()

            yield {
                'titulo': title,
                'autor': author,
                'abstract': abstract,
            }

        if 'archive/past_events/' in response.url:
            past_urls = response.xpath(
                '//div[@class="panel"]//a/@href').getall()
            for next_url in past_urls:
                yield response.follow(next_url, callback=self.parse)


@command()
@argument('editions', nargs=-1)
def main(editions):
    start_urls = []
    for edition in editions:
        start_urls.append(f"http://pycon.pug.pe/{edition.upper()}/")
    if not editions:
        start_urls.append("http://pycon.pug.pe/archive/past_events/")
    process = CrawlerProcess(
        settings={
            "FEEDS": {
                "items.csv": {"format": "csv"},
            },
        }
    )
    process.crawl(PugSpider, start_urls=start_urls)
    process.start()


if __name__ == '__main__':
    main()
