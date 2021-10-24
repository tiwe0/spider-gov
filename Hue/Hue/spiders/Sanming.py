import scrapy
from Hue.basepro import ZhengFuBaseSpider


class SanmingSpider(ZhengFuBaseSpider):
    name = 'Sanming'
    allowed_domains = ['sm.gov.cn']
    api = "http://www.sm.gov.cn/smartSearch/interface/resource/list.do"
    method = "POST"
    keywords = ["煤炭"]
    data = {
        "pagesize": "10",
        "currentpage": "{page}",
        "queryHisId": "",
        "keyWord": "{keyword}",
        "keyWordProcess": "true",
        "siteId": "ff808081744e1c2301744e1e83600002",
        "siteName": "选择站点",
        "province": "",
        "isChangeOrder": "false",
        "order": "RELEVANCE"
    }

    def edit_items_box(self, response):
        raw_data = response.json()
        items_box = raw_data["rows"]
        return items_box

    def edit_item(self, item):
        data = {}
        data["title"] = item.get("docTitle", None)
        data["date"] = item.get("docrelTime", None)
        data["url"] = item.get("siteUrl", None)
        return data

    def edit_data(self, data, keyword, page):
        data["currentpage"] = str(page)
        data["keyWord"] = str(keyword)
        return data

    def edit_page(self, response):
        raw_data = response.json()
        total_page = raw_data["trsPage"]["pagecount"]
        return int(total_page)

