from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title="タイトル")

if __name__ == '__main__' :
    app.debug = True
    app.run()