import os
from flask import Flask, render_template, request
import cv2
import numpy as np

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    entry_point = stop_loss = take_profit = comment = ""
    if request.method == 'POST':
        file = request.files['screenshot']
        comment = request.form.get('comment', '')
        if file:
            image = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
            avg_brightness = np.mean(image)
            if avg_brightness > 127:
                prediction = "BUY"
                entry_point = "Entry: current price - 0.0050"
                stop_loss = "SL: current price - 0.0100"
                take_profit = "TP: current price + 0.0200"
            else:
                prediction = "SELL"
                entry_point = "Entry: current price + 0.0050"
                stop_loss = "SL: current price + 0.0100"
                take_profit = "TP: current price - 0.0200"
    return render_template('index.html',
                           prediction=prediction,
                           comment=comment,
                           entry_point=entry_point,
                           stop_loss=stop_loss,
                           take_profit=take_profit)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
