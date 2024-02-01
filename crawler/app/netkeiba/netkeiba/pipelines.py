from .database import session
from .models import Race, RaceResult
from netkeiba.items import CrawlNetkeibaItem, CrawlRaceResultItem
from scrapy.exceptions import DropItem

class GetRacePipeline:
    def process_item(self, item, spider):
        if isinstance(item, CrawlNetkeibaItem):
            if item.get('id') is None or item.get('id') == '':
                raise DropItem(f'Missing or empty "id" field in item: {item}')

            id_exists = session.query(Race).filter(Race.id==item['id']).first()
            if(id_exists != None):
                spider.crawler.engine.close_spider(spider, f'{item} exists in database')

            if(id_exists == None):
                race = Race()
                race.id = item['id']
                race.race_name = item['race_name']
                race.race_place = item['race_place']
                race.number_of_entries = item['number_of_entries']
                race.race_state = item['race_state']
                race.date = item['date']
                try:
                    session.add(race)
                    session.commit()
                except:
                    session.rollback()
                    raise
                finally:
                    session.close()
        elif isinstance(item, CrawlRaceResultItem):
            horse_id_exists = session.query(RaceResult).filter(RaceResult.horse_id==item['horse_id']).first()
            if(horse_id_exists == None):
                race_result = RaceResult()
                race_result.id = item['id']
                race_result.horse_id = item['horse_id']
                race_result.rank = item['rank']
                race_result.box = item['box']
                race_result.horse_order = item['horse_order']
                race_result.horse_name = item['horse_name']
                race_result.sex_and_age = item['sex_and_age']
                race_result.burden_weight = item['burden_weight']
                race_result.jockey = item['jockey']
                race_result.time = item['time']
                race_result.difference = item['difference']
                race_result.transit = item['transit']
                race_result.climb = item['climb']
                race_result.odds = item['odds']
                race_result.popularity = item['popularity']
                race_result.horse_weight = item['horse_weight']
                race_result.horse_trainer = item['horse_trainer']
                race_result.horse_owner = item['horse_owner']
                race_result.prize = item['prize']
                try:
                    session.add(race_result)
                    session.commit()
                except:
                    session.rollback()
                    raise
                finally:
                    session.close()

        return item