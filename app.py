from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

cars = [
    {
        "id": 1,
        "brand": "Toyota",
        "location": "Bogotá",
        "applicant": "Carlos"
    }
]

@app.route("/api/cars", methods=["GET"])
def get_cars():
    return jsonify(cars)

@app.route("/api/cars", methods=["POST"])
def create_car():
    new_car = request.json
    new_car["id"] = len(cars) + 1
    cars.append(new_car)
    return jsonify(new_car)

@app.route("/api/cars/<int:id>", methods=["PUT"])
def update_car(id):
    for car in cars:
        if car["id"] == id:
            car.update(request.json)
            return jsonify(car)
    return jsonify({"message": "Car not found"}), 404

@app.route("/api/cars/<int:id>", methods=["DELETE"])
def delete_car(id):
    global cars
    car_exists = any(car["id"] == id for car in cars)

    if not car_exists:
        return jsonify({"message": "Car not found"}), 404

    cars = [car for car in cars if car["id"] != id]
    return jsonify({"message": "Car deleted"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)