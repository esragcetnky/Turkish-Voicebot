Turkish Voicebot using Streamlit, OpenAI, and gTTS

![image](https://github.com/user-attachments/assets/b94b9faa-58f5-4ca6-863c-8d11c37e8907)

Overview
This project is a Turkish Voicebot built using Streamlit for the user interface, gTTS (Google Text-to-Speech open-source library) for voice synthesis, and OpenAI's model for natural language processing. The voicebot can understand and respond to Turkish language queries, providing a seamless conversational experience.

Features
Voice Input & Output: The bot accepts voice inputs in Turkish and responds with synthesized speech using the gTTS library.
Natural Language Understanding: Leveraging OpenAI's model for accurate interpretation of Turkish language queries.
Interactive UI: Built with Streamlit, allowing users to interact with the voicebot directly from their browser.
Real-time Response: Processes queries and provides instant responses.
Chat History: Keeps track of the conversation history using a custom Python script.
Installation
Prerequisites
Python 3.7+
Streamlit
gTTS (Google Text-to-Speech open-source library)
OpenAI API Key
Setup
Clone the Repository

bash
Copy code
git clone https://github.com/your-username/turkish-voicebot.git
cd turkish-voicebot
Install Required Packages

bash
Copy code
pip install -r requirements.txt
Set Up Environment Variables Create a .env file in the project directory and add your OpenAI API key:

bash
Copy code
OPENAI_API_KEY=your_openai_api_key
Run the Application

bash
Copy code
streamlit run app.py
Usage
Once the application is running, open your browser and navigate to the local Streamlit server (usually http://localhost:8501).
You can start interacting with the voicebot by clicking on the microphone button, speaking your query in Turkish, and receiving an audio response.
Project Structure
app.py: Main Streamlit application file.
chat_history_array.py: Script that manages chat history during interactions.
requirements.txt: List of dependencies required to run the project.
.env: Environment variables file (not included in the repo for security reasons).
README.md: Project documentation.
How It Works
User Interaction: Users speak into the microphone, and their voice input is processed by the bot.
Processing: The text is sent to OpenAI's model, which processes the query and generates a response.
Chat History: The conversation history is managed by chat_history_array.py, allowing for context-aware responses.
Response: The response is then converted to speech using the gTTS library and played back to the user.
Contributing
If you would like to contribute to this project, please follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes and commit them (git commit -m 'Add new feature').
Push to the branch (git push origin feature-branch).
Create a Pull Request.
License
This project is licensed under the MIT License. See the LICENSE file for more details.

Contact
For any questions or suggestions, feel free to reach out:

Email: your.email@example.com
GitHub: your-username
