from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h3>nice to meet you!</h3>'

if __name__=='__main__':
    app.run(debug = True)
