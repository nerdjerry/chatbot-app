from flask import Flask, request, jsonify
from models.gpt_handler import GPTHandler

app = Flask(__name__)
gpt_handler = GPTHandler()

"""@app.route('/explain', methods=['POST'])
def explain_code():
    data = request.json
    code_snippet = data.get('code')
    
    if not code_snippet:
        return jsonify({'error': 'No code snippet provided.'}), 400
    
    #TODO: Add Error Handling
    explanation = gpt_handler.get_explanation(code_snippet)
    return jsonify({'explanation': explanation})"""

@app.route('/explain', methods=['POST'])
def explain_code():
    data = request.json
    code_snippet = data.get('code')
    
    if not code_snippet:
        return jsonify({'error': 'No code snippet provided.'}), 400
    
    try:
        explanation = gpt_handler.get_explanation(code_snippet)
        if "Error" in explanation:
            return jsonify({'error': explanation}), 500
        return jsonify({'explanation': explanation})
    except Exception as e:
        return jsonify({'error': f"Internal server error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)