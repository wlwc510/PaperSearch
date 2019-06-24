#coding=utf-8
import pymongo
import nltk
import nltk.data
import re

def splitSentence(paragraph):
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    sentences = tokenizer.tokenize(paragraph)
    return sentences

def GeneratingCitation():
    client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
    db = client['ncdb']
    collection = db['paper']
    results=collection.find({})
    for result in results:
        url = result['_id']
        para=result['introduction']
        sentences=splitSentence(para)
        for sentence in sentences:
            if ismention(sentence):
                db['cmention'].insert_one({"sentence": sentence,"ismention":1,"source": url,"part":"introduction","tag": 0})
            else:
                db['cmention'].insert_one({"sentence": sentence, "ismention": 0, "source": url, "part": "introduction","tag": 0})
        para = result['discussion']
        sentences = splitSentence(para)
        for sentence in sentences:
            if ismention(sentence):
                db['cmention'].insert_one(
                    {"sentence": sentence, "ismention": 1, "source": url, "part": "discussion", "tag": 0})
            else:
                db['cmention'].insert_one(
                    {"sentence": sentence, "ismention": 0, "source": url, "part": "discussion", "tag": 0})
        para = result['methods']
        sentences = splitSentence(para)
        for sentence in sentences:
            if ismention(sentence):
                db['cmention'].insert_one(
                    {"sentence": sentence, "ismention": 1, "source": url, "part": "methods", "tag": 0})
            else:
                db['cmention'].insert_one(
                    {"sentence": sentence, "ismention": 0, "source": url, "part": "methods", "tag": 0})
        para = result['results']
        sentences = splitSentence(para)
        for sentence in sentences:
            if ismention(sentence):
                db['cmention'].insert_one(
                    {"sentence": sentence, "ismention": 1, "source": url, "part": "results", "tag": 0})
            else:
                db['cmention'].insert_one(
                    {"sentence": sentence, "ismention": 0, "source": url, "part": "results", "tag": 0})

def ismention(sentence):
    pattern = re.compile("\[\d+\]")
    match = pattern.findall(sentence)
    for matchi in match:
        matchi = matchi.replace('[', '')
        matchi = matchi.replace(']', '')
        if matchi.isdigit():
            return True
    return False

GeneratingCitation()