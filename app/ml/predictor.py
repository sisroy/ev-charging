import numpy as np
from sklearn.linear_model import LinearRegression
import numpy as np


# Dummy data for demonstration
def train_model():
    # Here we use some dummy data to train a basic Linear Regression model.
    X = np.array([[1], [2], [3], [4], [5]])  # Example time (in hours)
    y = np.array([2, 4, 6, 8, 10])  # Demand at each time
    model = LinearRegression()
    model.fit(X, y)
    return model

def predict_demand(time):
    model = train_model()  # In production, this model should be pre-trained and loaded
    prediction = model.predict(np.array([[time]]))
    return prediction[0]

def predictt_peak_hours(data):
    # Placeholder for your predictive model logic
    # For example, you could load a trained model and make predictions
    # Here we just return a dummy response
    return {
        "peak_hours": ["18:00", "19:00", "0:00"],
        "suggested_time": "21:00"
    }

