
import scrapy

class Sp1Spider(scrapy.Spider):
    name = "sp1"
    allowed_domains = ["scrapethissite.com"]
    start_urls = ["https://www.scrapethissite.com/pages/simple/"]

    def parse(self, response):
        # Loop through each country block on the page
        for country in response.xpath('//div[@class="col-md-4 country"]'):
            yield {
                # Extracting only the country name, ignoring the <i> tag
                "Country": country.xpath('.//h3[@class="country-name"]/text()[normalize-space()]').get().strip(),
                "Capital": country.xpath('.//span[@class="country-capital"]/text()').get(default="").strip(),
                "Population": country.xpath('.//span[@class="country-population"]/text()').get(default="").strip(),
                "Area": country.xpath('.//span[@class="country-area"]/text()').get(default="").strip()
            }
