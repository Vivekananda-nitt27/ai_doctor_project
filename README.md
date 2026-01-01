🩺 AI Doctor – Vision & Voice Based Medical Assistant

An end-to-end AI Doctor application that takes patient voice input and medical images, analyzes them using multimodal AI models, and responds with a natural doctor-like voice.
The system is deployed and running on AWS EC2 with a Gradio web interface.

🚀 Project Status

✅ Successfully deployed on AWS EC2

✅ Running in production

✅ Accessible via browser (Gradio UI)

🧠 What This Project Does

Records patient voice via microphone

Converts speech to text using Whisper

Analyzes uploaded medical images using vision-enabled LLM

Generates concise medical reasoning

Converts doctor response into realistic voice

Displays everything in a single interactive web app

🛠️ Tech Stack
Frontend / UI

Gradio

Speech Processing

SpeechRecognition

PyAudio

FFmpeg

AI & ML

Whisper Large v3 (Speech-to-Text via Groq)

LLaMA Vision Models (Image + Text Reasoning)

ElevenLabs (Text-to-Speech)

gTTS (Fallback TTS)

Backend

Python

Groq API

ElevenLabs API

Deployment

AWS EC2 (Linux)

Virtual Environment (venv)

Environment Variables (.env)

📂 Project Structure
doctor_ai/
│
├── brain_of_the_doctor.py      # Image + LLM reasoning
├── voice_of_the_patient.py    # Audio recording & transcription
├── voice_of_the_doctor.py     # Text-to-Speech logic
├── gradio_app.py              # Gradio UI entry point
├── requirements.txt
├── README.md
└── .gitignore

🧩 Component Breakdown
🎙️ Voice of the Patient

Records patient speech

Converts audio to MP3

Transcribes speech using Whisper Large v3

🧠 Brain of the Doctor

Encodes medical images

Sends image + patient text to LLM

Generates human-like medical responses

Avoids AI disclaimers and markdown

🔊 Voice of the Doctor

Converts text response to speech

Uses ElevenLabs for realistic output

Supports autoplay in UI

🖥️ Gradio Interface

Microphone input

Image upload

Text output (STT + Doctor response)

Audio playback (Doctor voice)

🔐 Environment Variables

Create a .env file:

GROQ_API_KEY=your_groq_api_key
ELEVEN_API_KEY=your_elevenlabs_api_key


⚠️ Do not upload .env to GitHub.

▶️ How to Run Locally
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
python gradio_app.py


App runs at:

http://127.0.0.1:7860

☁️ Deployment (AWS EC2)

Ubuntu EC2 instance

Python + FFmpeg installed

Environment variables configured

Gradio app running continuously

⚠️ Disclaimer

This project is built only for educational and learning purposes.
It does not replace professional medical advice.

⭐ Key Highlights

Multimodal AI (Voice + Vision)

Real-time medical reasoning

Natural doctor-like voice responses

Modular & scalable architecture

Production deployment on AWS EC2
