#/usr/bin/python3

from flask import Flask, jsonify, request, session, app
from datetime import datetime, timedelta
import time
import sys
import schedule
import datetime

app = Flask(__name__)

blacklisted_ip=[]
usrname='<username>' #Take this as form input if you want (hard coded for now)
passwd='<password>'  #Take this as form input if you want (hard coded for now)
x={} # Stores the fields for the GET requests
req=3 #maximum number of requests allowed per user, alter this according to your own convenience.
header_vals=[] # stores the HTTP header USER AGENT


@app.route('/', methods=['GET','POST'])
def get_tasks():
    if request.method=='GET' and request.environ['REMOTE_ADDR'] not in blacklisted_ip:
        hc=request.environ['HTTP_USER_AGENT']
        if hc not in header_vals:
            header_vals.append(hc)
        if hc in header_vals:
            global req
            while(req>0):
                req-=1
                if request.environ['REMOTE_ADDR'] is not None:
                    x={'ip': request.environ['REMOTE_ADDR'],'username':usrname,'passwd':passwd, 'timestamp':time.time()}
                    #print(x)
                    #print(req)
                    #print(header_vals)
                    return jsonify(x),200
                else:
                    x={'ip':request.environ['HTTP_X_FORWARDED_FOR']}
                    return jsonify({'ip': request.environ['HTTP_X_FORWARDED_FOR']}), 200
            else:
                t=request.environ['REMOTE_ADDR']
                if t not in blacklisted_ip:
                    blacklisted_ip.append(t)
                #print(blacklisted_ip)
            
                return sys.exit()

    
    elif request.method=='POST':
        while(req>0):
            req-=1
            return 'success',200
        else:
            t=request.environ['REMOTE_ADDR']
            if t not in blacklisted_ip:
                blacklisted_ip.append(t)
            #print(blacklisted_ip)
            
            return sys.exit()

    else:
        return sys.exit()  


if __name__ == '__main__':
    app.run(debug=True)
