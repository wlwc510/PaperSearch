# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
# import pymssql


class NCPipeline(object):

    def __init__(self):
        # self.host = "192.168.2.212"
        # self.user = "sa"
        # self.password = "Bigsearch@"
        # self.db = "db_lql"
        # self.connetion = pymssql.connect(self.host, self.user, self.password, self.db)
        # self.cursor = self.connetion.cursor()

        client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
        self.db = client['ncdb']
        self.collection=self.db['nc_fulltext']

    def process_item(self, item, spider):
        try:
            # item = dict(item)
            # sql = "INSERT INTO [nc_title] (title_en, authors_en, abstract_en, title_url) VALUES ('"+",".join(item['title_en'])+"',' "+",".join(item['authors_en'])+"',' "+",".join(item['abstract_en'])+"',' "+",".join(item['title_url'])+"')"
            # sql = "INSERT INTO [journal_cn] (title_cn, authors_cn, organizations, keywords_cn, abstract_cn, journal_cn, journal_en, issn, cn, year, volume, issue, page, clcs, isCore, publisher, title_md5, title_url) VALUES ('"+item['title_cn']+"',' "+item['authors_cn']+"', '"+item['organizations']+"',' "+item['keywords_cn']+"', '"+item['abstract_cn']+"', '"+item['journal_cn']+"', '"+item['journal_en']+"', '"+item['issn']+"', '"+item['cn']+"', '"+item['year']+"', '"+item['volume']+"', '"+item['issue']+"', '"+item['page']+"', '"+item['clcs']+"', '"+str(item['isCore'])+"', '"+item['publisher']+"', '"+item['md5']+"', '"+item['title_url']+"')"
            # print(sql)
            # self.cursor.execute(sql)
            # self.connetion.commit()
            self.collection.insert_one(item)
            print('nc_fulltext插入成功')
        except Exception as e:
           print("--------------->", e)
           pass
        return ''
        # try:
        #     self.db.vip.insert(item)
        # except:
        #     # print('主键冲突')
        #     pass
        # return ''
