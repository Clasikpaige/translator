# api/app.py
from flask import Flask, request, jsonify
import onmt.translate

app = Flask(__name)

# Load the trained model
translator = onmt.translate.Translator(model='path_to_trained_model/model_step_1000.pt', gpu=0)

@app.route('/translate', methods=['POST'])
def translate():
    urhobo_text = request.json['urhobo_text']
    
    # Translate the Urhobo text to English
    translation = translator.translate(urhobo_text)
    
    return jsonify({'english_translation': translation})

if __name__ == '__main__':
    app.run(debug=True)
