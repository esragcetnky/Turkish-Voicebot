# -----------------------------------------Import Libraries----------------------------------------------------------#
import time
import os
import yaml
import pytz
import base64
from datetime import datetime

# tts model and generate response
import openai
from openai import OpenAI
# sst model 
import speech_recognition as sr
from gtts import gTTS

import streamlit as st
from audio_recorder_streamlit import audio_recorder

import chat_history_array

# ---------------------------------------- Website Page Title --------------------------------------------------------------#
st.set_page_config(
    page_title = "Turkish VoiceBot Demo",
    page_icon = "🤖",
)

# ----------------------------------------- Credential File  ---------------------------------------------------------#
CREDENTIALS_PATH = "credentials.yml"
credentials = yaml.safe_load(open(CREDENTIALS_PATH))

# ----------------------------------------- Model Parameters ---------------------------------------------------------#
INSTRUCTIONS = """Please answer the question below!"""
TEMPERATURE = 0.5
MAX_TOKENS = 500
FREQUENCY_PENALTY = 0
PRESENCE_PENALTY = 0.6
# limits how many questions we include in the prompt
MAX_CONTEXT_QUESTIONS = 10

# ----------------------------------------- OpenAI Entegration ----------------------------------------------#
client = OpenAI(api_key=credentials['openai_api_key'])

# ----------------------------------------- Title  ---------------------------------------------------------#

# adding title
st.title("Turkish Voicebot using Streamlit")
"""
Speech to text : Google's model

Generating response : OpenAI's gpt-4o-mini

Text to speech : OpenAI's TTS model
"""


# -------------------------------------- Text to Speech and Save Result------------------------------------------#
def tts_and_save_speech(response_text, file_path):
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",    
        input=response_text)
    os.makedirs(os.path.dirname(file_path),exist_ok=True)
    response.write_to_file(file_path)
    while not os.path.exists(file_path):
        time.sleep(1)
    autoplay_audio(file_path)

        
# -------------------------------------- Google Speech to text ------------------------------------------#
def speech_to_text(filename):
    r = sr.Recognizer()
    filename = filename 
    
    with sr.AudioFile(filename) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data, language='tr-TR')
        
    return text

# -------------------------------------- Getting results ------------------------------------------#
def get_response(instructions, previous_questions_and_answers, new_question):
    """Get a response from ChatCompletion

    Args:
        instructions: The instructions for the chat bot - this determines how it will behave
        previous_questions_and_answers: Chat history
        new_question: The new question to ask the bot

    Returns:
        The response text
    """
    # build the messages
    messages = [
        { "role": "system", "content": instructions },
    ]
    # add the previous questions and answers
    for question, answer in previous_questions_and_answers[-MAX_CONTEXT_QUESTIONS:]:
        messages.append({ "role": "user", "content": question })
        messages.append({ "role": "assistant", "content": answer })
    # add the new question
    messages.append({ "role": "user", "content": new_question })
    
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS,
        top_p=1,
        frequency_penalty=FREQUENCY_PENALTY,
        presence_penalty=PRESENCE_PENALTY,
    ).choices[0].message.content
    return completion

# -------------------------------------- Auto Play Audio ------------------------------------------#        
def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio controls autoplay="true">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(
            md,
            unsafe_allow_html=True,
        )


st.session_state.conversation = None
st.session_state.chat_history = None

# ------------------------------------- Start Recording --------------------------------------------------------------#
audio_bytes = audio_recorder(text="Kayıt için görsele tıklayın!",key="google")
    
if audio_bytes:        
    now = datetime.now(pytz.timezone('Turkey'))
    dt_string  = now.strftime("%d_%m_%Y_%H_%M")
    user_input_location =  f"recorded_files/user_input_google_{dt_string}.wav"
    os.makedirs(os.path.dirname(user_input_location),exist_ok=True)
        
    # saving the recorded audios
    with open(user_input_location, "wb") as f:
        f.write(audio_bytes)
  
    while not os.path.exists(user_input_location):
        time.sleep(1)

    if os.path.isfile(user_input_location):
        # Create transcription from audio file
        text = speech_to_text(user_input_location)
        print("-------------- STT RESULT BEGINS HERE------------- ")
        print(text)
        print("-------------- STT RESULT ENDS HERE------------- ")
    else:
        raise ValueError("%s isn't a file!" % user_input_location)  
        
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
        
        
    st.session_state.messages.append({"role": "user", "content": text})
    with st.chat_message("user"):
        st.markdown(text)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        response = get_response(INSTRUCTIONS, chat_history_array.previous_questions_and_answers, text)
        chat_history_array.previous_questions_and_answers.append((text, response))
        
        tts_and_save_speech(response,f"response_audios/response_google_{dt_string}.wav")
        
        message_placeholder.markdown(response + "▌")
        message_placeholder.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})