import streamlit as st

from google import genai
from dotenv import load_dotenv
import os

from gtts import gTTS
import io


#loading the environmet variables
load_dotenv()
my_api_key=os.getenv("GEMINI_API_KEY")
#initializing the client
client=genai.Client(api_key=my_api_key)


def generate_note(pil_images):
    from google import genai
    import os
    from dotenv import load_dotenv

    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    prompt = """Summarize the picture in note format in language Bangla(max 100 words).
Make sure to add necessary markdown to differentiate sections."""

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=pil_images + [prompt]  )

    return response.text
def audio_transcript(text):
    speech=gTTS(text,lang="bn",slow=False)
    audio_buffer=io.BytesIO()
    speech.write_to_fp(audio_buffer)
    audio_buffer.seek(0)
    return audio_buffer

def quiz_generator(image,difficulty):
    prompt = f"Generate 3 quizzes based on the {difficulty}. Make sure to add markdown differentiat the options. Add correct answer too,after the quiz"

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=image+ [prompt]  )
    return response.text
