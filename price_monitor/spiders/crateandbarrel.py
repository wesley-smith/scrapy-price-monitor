from .base_spider import BaseSpider


class CrateAndBarrelSpider(BaseSpider):
    name = "crateandbarrel.com"

    def parse(self, response):
        item = response.meta.get('item', {})
        item['url'] = response.url
        item['title'] = response.css('.shop-bar-product-title::text').get()
        item['price'] = float(
            response.css('.shop-bar-price-area::text').get().replace('$,', '')
        )
        yield item
