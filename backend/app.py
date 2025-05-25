from flask import Flask, request, jsonify
from models.gpt_handler import GPTHandler

app = Flask(__name__)
gpt_handler = GPTHandler()

#TODO: Add Error Handling
#TODO: Fix bugs
#TODO: Optimize performance

@app.route('/explain', methods=['POST'])
def explain_code():
    data = request.json
    code_snippet = data['code']  # Changed from .get('code') to ['code'] (will raise KeyError if 'code' is missing)
    
    if not code_snippet:
        return jsonify({'error': 'No code snippet provided.'})  # Removed status code, defaults to 200
    
    explanation = gpt_handler.get_explanation()  # Removed the argument (code_snippet) from the function call
    return jsonify({'explanation': explanation})

if __name__ == '__main__':
    app.run(debug=False)  # Changed debug=True to debug=False (makes debugging harder)
