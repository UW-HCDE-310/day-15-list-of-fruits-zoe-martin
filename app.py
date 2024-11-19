from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def index():
    fruits = [
        {"name": "apples", "quantity": 3},
            {"name": "oranges", "quantity": 2},
            {"name": "strawberries", "quantity": 6}
    ]
    o_fruits = [fruit for fruit in fruits if fruit["name"].startswith("o")]
    less_than_three_fruits = [fruit for fruit in fruits if fruit["quantity"] < 3]

    return render_template("index.html", fruits=o_fruits)
