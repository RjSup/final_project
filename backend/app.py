from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
# Link front end and backend
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})

# Load the machine learning model
# model = joblib.load('model.joblib')


@app.route('/', methods=['POST', 'GET'])
def Home():
    data = request.get_json()
    slider_value = data.get('sliderValue', None)
    investment_amount = data.get('investmentAmount', None)
    
    if slider_value is not None:
        message = f"You chose {slider_value}"
        print(data)
        return jsonify({'message': message})
    elif investment_amount is not None:
        message = f"Your investment amount is £{investment_amount}."
        print(data)
        return jsonify({'message': message})
    else:
        message = "No valid data provided"
        print(data)
        return jsonify({'message': message})
    
    

@app.route('/Dashboard', methods=['POST', 'GET'])
def dashboard():
    # return dashboard page from svelte
    return send_from_directory('build', 'frontend/src/routes/Dashboard/+page.svelte')


if __name__ == '__main__':
    app.run(debug=True, port=5173)