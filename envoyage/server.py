# python3 -m venv venv
# source venv/bin/activate
# pip3 install flask
# python3 server.py

from flask import render_template, request, Flask, redirect
from openingai import askAway

# INITIALIZE FLASK
app = Flask(__name__)

@app.route('/')
def show_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def process_form():
    global answer
    if request.method == 'POST':
        city = request.form['city']
        startDate = request.form['startDate']
        endDate = request.form['endDate']
        hobbies = request.form['hobbies']
        print(f"The city I want to go to is {city}. I will go on {startDate} and leave on {endDate}. My hobbies are {hobbies}")
        answer = askAway(city, startDate, endDate, hobbies)
        print(f"Envoyage: {answer}")
        return render_template("result.html", answer=answer)

if __name__ == '__main__':
    app.run(debug=True)