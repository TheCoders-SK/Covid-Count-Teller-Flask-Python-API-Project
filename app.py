from flask import Flask, render_template, request
import requests
import json

url = "https://disease.sh/v3/covid-19/all"
response = requests.get(url).text
json_response = json.loads(response)

count_today = json_response["cases"]
count_today = f"{count_today:,d}"
count_total = json_response["updated"]
count_total = f"{count_total:,d}"
count_recoverd_today = json_response["recovered"]
count_recoverd_today = f"{count_recoverd_today:,d}"
count_death_total = json_response["deaths"]
count_death_total = f"{count_death_total:,d}"
count_death = json_response["todayDeaths"]
count_death = f"{count_death:,d}"

app = Flask(__name__)


@app.route("/")
def main():
    return render_template(
        "home.html",
        count_today=count_today,
        count_total=count_total,
        count_recoverd_today=count_recoverd_today,
        count_death_total=count_death_total,
        count_death=count_death,
    )
