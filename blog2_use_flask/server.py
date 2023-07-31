from flask import Flask, render_template, request
import requests
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

URL = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(URL)
data = response.json()

EMAIL = ""  # 보안
PW = ""  # 보안


@app.route("/")
def home():
    return render_template("index.html", data=data)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        messaget = request.form["message"]
        sendeamil(name, email, phone, messaget)
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def sendeamil(name, email, phone, messaget):
    message = EmailMessage()
    messaget = f"내용 : {messaget}\n이름 : {name}\n발신자 : {email}\n핸드폰 번호 : {phone}"
    message.set_content(messaget)
    message["Subject"] = "블로그 컨택 메시지"
    message["From"] = "블로그"
    message["to"] = ""  # 보안
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PW)
        connection.send_message(message)


@app.route("/post/<id>")
def post(id):
    title = data[int(id) - 1]["title"]
    subtitle = data[int(id) - 1]["subtitle"]
    body = data[int(id) - 1]["body"]
    return render_template("post.html", title=title, subtitle=subtitle, body=body)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="80", debug=True)
