# transcribeAPI

## Whisper Tiny.en API

A Flask-based API for transcribing audio and video files using OpenAI's Whisper `tiny.en` model.

## Features
- Accepts audio or video files for transcription.
- Uses Whisper's `tiny.en` model for efficient transcription in English.
- Provides word-level timestamps for the transcription.
- Supports CORS for easy integration with frontend applications.

## Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

## Installation

1. Clone the repository or copy the files into your project folder.
   ```bash
   git clone <repository_url>
   cd <project_folder>
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Make sure PyTorch is installed for your environment (CPU/GPU). If not, install it using:

bash
Copy code
pip install torch
Running the API
Start the Flask server:

bash
Copy code
python main.py
The server will run on http://127.0.0.1:5000 by default.

API Endpoints
POST /transcribe
Description
Transcribes an audio or video file and returns the transcription result along with word-level timestamps.

Request
Method: POST
Headers: None
Body: Multipart form-data with the following field:
file: The audio or video file to transcribe (e.g., .mp3, .mp4).
Response
Status 200: JSON object containing the transcription result.
Status 400: Error message if no file is provided.
Status 500: Error message if an internal error occurs.
Example Request Using curl
bash
Copy code
curl -X POST -F "file=@your_audio_or_video_file.mp4" http://127.0.0.1:5000/transcribe
Example Request Using Postman
Select POST method.
Set the URL to http://127.0.0.1:5000/transcribe.
In the Body tab, choose form-data and upload the file with the key file.
Send the request.
Example Response
json
Copy code
{
  "text": "This is an example transcription.",
  "segments": [
    {
      "id": 0,
      "start": 0.0,
      "end": 5.0,
      "text": "This is an example transcription.",
      "words": [
        {"word": "This", "start": 0.0, "end": 0.5},
        {"word": "is", "start": 0.5, "end": 1.0},
        {"word": "an", "start": 1.0, "end": 1.5},
        {"word": "example", "start": 1.5, "end": 2.5},
        {"word": "transcription", "start": 2.5, "end": 3.0}
      ]
    }
  ],
  "language": "en"
}
Notes
The Whisper tiny.en model is lightweight and optimized for English-only transcription tasks. If you need support for other languages or higher accuracy, consider switching to larger Whisper models.
Deployment
For deployment in a production environment:

Use a WSGI server like Gunicorn:
bash
Copy code
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 main:app
Configure reverse proxy (e.g., Nginx) for better performance and security.
License
This project uses Whisper under the OpenAI license. Please ensure compliance with OpenAI's terms and conditions.

Contributing
Feel free to fork and contribute to this project. Submit a pull request or report issues for improvements.

Acknowledgments
OpenAI Whisper
Flask for building the API
Flask-CORS for CORS support
yaml
Copy code

---

This README provides detailed instructions for installing, running, and using the API, along with example requests and responses. Let me know if you'd like additional sections or modifications!





