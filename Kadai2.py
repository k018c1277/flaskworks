import datetime

from flask import Flask
app = Flask(__name__)

@app.route('/')

def kadai_time():
    t = datetime.datetime.now()
    t = t.strftime('%m/%d %H:%M')
    return t 

if __name__=='__main__':
    app.debug = True
    app.run()