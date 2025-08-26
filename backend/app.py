from flask import Flask, render_template, jsonify
import data_fetcher

app = Flask(
    __name__,
    template_folder="../frontend",
    static_folder="../frontend",
    static_url_path="/static"
)

@app.route("/")
def home():
    return render_template("index.html")

# 🔹 This is the missing API route
@app.route("/api/stock/<ticker>")
def stock_api(ticker):
    data = data_fetcher.get_stock_data(ticker)
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
