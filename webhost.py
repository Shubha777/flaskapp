from flask import Flask, request, render_template
from prototype import maine
app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('lag.html')

@app.route('/', methods=['POST'])
def my_form_post():
    variable = request.form["nitasearch"]
    lol=maine(variable)
    return lol


if __name__ == "__main__":
    app.run(debug=True)