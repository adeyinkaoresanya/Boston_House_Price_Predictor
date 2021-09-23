import numpy as np
from flask import Flask, request
import json
import pickle


app = Flask(__name__)

classifier = pickle.load(open('classifier.pkl', 'rb'))

def __process_input(request_data: str) -> np.array:
    '''
    This function preprocesses the request data by transforming it into 2D array the model accepts
    
    Args:
        request_data (str): JSON type data obtained from requests
        
    Returns:
        np.array: A 2-dimensional array of inputs

    '''
    parsed_body = np.asarray(json.loads(request_data)["inputs"])
    assert len(parsed_body.shape) == 2, "'inputs' must be a 2-d array"
    return parsed_body

@app.route('/', methods=['GET'])
def home():
    return ('Welcome to the Boston House Prediction Page')

# CREATING ROUTE FOR MODEL PREDICTION
@app.route("/predict", methods=["POST"])
def predict() -> str:
    '''
    This function feeds the request data to the model and returns the predicted values

    Returns:
        The predictions in JSON format
    '''
    try:
        
        input_params = __process_input(request.data)
        predictions = classifier.predict(input_params)
        return json.dumps({"Predicted House Price(s)": predictions.tolist()})
    except (KeyError, json.JSONDecodeError, AssertionError):
        return json.dumps({"error": "CHECK INPUT"}), 400
    except:
        return json.dumps({"error": "PREDICTION FAILED"}), 500

if "__name__" == "__main__":
    app.run(debug=True)