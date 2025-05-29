
from flask import Flask, request, render_template
import cv2
import numpy as np
from your_model import analyze_chart

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    signal = entry = stop_loss = take_profit = comment = None

    if request.method == "POST":
        file = request.files["file"]
        comment = request.form.get("comment", "")
        img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
        signal, entry, stop_loss, take_profit = analyze_chart(img)

    return render_template("index.html", signal=signal, entry=entry, stop_loss=stop_loss, take_profit=take_profit, comment=comment)

if __name__ == "__main__":
    app.run(debug=True)
