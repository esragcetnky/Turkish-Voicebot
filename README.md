# Turkish Voicebot using Streamlit, OpenAI, and gTTS
![image](https://github.com/user-attachments/assets/b94b9faa-58f5-4ca6-863c-8d11c37e8907)
## Overview

This project is a **Turkish Voicebot** built using **Streamlit** for the user interface, **gTTS (Google Text-to-Speech open-source library)** for voice synthesis, and **OpenAI's model** for natural language processing. The voicebot can understand and respond to Turkish language queries, providing a seamless conversational experience.

## Features

- **Voice Input & Output**: The bot accepts voice inputs in Turkish and responds with synthesized speech using the gTTS library.
- **Natural Language Understanding**: Leveraging OpenAI's model for accurately interpreting Turkish language queries.
- **Interactive UI**: Built with Streamlit, allowing users to interact with the voicebot directly from their browser.
- **Real-time Response**: Processes queries and provides instant responses.
- **Chat History**: Keeps track of the conversation history using a custom Python script.

## Installation

### Prerequisites

- Python 3.7+
- [Streamlit](https://streamlit.io)
- gTTS (Google Text-to-Speech open-source library)
- OpenAI API Key

### Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/turkish-voicebot.git
   cd turkish-voicebot


2. **Install Required Packages**
   ```bash
    pip install -r requirements.txt

3. **Set Up API Credentials:**
   Add your OpenAI API key to credentials.yml 
   ```bash
    openai_api_key: "your_openai_api_key"

4. **Run the Application:**
   Add your OpenAI API key to credentials.yml 
   ```bash
    streamlit run main.py

## Project Structure
  - main.py: Main Streamlit application file.
  - chat_history_array.py: Script that manages chat history during interactions.
  - credentials.yml: File to store your OpenAI API key.
  - requirements.txt: List of dependencies required to run the project.
  - README.md: Project documentation.
    
## How It Works
  1. User Interaction: Users speak into the microphone, and their voice input is processed by the bot.
  2. Processing: The text is sent to OpenAI's model, which processes the query and generates a response.
  3. Chat History: The conversation history is managed by chat_history_array.py, allowing for context-aware responses.
  4. Response: The response is then converted to speech using the gTTS library and played back to the user.

## Contributing
If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make your changes and commit them (git commit -m 'Add new feature').
4. Push to the branch (git push origin feature-branch).
5. Create a Pull Request.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Contact
For any questions or suggestions, feel free to reach out:

  - Email: esragcetinkaya@gmail.com
  - Linkedin : [esragcetinkaya](https://www.linkedin.com/in/esra-gul-cetinkaya/?locale=en_US)

