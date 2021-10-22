import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/detik-popular")
def detik_popular():
    response = requests.get("http://www.floatrates.com/daily/idr.json", params={"tag_from": "wp_cb_mostPopular_more"})
    soup = BeautifulSoup(response.text, "html.parser")
    popular_area = soup.find(attrs={"class": "grid-row list-content"})
    titles = popular_area.findAll(attrs={"class": "media__title"})
    images = popular_area.findAll(attrs={"class": "media__image"})
    return render_template("index.html", images=images)

@app.route("/floatrates-idr")
def floatrates_idr():
    response = requests.get("http://www.floatrates.com/daily/idr.json")
    json_data = response.json()
    return render_template("floatrates-idr.html", datas=json_data.values())


if __name__ == "__main__":
    app.run(debug=True)