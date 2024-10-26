from flask import Blueprint, jsonify, request
from .ml.predictor import predict_peak_hours, recommend_stations


import openai
from flask import Flask, request, jsonify

app = Flask(__name__)

# Set your OpenAI API key here
openai.api_key = "YOUR_OPENAI_API_KEY"

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_input = request.json.get("message")
    
    try:
        # Call OpenAI API to get a response
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=50
        )
        
        # Extract the chatbot's response
        bot_response = response.choices[0].text.strip()
    except Exception as e:
        bot_response = "I'm having trouble processing that request."

    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)


@bp.route('/api/predict', methods=['POST'])
def predict():
    data = request.json
    # Assuming data contains historical usage data
    prediction = predict_peak_hours(data)
    return jsonify(prediction)

@bp.route('/api/recommend', methods=['POST'])
def recommend():
    user_data = request.json
    recommendations = recommend_stations(user_data)
    return jsonify(recommendations)

def setup_routes(app):
    @app.route("/")
    def home():
        return jsonify({"message": "Welcome to the Connected Charging Station API"})

    @app.route("/predict_demand", methods=["POST"])
    def predict_demand():
        data = request.get_json()
        time = data.get("time", 1)  # Default to 1 if "time" is not provided
        prediction = ml_predict_demand(time)  # Call the ML prediction function
        # Call the prediction function from `predictor.py` here
        result = {"prediction": "Placeholder for ML model prediction"}
        return jsonify(result)
