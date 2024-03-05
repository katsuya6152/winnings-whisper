from scrapy import signals
from scrapy.exceptions import NotConfigured
import mysql.connector

from .. import config

class StatsRecorderExtension:
    def __init__(self, db_config):
        self.db_config = db_config

    @classmethod
    def from_crawler(cls, crawler):
        # 拡張機能が有効でない場合は例外を発生させる
        if not crawler.settings.getbool('STATS_RECORDER_ENABLED'):
            raise NotConfigured

        db_config = {
            'user': config.DB_USER,
            'password': config.PASSWORD,
            'host': config.HOST,
            'database': config.DATABASE,
        }

        ext = cls(db_config)

        crawler.signals.connect(ext.spider_closed, signal=signals.spider_closed)
        return ext

    def spider_closed(self, spider, reason):
        stats = spider.crawler.stats.get_stats()
        start_time = stats.get("start_time", "null")
        finish_time = stats.get("finish_time", "null")
        elapsed_time = self.seconds_to_time_format(int(stats.get("elapsed_time_seconds", 0)))
        
        with mysql.connector.connect(**self.db_config) as conn, conn.cursor() as cursor:
            cursor.execute('''CREATE TABLE IF NOT EXISTS spider_stats (
                                id INT AUTO_INCREMENT PRIMARY KEY,
                                spider_name VARCHAR(255),
                                start_time DATETIME,
                                finish_time DATETIME,
                                elapsed_time TIME,
                                reason VARCHAR(255),
                                stats TEXT)''')
            
            cursor.execute('''INSERT INTO spider_stats (spider_name, start_time, finish_time, elapsed_time, reason, stats) 
                                VALUES (%s, %s, %s, %s, %s, %s)''', 
                            (spider.name, start_time, finish_time, elapsed_time, reason, str(stats)))
            conn.commit()
    
    @staticmethod
    def seconds_to_time_format(seconds):
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        seconds = seconds % 60
        return "{:02}:{:02}:{:06.3f}".format(hours, minutes, seconds)