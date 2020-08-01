from flask import Flask, jsonify, request
from datetime import datetime, timedelta
import time
import sys
app = Flask(__name__)


usrname='ajaj'
passwd='heyhey'
x={}
y={}
req=3 #maximum number of requests allowed per user
@app.route('/', methods=['GET','POST'])
def get_tasks():
    if request.method=='GET':
        print(request.remote_addr)
        global req
        while(req>0):
            req-=1
            if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
                x={'ip': request.environ['REMOTE_ADDR'],'username':usrname,'passwd':passwd, 'timestamp':time.time()}
                print(x)
                print(req)
                return jsonify(x),200
            else:
                y={'ip':request.environ['HTTP_X_FORWARDED_FOR']}
                return jsonify({'ip': request.environ['HTTP_X_FORWARDED_FOR']}), 200
        else:
            return sys.exit()
    elif request.method=='POST':
        while(req>0):
            req-=1
            return 'success'
        else:
            return sys.exit()


if __name__ == '__main__':
    app.run(debug=True)
