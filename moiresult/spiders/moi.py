from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import FormRequest

from moiresult.items import MoiRecord


class MoiSpider(BaseSpider):
    name = "moi"
    allowed_domains = ["result-p.moi.ir"]
    start_urls = ["http://result-p.moi.ir/Portal/Home/default.aspx"]

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://result-p.moi.ir/Portal/Home/default.aspx
        """
        target = 'WebPart_f4e73bd8_5a9b_4703_bbbd_3ba9275580c4$LF0$PagerObject'
        for i in range(0, 125): # 125
            yield FormRequest.from_response(response,
                                            formdata={'__EVENTTARGET': target, '__EVENTARGUMENT': str(i)},
                                            callback=self.parse_item,
                                            dont_click=True
                                            )

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        rows = hxs.select('//tr[@class="DGItem "] | //tr[@class="DGAlt "]')

        items = []
        for row in rows:
            cols = row.select("td//text()")
            item = MoiRecord()
            item['rec_id'] = cols[0].extract()
            item['province'] = cols[1].extract()
            item['county'] = cols[2].extract()
            item['township'] = cols[3].extract()
            item['name'] = cols[5].extract()
            if len(cols) == 8:
                item['votes'] = cols[7].extract()
            else:
                item['votes'] = 0
            items.append(item)

        return items
