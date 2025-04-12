from flask import Flask, request, render_template
from services import UPITrustService, LoadDBService as db

app = Flask(__name__)

@app.route('/')
def home():
    db.load()
    return render_template('index.html');

@app.route('/safescan-result', methods=["POST"])
def fetchResults():
    upiId = request.form.get('upi-id')
    response = UPITrustService.validateUPI(upiId)
    return render_template('results.html', resp = response)

if __name__ == "__main__":
    app.run(debug=True)