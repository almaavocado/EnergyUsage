from flask import Flask, jsonify, request
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/sites', methods=['GET'])
def get_sites():
    try:
        api_key = request.headers.get('X-Voltus-API-Key')
        response = requests.get('https://sandbox.voltus.co/2022-04-15/sites', headers={'X-Voltus-API-Key': api_key})
        data = response.json()
        return jsonify({'sites': data['sites']})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run()
