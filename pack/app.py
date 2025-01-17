from flask import Flask, request, jsonify
from transformers import pipeline
import re


app = Flask(__name__)
pipe = pipeline("text-generation", model="Qwen/Qwen2.5-Coder-1.5B-Instruct", device=-1)
@app.route('/optimize', methods=['POST'])
def optimize():
    # Get data from the POST request
    data = request.json
    input_code = data.get("code")
    optimization_goal = data.get(
        "goal",
        "Optimize the following code to reduce time complexity, remove unnecessary steps, improve performance, reduce space, and minimize energy consumption. Focus on eliminating redundant operations, using more efficient algorithms, and optimizing memory usage."
    )

    if not input_code:
        return jsonify({"error": "No code provided"}), 400

    # Generate optimized code based on the input and goal
    prompt = f"Optimize the following code to {optimization_goal}. Return only the optimized code without any explanations or comments:\n\n{input_code}\n\nOptimized Code:\n"
    response = pipe(prompt, max_new_tokens=300)
    generated_text = response[0]["generated_text"]

    # Extract only the optimized code
    match = re.search(r"Optimized Code:\s*(```python)?(.*?)(```|\Z|Explanation:|Additionally|This optimized code)", generated_text, re.DOTALL)
    optimized_code = match.group(2).strip() if match else generated_text.strip()

    return jsonify({"optimized_code": optimized_code})

if __name__ == "__main__":
    # Listen on all network interfaces
    app.run(host="0.0.0.0", port=5000)

