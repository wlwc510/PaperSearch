import pymongo


def __init__(self):
    # self.host = "192.168.2.212"
    # self.user = "sa"
    # self.password = "Bigsearch@"
    # self.db = "db_lql"
    # self.connetion = pymssql.connect(self.host, self.user, self.password, self.db)
    # self.cursor = self.connetion.cursor()

    client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
    self.db = client['nc_title']


def process_item(self):
    try:
        item = dict(item)
        sql = "INSERT INTO [journal_cn] (title_en, authors_en, abstract_en, title_url) VALUES ('" + item[
            'title_en'] + "',' " + item['authors_en'] + "',' " + item['abstract_en'] + "',' " + item['title_url'] + "')"
        # sql = "INSERT INTO [journal_cn] (title_cn, authors_cn, organizations, keywords_cn, abstract_cn, journal_cn, journal_en, issn, cn, year, volume, issue, page, clcs, isCore, publisher, title_md5, title_url) VALUES ('"+item['title_cn']+"',' "+item['authors_cn']+"', '"+item['organizations']+"',' "+item['keywords_cn']+"', '"+item['abstract_cn']+"', '"+item['journal_cn']+"', '"+item['journal_en']+"', '"+item['issn']+"', '"+item['cn']+"', '"+item['year']+"', '"+item['volume']+"', '"+item['issue']+"', '"+item['page']+"', '"+item['clcs']+"', '"+str(item['isCore'])+"', '"+item['publisher']+"', '"+item['md5']+"', '"+item['title_url']+"')"
        # print(sql)
        self.cursor.execute(sql)
        self.connetion.commit()
        print('nc插入成功')
    except Exception as e:
        print("--------------->", e)
        pass
    return ''

def query_item(self):
    try:
        item = dict(item)
        sql = "INSERT INTO [journal_cn] (title_en, authors_en, abstract_en, title_url) VALUES ('" + item[
            'title_en'] + "',' " + item['authors_en'] + "',' " + item['abstract_en'] + "',' " + item['title_url'] + "')"
        # sql = "INSERT INTO [journal_cn] (title_cn, authors_cn, organizations, keywords_cn, abstract_cn, journal_cn, journal_en, issn, cn, year, volume, issue, page, clcs, isCore, publisher, title_md5, title_url) VALUES ('"+item['title_cn']+"',' "+item['authors_cn']+"', '"+item['organizations']+"',' "+item['keywords_cn']+"', '"+item['abstract_cn']+"', '"+item['journal_cn']+"', '"+item['journal_en']+"', '"+item['issn']+"', '"+item['cn']+"', '"+item['year']+"', '"+item['volume']+"', '"+item['issue']+"', '"+item['page']+"', '"+item['clcs']+"', '"+str(item['isCore'])+"', '"+item['publisher']+"', '"+item['md5']+"', '"+item['title_url']+"')"
        # print(sql)
        self.cursor.execute(sql)
        self.connetion.commit()
        print('nc插入成功')
    except Exception as e:
        print("--------------->", e)
        pass
    return ''

query_item(self)
