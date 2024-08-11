# audio_to_text/converter.py

import os
import speech_recognition as sr
from pydub import AudioSegment

class AudioToTextConverter:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def convert(self, audio_file: str) -> str:
        """
        Converts an audio file to text.

        :param audio_file: Path to the audio file.
        :return: Transcribed text from the audio.
        """
        # Convert audio to WAV format if it's not already in that format
        if not audio_file.endswith(".wav"):
            audio_file = self._convert_to_wav(audio_file)

        with sr.AudioFile(audio_file) as source:
            audio = self.recognizer.record(source)
            try:
                text = self.recognizer.recognize_google(audio)
                return text
            except sr.UnknownValueError:
                return "Could not understand the audio."
            except sr.RequestError as e:
                return f"Could not request results from Google Speech Recognition service; {e}"

    def _convert_to_wav(self, audio_file: str) -> str:
        """
        Converts an audio file to WAV format.

        :param audio_file: Path to the audio file.
        :return: Path to the converted WAV file.
        """
        sound = AudioSegment.from_file(audio_file)
        wav_file = f"{os.path.splitext(audio_file)[0]}.wav"
        sound.export(wav_file, format="wav")
        return wav_file

