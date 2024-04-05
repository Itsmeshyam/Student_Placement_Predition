from flask import Flask, request, render_template
from prediction import Predictions
import os

des = os.path.abspath('templates')

app = Flask(__name__)


@app.route("/")
def intro():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            age = int(request.form.get("age"))
            internships = int(request.form.get("internships"))
            cgpa = int(request.form.get("cgpa"))
            stream = int(request.form.get("stream"))
            historyofbacklogs = int(request.form.get("historyofbacklogs"))

            p = Predictions(age, internships, cgpa, stream, historyofbacklogs)
            predic = p.predict()

            return render_template('results.html', predic=predic)

        except Exception as e:

            print("The exception has raised", e)
            return "Something went wrong :("

    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
