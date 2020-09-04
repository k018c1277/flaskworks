from flask import Flask, render_template

app = Flask(__name__)

data = []

@app.route('/user/<id>/')
def adduser(id):
        data.append(id)
        return render_template('index.html', user=id)

@app.route('/list/')
def userlist():
        return render_template('list.html',  list=data)

if __name__ == '__main__':
    app.debug = True
    app.run()