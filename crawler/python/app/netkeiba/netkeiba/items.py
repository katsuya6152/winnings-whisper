import scrapy

class CrawlNetkeibaItem(scrapy.Item):
    id = scrapy.Field()
    race_name = scrapy.Field()
    race_place = scrapy.Field()
    number_of_entries = scrapy.Field()
    race_state = scrapy.Field()
    date = scrapy.Field()

class CrawlRaceResultItem(scrapy.Item):
    id = scrapy.Field()
    horse_id = scrapy.Field()
    rank = scrapy.Field()
    box = scrapy.Field()
    horse_order = scrapy.Field()
    horse_name = scrapy.Field()
    sex_and_age = scrapy.Field()
    burden_weight = scrapy.Field()
    jockey = scrapy.Field()
    time = scrapy.Field()
    difference = scrapy.Field()
    transit = scrapy.Field()
    climb = scrapy.Field()
    odds = scrapy.Field()
    popularity = scrapy.Field()
    horse_weight = scrapy.Field()
    horse_trainer = scrapy.Field()
    horse_owner = scrapy.Field()
    prize = scrapy.Field()

class CrawlRefundItem(scrapy.Item):
    id = scrapy.Field()
    race_id = scrapy.Field()
    bet_type = scrapy.Field()
    winning_horse_order = scrapy.Field()
    payout = scrapy.Field()
    winning_horse_popularity = scrapy.Field()