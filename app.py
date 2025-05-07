from flask import Flask, request, jsonify

app = Flask(__name__)

# Create an object to store data
data_store = []

@app.route("/")
def hello():
    return "Hello, Docker!???"  # You can add more exclamations here later to test live reload

@app.route("/add", methods=["POST"])
def add_data():
    # Get data from the POST request (JSON)
    data = request.get_json()

    # Add data to the data store (list in this case)
    data_store.append(data)
    
    # Respond with the updated list
    return jsonify({"message": "Data added successfully", "data": data_store}), 201

@app.route("/data", methods=["GET"])
def get_data():
    # Return the current data store as a response
    return jsonify({"data": data_store})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8001)  # Port 8001 for Docker Compose compatibility
