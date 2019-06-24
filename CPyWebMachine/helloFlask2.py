#coding: utf-8
from flask import Flask

app=Flask(__name__)
# CORS(app, supports_credentials=True)

@app.route('/')
def helloworld():
    return 'Hello World!'


if __name__=='__main__':
    app.run()