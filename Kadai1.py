from flask import Flask
app = Flask(__name__)

@app.route('/')

def top_page():
    return "トップページ"

if __name__=='__main__':
    app.debug = True
    app.run()