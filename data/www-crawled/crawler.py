import scrapy

class YogaSpider(scrapy.Spider):
    name = "yoga"
    start_urls = [
        'https://www.yogajournal.com/poses'  # Replace with the actual URL
    ]

    def parse(self, response):
        for pose in response.css('div.pose'):  # Modify the selector based on the actual website structure
            yield {
                'name': pose.css('::text').get()
            }

        # Follow pagination links (if any)
        next_page = response.css('a.next::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)