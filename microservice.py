from flask import Flask, request, jsonify

app = Flask(__name__)

API_KEY = "2f5ae96c-b558-4c7b-a590-a501ae1c3f6c"

@app.route('/DevOps', methods=['POST'])
def devops():
    api_key = request.headers.get('X-Parse-REST-API-Key')
    
    if api_key != API_KEY:
        return "ERROR", 401
    
    data = request.json
    message = f"Hello {data['to']} your message will be sent"
    
    return jsonify({"message": message})

@app.route('/DevOps', methods=['GET', 'PUT', 'DELETE'])
def not_allowed():
    return "ERROR", 405

if __name__ == '__main__':
    app.run(debug=True)
