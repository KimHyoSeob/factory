from flask import Flask, render_template
from post import Post

app = Flask(__name__)


pdata = Post()
data = pdata.blog_data


@app.route("/")
def home():
    return render_template("index.html", data=data)


@app.route("/post/<id>")
def post(id):
    title = data[int(id) - 1]["title"]
    subtitle = data[int(id) - 1]["subtitle"]
    body = data[int(id) - 1]["body"]
    return render_template("post.html", title=title, subtitle=subtitle, body=body)


if __name__ == "__main__":
    app.run(debug=True)
