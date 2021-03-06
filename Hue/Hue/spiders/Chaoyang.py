import scrapy
from Hue.basepro import ZhengFuBaseSpider


class ChaoyangSpider(ZhengFuBaseSpider):
    """TODO SCRAPY"""
    name = 'Chaoyang'
    allowed_domains = ['chaoyang.gov.cn']
    start_urls = ['http://chaoyang.gov.cn/']

    start_page = 0
    method = "POST"
    api = "http://www.chaoyang.gov.cn/search/search.ct"
    data = {
        'siteCode': 'CYSZF',
        'isAll': '0',
        'offset': 'page',
        'limit': '15',
        'template': 'CYSZF',
        'ssfw': '2',
        'sswjlx': '1',
        'timefw': '1',
        'columnTypeId': '',
        'searchKey': 'keywords'
    }

    def edit_data(self, data, keyword, page):
        data['searchKey'] = keyword
        data['page'] = str(page)
        return data

    def edit_items_box(self, response):
        return response.css(".result-li")

    def edit_item(self, item):
        result = {}
        result['url'] = item.css("a.tit::attr(href)").get()
        return result

    def edit_page(self, response):
        try:
            return int(
                response.css(
                    "body > div.sousuo-wrap > div.ss-wrap.wrap-clear > div.left > div.fenye-wrap > span.nowpage::text"
                ).re(".*/(\d+)页")[0])
        except Exception:
            return 0
