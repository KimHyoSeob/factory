from flask import Flask, render_template
import requests

app = Flask(__name__)

URL = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(URL)
data = response.json()


@app.route("/")
def home():
    return render_template("index.html", data=data)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<id>")
def post(id):
    title = data[int(id) - 1]["title"]
    subtitle = data[int(id) - 1]["subtitle"]
    body = data[int(id) - 1]["body"]
    return render_template("post.html", title=title, subtitle=subtitle, body=body)


if __name__ == "__main__":
    app.run(debug=True)
