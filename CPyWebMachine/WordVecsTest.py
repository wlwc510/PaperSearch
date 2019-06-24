from gensim.models import word2vec

# model=word2vec.Word2Vec.load('./data/w2v.m')
# print(model.wv.similar_by_word('DNA',topn=30))

def getMostSimilarTop3(input):
    model = word2vec.Word2Vec.load('./data/w2v.m')
    return model.wv.similar_by_word(input,topn=3)

