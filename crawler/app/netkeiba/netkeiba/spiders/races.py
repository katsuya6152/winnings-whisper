import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from netkeiba.items import CrawlNetkeibaItem, CrawlRaceResultItem
from scrapy_playwright.page import PageMethod
import re

class RacesSpider(CrawlSpider):
    name = "races"

    def start_requests(self):
        url = "https://db.netkeiba.com/?pid=race_search_detail"
        yield scrapy.Request(
            url,
            meta=dict(
                playwright=True,
                playwright_page_methods=[
                    # 競走種別：芝
                    PageMethod("click", "input[type='checkbox'][id='check_track_1']"),
                    # 期間：2017 ~
                    PageMethod("select_option", "select[name='start_year']", "2017"),
                    # 競馬場：東京・中山・中京・京都・阪神
                    PageMethod("click", "input[type='checkbox'][id='check_Jyo_05']"),
                    PageMethod("click", "input[type='checkbox'][id='check_Jyo_06']"),
                    PageMethod("click", "input[type='checkbox'][id='check_Jyo_07']"),
                    PageMethod("click", "input[type='checkbox'][id='check_Jyo_08']"),
                    PageMethod("click", "input[type='checkbox'][id='check_Jyo_09']"),
                    # 距離：1600~3200
                    PageMethod("click", "input[type='checkbox'][id='check_kyori_1600']"),
                    PageMethod("click", "input[type='checkbox'][id='check_kyori_1700']"),
                    PageMethod("click", "input[type='checkbox'][id='check_kyori_1800']"),
                    PageMethod("click", "input[type='checkbox'][id='check_kyori_1900']"),
                    PageMethod("click", "input[type='checkbox'][id='check_kyori_2000']"),
                    PageMethod("click", "input[type='checkbox'][id='check_kyori_2100']"),
                    PageMethod("click", "input[type='checkbox'][id='check_kyori_2200']"),
                    PageMethod("click", "input[type='checkbox'][id='check_kyori_2300']"),
                    PageMethod("click", "input[type='checkbox'][id='check_kyori_2400']"),
                    PageMethod("click", "input[type='checkbox'][id='check_kyori_2500']"),
                    PageMethod("click", "input[type='checkbox'][id='check_kyori_2600']"),
                    PageMethod("click", "input[type='checkbox'][id='check_kyori_3000']"),
                    PageMethod("click", "input[type='checkbox'][id='check_kyori_3200']"),
                    # 表示件数：100
                    PageMethod("select_option", "select[name='list']", "100"),
                    # 検索
                    PageMethod("click", "input[type='submit'][value='検索']"),
                ],
                errback=self.errback,
            ),
        )

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//tr[position()>1]//td[position()=5]/a'), callback='parse_item', follow=False),
        Rule(LinkExtractor(restrict_xpaths='//*[@id="contents_liquid"]/div[2]/ul[1]/li[14]/a')),
    )

    async def parse_item(self, response):
        tr_elements = response.xpath('//table[@summary="レース結果"]/child::tr')
        id = response.xpath('substring(//ul[@class="race_place fc"]/li/a[@class="active"]/@href, 7, 12)').get()
        yield CrawlNetkeibaItem(
            id = id,
            race_name = response.xpath('//dd/h1/text()').get(), 
            race_place = response.xpath('//div[@class="race_head_inner"]/ul/li/a[@class="active"]/text()').get(), 
            number_of_entries = len(tr_elements) - 1, 
            race_state = response.xpath('//diary_snap_cut/span/text()').get(), 
            date = response.xpath('//div[@class="data_intro"]/p/text()').get()
        )
        for index, tr_ in enumerate(tr_elements):
            if index == 0:
                continue
            cleaned_html = re.sub(r'</?diary_snap_cut>', '', tr_.get())
            tr = scrapy.Selector(text=cleaned_html).xpath('//tr')
            yield CrawlRaceResultItem(
                id = id,
                horse_id = id + str(index).zfill(2),
                rank = tr.xpath('./td[position()=1]/text()').get(),
                box = tr.xpath('./td[position()=2]/span/text()').get(),
                horse_order = tr.xpath('./td[position()=3]/text()').get(),
                horse_name = tr.xpath('./td[position()=4]/a/text()').get(),
                sex_and_age = tr.xpath('./td[position()=5]/text()').get(),
                burden_weight = tr.xpath('./td[position()=6]/text()').get(),
                jockey = tr.xpath('./td[position()=7]/a/text()').get(),
                time = tr.xpath('./td[position()=8]/text()').get(),
                difference = tr.xpath('./td[position()=9]/text()').get(),
                transit = tr.xpath('./td[position()=11]/text()').get(),
                climb = tr.xpath('./td[position()=12]/span/text()').get(),
                odds = tr.xpath('./td[position()=13]/text()').get(),
                popularity = tr.xpath('./td[position()=14]/span/text()').get(),
                horse_weight = tr.xpath('./td[position()=15]/text()').get(),
                horse_trainer = tr.xpath('./td[position()=19]/a/text()').get(),
                horse_owner = tr.xpath('./td[position()=20]/a/text()').get(),
                prize = tr.xpath('./td[position()=21]/text()').get()
            )

    async def errback(self, failure):
        page = failure.request.meta["playwright_page"]
        await page.close()