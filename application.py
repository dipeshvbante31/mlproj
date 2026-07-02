import pickle
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

# Load model and scaler
ridge_model = pickle.load(open("models/ridge.pkl", "rb"))
standard_scaler = pickle.load(open("models/scaler.pkl", "rb"))


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predictdata", methods=["GET", "POST"])
def predict_datapoint():

    if request.method == "POST":
        try:
            temperature = float(request.form["Temperature"])
            rh = float(request.form["RH"])
            ws = float(request.form["WS"])
            rain = float(request.form["Rain"])
            ffmc = float(request.form["FFMC"])
            dmc = float(request.form["DMC"])
            isi = float(request.form["ISI"])
            classes = float(request.form["Classes"])
            region = float(request.form["Region"])

            # IMPORTANT:
            # These column names and order must match your training data.
            data = pd.DataFrame({
                "Temperature": [temperature],
                "RH": [rh],
                "Ws": [ws],          # Use "WS" instead if your training column was "WS"
                "Rain": [rain],
                "FFMC": [ffmc],
                "DMC": [dmc],
                "ISI": [isi],
                "Classes": [classes],
                "Region": [region]
            })

            scaled_data = standard_scaler.transform(data)
            prediction = ridge_model.predict(scaled_data)[0]

            return render_template(
                "home.html",
                prediction_text=f"Predicted Fire Weather Index (FWI): {prediction:.2f}"
            )

        except Exception as e:
            return render_template(
                "home.html",
                prediction_text=f"Error: {e}"
            )

    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)