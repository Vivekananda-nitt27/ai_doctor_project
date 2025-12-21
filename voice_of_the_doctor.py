from elevenlabs.client import ElevenLabs
from elevenlabs import save
import os

client = ElevenLabs(
    api_key=os.getenv("ELEVENLABS_API_KEY")
)

def text_to_speech_with_elevenlabs(text, output_path="doctor_voice.mp3"):
    audio = client.text_to_speech.convert(
        voice_id="21m00Tcm4TlvDq8ikWAM",  
        model_id="eleven_turbo_v2_5",    
        text=text
    )

    save(audio, output_path)
    return output_path
