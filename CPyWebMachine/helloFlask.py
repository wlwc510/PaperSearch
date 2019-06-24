#coding: utf-8
from flask import Flask
from flask import request
from flask import jsonify, make_response
import json
from CollaborateFilter import CF_knearest
from CollaborateFilter import CF_svd
import numpy as np
from numpy import *
from MongoDBHelper import RatingPaper
from MongoDBHelper import getUserItemMatrix
from WordVecsTest import getMostSimilarTop3
from flask_cors import *

app=Flask(__name__)
CORS(app, supports_credentials=True)
# CORS(app, resources=r'/*')

# @app.after_request
# def cors(environ):
#     environ.headers['Access-Control-Allow-Origin']='*'
#     environ.headers['Access-Control-Allow-Method']='*'
#     environ.headers['Access-Control-Allow-Headers']='x-requested-with,content-type'
#     return environ

@app.route('/')
def helloworld():
    return 'Hello World!'

@app.route('/Search/<input>',methods=['GET','POST'])
def search(input):
    result=json.dumps(getMostSimilarTop30(input))
    return result

@app.route('/Rating',methods=['GET','POST'])
# @cross_origin()
def rating():
    result=""
    if request.method=='POST':
        data=request.get_data()
        json_data = json.loads(data.decode("utf-8"))
        uuid=json_data.get("uuid")
        score=json_data.get("score")
        paperid=json_data.get("paperid")
        print(RatingPaper(uuid,paperid,score))
        result_text = {"code": 200, "message": "更新数据成功"}
    else:
        print("err")
        result_text = {"code": 301, "message": "内部错误"}

    response = make_response(jsonify(result_text))
    return response





@app.route('/SearchPost',methods=['GET','POST'])
def searchPost():
    if request.method=='POST':
        data=request.data
        json_data=json.loads(data.decode("utf-8"))
        input=json_data.get("input")
        result=getMostSimilarTop3(input)
        result_text = {"code": 200, "message": "查询成功", "data":result}
    else:
        result_text = {"code": 400, "message": "失败"}
    return make_response(jsonify(result_text))

@app.route("/CF_knearest",methods=['GET','POST'])
def cfilter_knearest():
    # print("here")
    if request.method=='POST':
        data=request.data
        json_data=json.loads(data.decode("utf-8"))
        uuid=json_data.get("uuid")
        ratingMatrix, itmelist=getUserItemMatrix(uuid)
        cf=CF_knearest(k=1)
        re=cf.fit(np.array(ratingMatrix))

        # result=json.dumps(cf.fit(np.array(ratingMatrix)))
        result_text = {"code": 200, "message": "查询成功","data":str(re),"rep":itmelist[re[0][0]]}
    else:
        result_text = {"code": 400, "message": "失败"}
    return make_response(jsonify(result_text))

@app.route("/CF_svd",methods=['GET','POST'])
def cfilter_svd():
    # print("here")
    if request.method=='POST':
        data=request.data
        json_data=json.loads(data.decode("utf-8"))
        list_data=json_data.get("matrix")
        matrix_data=np.array(list_data)
        cf=CF_svd(k=1)
        result=json.dumps(cf.fit(matrix_data))
        result_text = {"code": 200, "message": "查询成功","data":result}
    else:
        result_text = {"code": 400, "message": "失败"}
    return make_response(jsonify(result_text))

if __name__=='__main__':
    app.run()