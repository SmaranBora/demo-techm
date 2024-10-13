import google.generativeai as genai
from flask import Flask, request, jsonify
import os

# Initialize Flask app
app = Flask(__name__)

api_key = "AIzaSyDlcimacAhUz5v5G1fJsEDX4_7yA3H7BE0"
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

def optimize_code(code: str) -> str:
    # Generate optimized code
    prompt = f"Convert the following code to green optimized code:\n\n{code}\n\nOptimized Code:"
    response = model.generate_content(prompt)
    return response.text

@app.route('/optimize', methods=['POST'])
def optimize():
    # Get the JSON data from the request
    data = request.get_json()
    code = data.get('code', '')

    # Check if code is provided
    if not code:
        return jsonify({"error": "No code provided"}), 400

    # Get optimized code
    optimized_code = optimize_code(code)

    # Return the optimized code in JSON format
    return jsonify({"optimized_code": optimized_code})

if __name__ == '__main__':
    app.run(debug=True)