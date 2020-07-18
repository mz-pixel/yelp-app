from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    # we need to return a page
    return render_template("index.html")

app.config['TEMPLATES_AUTO_RELOAD'] = True

my_port = 5000

app.run(host="0.0.0.0", port=my_port, debug=True, use_reloader=False)

