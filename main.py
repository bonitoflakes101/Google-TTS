from google.cloud import texttospeech
import os
from playsound import playsound

# replace directory with your own
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"C:\Users\xiang\Downloads\prac-423707-4b3eb9019a6f.json"
client = texttospeech.TextToSpeechClient()

# put output text from AI here
text_to_speak = "THANK GOD IT'S WORKING"
input_text = texttospeech.SynthesisInput(text=text_to_speak)

voice = texttospeech.VoiceSelectionParams(
    language_code="en-US",
    name="en-US-Studio-O",
)

# use MP3 encoding since we are saving as MP3
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3,
    speaking_rate=1
)

response = client.synthesize_speech(
    request={"input": input_text, "voice": voice, "audio_config": audio_config}
)

# The response's audio_content is binary.
output_path = r"C:\Users\xiang\VSCProjects\TTS_googlecloud\output.mp3"
with open(output_path, "wb") as out:
    out.write(response.audio_content)
    print(f'Audio content written to file "{output_path}"')

# plays the mp3 file 
playsound(output_path)
