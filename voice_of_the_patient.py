from dotenv import load_dotenv
load_dotenv()

from groq import Groq

def transcribe_with_groq(audio_filepath, stt_model="whisper-large-v3"):
    client = Groq()  # auto-loads GROQ_API_KEY

    with open(audio_filepath, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            model=stt_model,
            file=audio_file,
            language="en"
        )

    return transcription.text
