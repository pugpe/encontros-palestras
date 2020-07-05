from scrapy import Spider
from scrapy.crawler import CrawlerProcess

import readme_generator


class PugRankSpider(Spider):
    name = 'pugpe'
    allowed_domains = ['pug.pe']
    start_urls = ['http://pycon.pug.pe/archive/past_events/']

    def parse(self, response):
        talks = response.xpath('//h2[@id="talks"]/following-sibling::div')
        for talk in talks:
            title = talk.xpath('.//h4/text()').get()
            author = talk.xpath('.//h6/text()').get()

            yield {
                'titulo': title,
                'autor': author
            }

        if 'archive/past_events/' in response.url:
            past_urls = response.xpath(
                '//div[@class="panel"]//a/@href').getall()
            for next_url in past_urls:
                yield response.follow(next_url, callback=self.parse)


def main():
    process = CrawlerProcess(
        settings={
            "FEEDS": {
                "temp/talks_all.csv": {"format": "csv"},
            },
        }
    )
    process.crawl(PugRankSpider)
    process.start()
    readme_generator.rank_readme()


if __name__ == '__main__':
    main()  # pylint: disable=no-value-for-parameter
