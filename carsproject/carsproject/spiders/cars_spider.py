import scrapy
from carsproject.items import CarItem


class CarsSpider(scrapy.Spider):
    name = "cars"
    start_urls = [
        "https://www.cars.com/new-cars/?type=electric-vehicle",
        "https://www.cars.com/new-cars/?type=suv",
        "https://www.cars.com/new-cars/?type=sedan",
        "https://www.cars.com/new-cars/?type=pickup-truck",
        "https://www.cars.com/new-cars/?type=coupe",
        "https://www.cars.com/new-cars/?type=hatchback",
        "https://www.cars.com/new-cars/?type=wagon",
        "https://www.cars.com/new-cars/?type=convertible",
        "https://www.cars.com/new-cars/?type=van"
    ]

    def parse(self, response):
        vehicle_type = response.url.split('=')[-1].replace('-', ' ').title()

        for car in response.css('div.new-car-model-card'):
            image = car.css(
                'div.new-car-model-card-image img::attr(src)').get()
            name = car.css(
                'div.new-car-model-card-name::text').get().strip()
            start_price = car.css(
                'div.new-car-model-card-price::text').re_first(r'\$(\d+,\d+)')

            yield CarItem(
                image=image,
                name=name,
                start_price=start_price,
                type=vehicle_type
            )
