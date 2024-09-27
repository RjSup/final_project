from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST', 'GET'])
def Home():
    data = request.get_json()
    user_text = data.get('text', '')
    slider_value = data.get('value', 0)

    message = f"You chose {slider_value}"

    modified_text = user_text.upper()
    
    print(data)

    return jsonify({'message': message})

if __name__ == '__main__':
    app.run(debug=True, port=5000)