

**🩺 AI Doctor — Vision & Voice Powered Medical Assistant
🚀 Project Status**

✅ Successfully deployed on AWS EC2

✅ Running in production

✅ Browser-based interactive UI using Gradio

**🧠 Project Overview**

An end-to-end AI Doctor application that enables intelligent medical interaction using voice and images.
The system listens to a patient’s voice, analyzes optional medical images using multimodal AI, and responds with a natural, doctor-like voice.

**✨ Key Features**

🎙️ Voice-based patient interaction

🖼️ Medical image understanding with vision-enabled LLMs

🧾 Real-time speech-to-text transcription

🧠 Concise AI-powered medical reasoning

🔊 Natural doctor-like voice responses

🖥️ Unified web interface

🛠️ Technology Stack
🖥️ Frontend / UI

Gradio

🎧 Speech Processing

SpeechRecognition

PyAudio

FFmpeg

🤖 AI & Machine Learning

Whisper Large v3 (Speech-to-Text via Groq)

LLaMA Vision Models (Image + Text Reasoning)

ElevenLabs (Text-to-Speech)

gTTS (Fallback TTS)

⚙️ Backend

Python

Groq API

ElevenLabs API

☁️ Deployment

AWS EC2 (Linux)

Virtual Environment (venv)

Secure Environment Variables (.env)

**📂 Project Structure**
doctor_ai/
│
├── brain_of_the_doctor.py      # Image encoding & AI reasoning
├── voice_of_the_patient.py     # Audio recording & transcription
├── voice_of_the_doctor.py      # Text-to-Speech generation
├── gradio_app.py               # Gradio web interface
├── requirements.txt
├── README.md
└── .gitignore

🧩 System Components
🎙️ Voice of the Patient

Records patient speech via microphone

Converts audio into MP3 format

Transcribes speech using Whisper Large v3

🧠 Brain of the Doctor

Encodes uploaded medical images

Combines patient speech + image input

Generates concise, doctor-like medical responses

Avoids AI disclaimers and markdown formatting

🔊 Voice of the Doctor

Converts AI-generated medical responses into speech

Uses ElevenLabs for realistic voice output

Supports audio playback within the UI

🖥️ Gradio Web Interface

Microphone audio input

Medical image upload

Speech-to-text output

Doctor’s response display

Audio playback

🔐 Environment Variables

Create a .env file:

GROQ_API_KEY=your_groq_api_key
ELEVEN_API_KEY=your_elevenlabs_api_key


⚠️ Never commit .env to GitHub

▶️ Run Locally
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
python gradio_app.py


📍 Application URL: http://127.0.0.1:7860

☁️ Deployment on AWS EC2

Hosted on Linux-based EC2 instance

Python runtime with required dependencies

Environment variables securely configured

Application running continuously

⚠️ Disclaimer

This project is developed strictly for educational and learning purposes.
It does not replace professional medical advice, diagnosis, or treatment.

⭐ Project Highlights

Multimodal AI (Voice + Vision)

Real-time medical reasoning

Natural doctor-like voice responses

Modular and scalable architecture

Production deployment on AWS EC2

**📌 Intellectual Property Notice**

This project is shared for educational purposes only.
Commercial use, redistribution, or deployment without permission is not allowed.
