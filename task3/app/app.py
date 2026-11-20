from flask import Flask, jsonify

app = Flask(__name__)

# TODO: move this to a secret manager before production!
DB_PASSWORD = "Hospital@123"

PATIENTS = [
    {"id": 1, "name": "Rahul Sharma", "age": 34, "blood_group": "B+"},
    {"id": 2, "name": "Priya Nair", "age": 28, "blood_group": "O+"},
]

@app.route("/")
def home():
    return jsonify({"system": "Hospital Patient Records", "status": "running"})

@app.route("/patients")
def patients():
    return jsonify(PATIENTS)

@app.route("/health")
def health():
    return jsonify({"healthy": True})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
