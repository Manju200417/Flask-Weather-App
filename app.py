from flask import Flask,render_template,request
import requests as re
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def main():
    weather = None
    error = None

    try:
        if request.method == "POST":
            city =  (request.form["city"]).title().strip()
            if city:
                    URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
                    res = re.get(URL)
                    if res.status_code == 200:
                        data = res.json()
                        weather = {
                            "city" : data["name"],
                            "Temperature" : data["main"]["temp"],
                            "Humidity" : data["main"]["humidity"],
                            "Wind_Speed" : data["wind"]["speed"]
                        }
                    else : error = "City not found. Please enter a valid city."

            else : error = "Please Enter City Name!!!"

    except Exception as e:
        error = e
        print("Error :",e)

    return render_template('index.html',weather = weather,error = error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)



