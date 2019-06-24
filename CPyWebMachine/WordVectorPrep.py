from gensim.models import word2vec

sentences=word2vec.Text8Corpus("./data/ncdb.paper.csv")
model=word2vec.Word2Vec(sentences,sg=0,min_count=1,workers=4)
model.save("D:/GeoSemantics/PythonWKSP/CPyWebMachine/data/"+"w2v.m")
# model=Word2Vec(sentences, sg=1, size=100,  window=5,  min_count=5,  negative=3, sample=0.001, hs=1, workers=4)
