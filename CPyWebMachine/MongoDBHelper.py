import pymongo

def RatingPaper(uuid,paperid,scores):
    client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
    db = client['ncdb']
    collection = db['user2record']
    test= collection.find_one({"uuid":uuid,"paperid":paperid})
    if str(test)=='None':
        collection.insert_one({"uuid":uuid,"paperid":paperid,"rating":scores})
    else:
        collection.update({"uuid":uuid,"paperid":paperid},{"$set":{"rating":scores}})
    return collection.find_one({"uuid":uuid,"paperid":paperid})

def getUserItemMatrix(uuid):
    client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
    db = client['ncdb']
    collection = db['user2record']
    # datacolls=collection.find({})
    userlist=collection.distinct('uuid')
    itemlist=collection.distinct('paperid')
    ratingMatrix=[]
    for user_id in userlist:
        if user_id==uuid:
            row = collection.find({"uuid":user_id},{"rating":1,"_id":0})
            ratingrow=[]
            for i in row:
                ratingrow.append(float(i['rating']))
            ratingMatrix.append(ratingrow)
            userlist.remove(user_id)
    for user_id in userlist:
        row = collection.find({"uuid": user_id}, {"rating": 1, "_id": 0})
        ratingrow = []
        for i in row:
            ratingrow.append(float(i['rating']))
        ratingMatrix.append(ratingrow)

    return ratingMatrix,itemlist



