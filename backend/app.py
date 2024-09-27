from flask import Flask, request, jsonify
from flask_cors import CORS
# for communicating with algorithm import joblib

app = Flask(__name__)
CORS(app)

# Load the machine learning model
# model = joblib.load('model.joblib')

@app.route('/', methods=['POST', 'GET'])
def getSliderInfo():
    data = request.get_json()
    slider_value = data.get('sliderValue', None)
    investment_amount = data.get('investmentAmount', None)

    if slider_value is not None:
        message = f"You chose {slider_value}"
        print(data)
        return jsonify({'message': message})
        # send the data to the machine learning model
    

    elif investment_amount is not None and investment_amount > 0:
        message = f"Your investment amount is £{investment_amount}."
        print(data)
        return jsonify({'message': message})
        # send the data to the machine learning model
    

    else:
        message = "No valid data provided"
        print(data)
        return jsonify({'message': message})


if __name__ == '__main__':
    app.run(debug=True, port=5000)