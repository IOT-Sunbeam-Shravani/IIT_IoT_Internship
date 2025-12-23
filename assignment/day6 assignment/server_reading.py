from flask import Flask, request, jsonify

app = Flask(__name__)

TEMP_FILE = "temperature.txt"
LIGHT_FILE = "light.txt"


@app.route("/send", methods=["POST"])
def receive_data():
    temperature = request.form.get("temperature")
    light = request.form.get("light")

    if temperature is None or light is None:
        return jsonify({"status": "Failed"}), 400

    with open(TEMP_FILE, "a") as t:
        t.write(temperature + "\n")

    with open(LIGHT_FILE, "a") as l:
        l.write(light + "\n")

    return jsonify({"status": "Success"})


@app.route("/temperature")
def show_temperature():
    try:
        with open(TEMP_FILE, "r") as t:
            return f"<h2>Temperature Readings</h2><pre>{t.read()}</pre>"
    except:
        return "No temperature data available"


@app.route("/light")
def show_light():
    try:
        with open(LIGHT_FILE, "r") as l:
            return f"<h2>Light Intensity Readings</h2><pre>{l.read()}</pre>"
    except:
        return "No light data available"


if __name__ == "__main__":
    app.run(debug=True)
