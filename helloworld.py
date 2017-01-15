from flask iport Flask
app = Flask[__name__]

@app.route('/')
def index():
    return 'alert("nice to meet you!")'

if __name__=='__main__':
    app.run(debug = True)
