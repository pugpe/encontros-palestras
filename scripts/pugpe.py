import os
import shutil
from click import argument, command

from scrapy import Request
from scrapy import Spider
from scrapy.crawler import CrawlerProcess
import readme_generator


class PugSpider(Spider):
    name = 'pugpe'
    allowed_domains = ['pug.pe']

    def parse(self, response):
        if 'archive/past_events/' in response.url:
            past_urls = response.xpath(
                '//div[@class="panel"]//a/@href').getall()
            for next_url in past_urls:
                yield response.follow(next_url, callback=self.parse)

        event = response.xpath('//h2[@id="home"]/text()').get()
        talks = response.xpath('//h2[@id="talks"]/following-sibling::div')
        place = response.xpath(
            '//h2[@id="local"]/following-sibling::h5').re_first('Local:(.*)')
        event_time = response.xpath(
            '//h2[@id="local"]/following-sibling::h5').re_first('Horário:(.*)</h5>')
        talks_list = []
        for talk in talks:
            title = talk.xpath('.//h4/text()').get()
            author = talk.xpath('.//h6/text()').get()
            abstract = talk.css('p::text').get()

            talks_list.append({
                'titulo': title,
                'autor': author,
                'abstract': abstract,
            })

        if event and talks_list:
            yield {
                'evento': event,
                'local': place,
                'horario': event_time,
                'palestras': talks_list,
            }


@command()
@argument('edition')
def main(edition):
    start_urls = []
    if edition:
        start_urls.append(f"http://pycon.pug.pe/{edition.upper()}/")
    process = CrawlerProcess(
        settings={
            "FEEDS": {
                "temp/talks.json": {"format": "json"},
            },
        }
    )
    process.crawl(PugSpider, start_urls=start_urls)
    process.start()
    readme_generator.main()


if __name__ == '__main__':
    if os.path.exists("temp"):
        shutil.rmtree("temp")
    main()  # pylint: disable=no-value-for-parameter
