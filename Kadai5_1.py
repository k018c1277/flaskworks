from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
        return render_template('Kadai5_1index.html')

@app.route('/send', methods=['GET', 'POST'])
def send():
        name = request.form.get('name')
        email = request.form.get('email')
        if name is None:
            name = ''
            email = ''
        return render_template('Kadai5_1receive.html', name=name, email=email)

if __name__ == '__main__':
    app.debug = True
    app.run()