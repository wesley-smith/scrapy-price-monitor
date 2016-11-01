from .base_spider import BaseSpider


class AmazonSpider(BaseSpider):
    name = "amazon.com"
    allowed_domains = ["amazon.com"]

    def parse(self, response):
        item = response.meta.get('item', {})
        item['url'] = response.url
        item['title'] = response.css("span#productTitle::text").extract_first("").strip()
        item['price'] = float(
            response.css("span#priceblock_ourprice::text").re_first("\$(.*)") or 0
        )
        item['rating'] = response.css('a#reviewStarsLinkedCustomerReviews > i > span::text').re_first("(.+) out of .+")
        yield item