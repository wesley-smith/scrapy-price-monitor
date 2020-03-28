from .base_spider import BaseSpider


class PotteryBarnSpider(BaseSpider):
    name = "potterybarn.com"

    def parse(self, response):
        item = response.meta.get('item', {})
        item['url'] = response.url
        item['title'] = response.css('.pip-summary > h1 ::text').get()

        subset_pricing = response.css('.subset-pricing')
        if subset_pricing:
            prices = response.css(
                '.product-price .grouping-price > span:not(.price-strike-special) .price-amount::text'
            ).getall()
        else:
            prices = response.css(
                '.price-details .product-price > span.price-state:not(.price-strike-special) .price-amount::text'
            ).getall()

        if not prices:
            pass
        elif len(prices) > 1:
            item['price_low'] = float(prices[0].replace(',', ''))
            item['price_high'] = float(prices[1].replace(',', ''))
        else:
            item['price'] = float(prices[0].replace(',', ''))
        yield item
