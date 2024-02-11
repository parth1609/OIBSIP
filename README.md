# OIBSIP

OIBSIP - OASIS Infobyte Internship

Task - 1 (Voice Assistant)

Create a basic voice assistant that can perform simple tasks based on voice commands. Implement features like responding to "Hello" and providing predefined responses, telling the time or date, and searching the web or information based on user queries.

Features:
1. Speech Recognition:
Utilizing the SpeechRecognition library, the AI Assistant now listens to audio input from a microphone and recognizes speech using Google's speech recognition API.
2. Text-to-Speech:
The pyttsx3 library has been integrated to convert text into speech, providing a seamless interaction with the assistant.
3. Natural Language Processing (NLP):
The program incorporates the sklearn.feature_extraction.text module, featuring the TfidfVectorizer class for converting raw documents into a matrix of TF-IDF features.
4. Machine Learning Model:
The AI Assistant employs a Support Vector Classifier (SVC) with a linear kernel to predict user intents based on their input.
5. Diverse User Interactions:
The assistant can engage in various conversations, including greetings, farewells, weather inquiries, jokes, compliments, riddles, movie and music recommendations, game suggestions, and inspirational quotes.

