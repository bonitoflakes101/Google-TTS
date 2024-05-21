from google.cloud import texttospeech
from playsound import playsound

class GoogleCloudTextToSpeech:
    def __init__(self, credentials_path):
        self.credentials_path = credentials_path
        self.client = texttospeech.TextToSpeechClient()

    # transforms given text input from AI to MP3 file
    def synthesize_speech(self, text_to_speak, output_path):
        input_text = texttospeech.SynthesisInput(text=text_to_speak)

        voice = texttospeech.VoiceSelectionParams(
            language_code="en-US",
            name="en-US-Studio-O",
        )

        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3,
            speaking_rate=1
        )

        response = self.client.synthesize_speech(
            request={"input": input_text, "voice": voice, "audio_config": audio_config}
        )

        with open(output_path, "wb") as out:
            out.write(response.audio_content)
            print(f'Audio content written to file "{output_path}"')

    # this just plays that MP3 file
    def play_audio(self, output_path):
        playsound(output_path)

# example usage, lagay sa main file:
if __name__ == "__main__":
    credentials_path = r"C:\Users\xiang\Downloads\prac-423707-4b3eb9019a6f.json" # replace this with your own credentials path, yung json file na pina download ko
    tts = GoogleCloudTextToSpeech(credentials_path)

    text_to_speak = "TEST SPEECH" # this should be the output of the AI 
    output_path = r"C:\Users\xiang\VSCProjects\TTS_googlecloud\output.mp3" # replace this kung san mo gusto ma-write yung mp3 file. 

    tts.synthesize_speech(text_to_speak, output_path) # transforms text to mp3 file
    tts.play_audio(output_path) # it plays the mp3 file
