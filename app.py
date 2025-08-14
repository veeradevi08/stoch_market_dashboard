from flask import Flask, jsonify
from flask_cors import CORS
import datetime
import random

app = Flask(__name__)
CORS(app)  # Enable CORS so frontend can call API

# Example route to get stock data
@app.route('/api/stock-data', methods=['GET'])
def get_stock_data():
    # Simulating stock price data
    stocks = ["AAPL", "TSLA", "AMZN", "MSFT", "GOOG"]
    data = []

    for stock in stocks:
        data.append({
            "symbol": stock,
            "price": round(random.uniform(100, 2000), 2),
            "change": round(random.uniform(-5, 5), 2),
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
