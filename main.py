from flask import Flask, request, jsonify
from flask_cors import CORS
import whisper
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the Whisper tiny.en model
model = whisper.load_model("tiny.en")

@app.route('/transcribe', methods=['POST'])
def transcribe():
    """
    Endpoint to transcribe an audio or video file using Whisper tiny.en model.
    """
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files['file']

    # Save the file temporarily
    temp_path = f"temp_{file.filename}"
    file.save(temp_path)

    try:
        # Transcribe the file
        result = model.transcribe(temp_path, language="en", word_timestamps=True)
        # Clean up the temporary file
        os.remove(temp_path)
        return jsonify(result), 200

    except Exception as e:
        # Clean up the temporary file in case of an error
        if os.path.exists(temp_path):
            os.remove(temp_path)
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
