# Install the assemblyai package by executing the command "pip install assemblyai"

# Come to this later

import assemblyai as aai

aai.settings.api_key = "12d38a465e2648889e760ef08a15ca12"

# audio_file = "./local_file.mp3"
audio_file = "https://assembly.ai/wildfires.mp3"

config = aai.TranscriptionConfig(speech_model=aai.SpeechModel.universal)

transcript = aai.Transcriber(config=config).transcribe(audio_file)

if transcript.status == "error":
  raise RuntimeError(f"Transcription failed: {transcript.error}")

print(transcript.text)