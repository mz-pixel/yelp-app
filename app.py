from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    # we need to return a page
    return render_template("index.html")
    
my_port = 5000

app.run(host="127.0.0.1", port=my_port, debug=False)

