from scrapy import Request, Spider


class MusicSpider(Spider):
    name = "music"

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.pages = int(kwargs.get("pages", 10))

    def start_requests(self):
        for i in range(0, self.pages + 1):
            yield Request(f"https://www.metacritic.com/browse/albums/score/metascore/all/filtered?view=detailed&page={i}")

    def parse(self, response):
        for td in response.xpath("//table[@class='clamp-list']/tr/td[@class='clamp-summary-wrap']"):
            yield {
                "id": td.xpath(".//input/@id").get(),
                "sort_no": td.xpath(".//span[@class='title numbered']/text()").get().strip(),
                "title": td.xpath(".//a[@class='title']/h3/text()").get().strip(),
                "artist": td.xpath(".//div[@class='artist']/text()").get().replace("by ", "", 1).strip(),
                "release_date": td.xpath(".//div[@class='clamp-details']/span[1]/text()").get().strip(),
                "summary": td.xpath(".//div[@class='summary']/text()").get().strip(),
                "metascore": td.xpath(".//div[@class='clamp-metascore']/a/div/text()").get(),
                "user_score": td.xpath(".//div[@class='clamp-userscore']/a/div/text()").get(),
            }
