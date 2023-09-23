import flask
from flask import Flask, redirect, url_for, render_template, request


app = Flask(__name__)


def prod_calculator1(a,b):
    result=None
    if request.method == 'POST':
        a = float(request.form['num1'])
        b = float(request.form['num2'])
        result = a * b
    return result


@app.route("/", methods=["GET","POST"])
def welcome():
    return "Welcome to Login system"


@app.route('/product', methods=["GET","POST"])
def prod_calculator():
    result=None
    if request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        result = num1 * num2

    return render_template('home.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)


