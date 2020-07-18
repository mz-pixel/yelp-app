from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return"Hello World!"
    
my_port = 5000

app.run(host="127.0.0.1", port=my_port, debug=True)
