<thml>
    <head>
        <meta charset="UTF-8">
    </head>
    
        <body>
            <h1>70点以上の科目</h1>
            <h2>
                {% for l in list %}
                    {% if list[l] >= 70 %}
                        {{ l }}
                    {% endif %}
                {% endfor %}
            </h2>
        </body>
    </thml>

    

    from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    list =  {'英語': 87, '数学': 90, '国語': 45, '理科': 75, '社会': 31}

    
if __name__ == '__main__' :
    app.debug = True
    app.run()