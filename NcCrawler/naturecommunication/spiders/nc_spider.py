import scrapy
from scrapy import Spider
import json
from lxml import etree
from Crawler.NcCrawler.naturecommunication.items import NCfulltext_item
from numpy import unicode
import pymongo
import random

class NC(Spider):
    name = "nc_spider"
    allowed_domain="www.nature.com"
    host="https://www.nature.com"
    id = 0

    authors=[]

    start_urls = []
    for page in range(4,44):
        start_urls.append('https://www.nature.com/subjects/physical-sciences/ncomms?searchType=journalSearch&sort=PubDate&page='+str(page))



    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.list_parse)

    def list_parse(self, response):

        hxs = scrapy.Selector(response)

        for num in range(1,50):
            article_url=hxs.xpath('//*[contains(@class,"border-gray-medium border-bottom-1 pb20")]['+str(num)+']//a/@href').extract()
        # 除去 \n
            article_url="".join(article_url)
            article_url=article_url.replace("\n","")
            article_url=article_url.strip()

            authors=hxs.xpath('//*[contains(@class,"border-gray-medium border-bottom-1 pb20")]['+str(num)+']//*[@itemprop="name"][1]/text()').extract()
         # 除去 \n
            authors=",".join(authors)
            item = NCfulltext_item()
            item['_id']=article_url
            item['url']=article_url
            item['authors']=authors
            url=self.host+article_url

            yield scrapy.Request(url,callback=self.list_parsedetail, meta={'item':item})

    def list_parsedetail(self, response):
        abstract = ""
        introduction = ""
        results = ""
        methods = ""
        discussion = ""
        references = ""

        hxs = scrapy.Selector(response)
        # 获取 article title
        title = hxs.xpath('//*[contains(@data-test,"article-title")][1]//text()').extract()
        title = "".join(title)
        title = title.replace("\n", "")
        title = title.strip()

        # tags = hxs.xpath('//*[contains(@class,"serif article-section js-article-section cleared clear")]/h2[1]/span[1]/text()').extract()
        # section_number = len(tags)

        sections = hxs.xpath('//section[@*]')
        tags=sections.xpath('div[1]/h2/text()').extract()
        section_number = len(tags)
        for sl in range(1,section_number):
            tag=tags[sl-1]
            tag=tag.lower()
            content=sections[sl-1].xpath('div[1]//p//text()').extract()
            #出现引用的地方要标注出来 [1]
            contentout=[]

            for paras in content:
                if paras.isdigit():
                    contentout.append('['+str(paras)+']')
                else:
                    contentout.append(paras)
            content="".join(contentout)
            content=content.replace("\n","")
            content=content.strip()
            if "abstract" in tag:
                abstract=content
            elif "introduction" in tag:
                introduction=content
            elif "method" in tag:
                methods=content
            elif "discussion" in tag:
                discussion =content
                if "result" in tag:
                    results = content
            elif "result" in tag:
                results =content
            elif "references" in tag:
                content =[]
                parts=sections[sl - 1].xpath('div//ol/li')
                parts_num=len(parts)
                for part_i in range(1,parts_num):
                    index="".join(parts[part_i-1].xpath('span/text()').extract())
                    refs="".join(parts[part_i-1].xpath('p//text()').extract())
                    refs='['+index.replace(".","")+']'+refs
                    content.append(refs)
                # 出现引用的地方要标注出来 []
                content = "".join(content)
                content = content.replace("\n", "")
                content = content.strip()
                references =content

        item=response.meta['item']
        # item = NCfulltext_item()
        # item['_id']=title + str(random.randint(1,1000))
        item['title']=title
        # item['authors']=pageitem['authors_en']
        item['results']=results
        item['abstract']=abstract
        item['discussion']=discussion
        item['methods']=methods
        item['references']=references
        item['introduction']=introduction
        yield item

