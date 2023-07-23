import streamlit as st
import os
import numpy as np
from io import BytesIO
import streamlit.components.v1 as components
from st_custom_components import st_audiorec
import whisper
import base64

def transcribe_audio(audio_data):
    # Decode base64 audio to bytes
    audio_bytes = base64.b64decode(audio_data)
    # Save audio to a .wav file
    with open("audio.wav", "wb") as audio_file:
        audio_file.write(audio_bytes)
    # Load the Whisper ASR model
    model = whisper.load_model("base")
    # Transcribe the audio
    result = model.transcribe("audio.wav")
    # Return the transcribed text
    return result["text"]

def generate_response(text):
    # code to generate response from GPT model
    return response

def synthesize_speech(text):
    # code to convert text to speech using Text-to-Speech API
    return audio

def main():
    st.title("Voice Chatbot")
    # Step 1: Record audio
    wav_audio_data = st_audiorec()

    if wav_audio_data is not None:
        # display audio data as received on the backend
        st.audio(wav_audio_data, format='audio/wav')
        print("Start transcribing...")
        transcript = transcribe_audio(wav_audio_data)
        print("Transcribing finished")
        st.write(f"Transcript: {transcript}")

        # # Step 2: Transcribe audio to text
        # text = transcribe_audio(audio)
        
        # # Step 3: Generate response using GPT model
        # response = generate_response(text)

        # # Step 4: Synthesize response to speech
        # response_audio = synthesize_speech(response)

        # # Play the response audio
        # st.audio(response_audio)

if __name__ == '__main__':
    main()
