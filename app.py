from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import requests
from io import StringIO  # Import StringIO from io module

# Initialize FastAPI app
app = FastAPI()

# Define the request body model
class PredictRequest(BaseModel):
    feature: float

# Sample data URL (replace with an actual public dataset API)
DATA_URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"

# Load and preprocess the dataset
def load_data():
    response = requests.get(DATA_URL)
    data = pd.read_csv(StringIO(response.text))  # Use StringIO from io module
    # Using 'total_bill' to predict 'tip'
    X = data[['total_bill']]
    y = data['tip']
    return train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Linear Regression model
X_train, X_test, y_train, y_test = load_data()
model = LinearRegression()
model.fit(X_train, y_train)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Linear Regression API!"}

@app.post("/predict/")
def predict(data: PredictRequest):
    # Make prediction
    feature_array = np.array(data.feature).reshape(-1, 1)
    prediction = model.predict(feature_array)
    return {"prediction": prediction[0]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080)
