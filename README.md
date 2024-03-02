# OIBSIP

OIBSIP - OASIS Infobyte Internship

<h3> Task - 1 </h3> 
<h1>Voice Assistant</h1> 

Create a basic voice assistant that can perform simple tasks based on voice
commands. Implement features like responding to "Hello" and providing predefined responses,
telling the time or date, and searching the web for information based on user queries.



Features:

1.  Speech Recognition:
Utilizing the SpeechRecognition library, the AI Assistant now listens to audio input from a microphone and recognizes speech using Google's speech recognition API.
2. Text-to-Speech:
The pyttsx3 library has been integrated to convert text into speech, providing a seamless interaction with the assistant.
3. Natural Language Processing (NLP):
The program incorporates the sklearn.feature_extraction.text module, featuring the TfidfVectorizer class for converting raw documents into a matrix of TF-IDF features.
4. Machine Learning Model:
The AI Assistant employs a Support Vector Classifier (SVC) with a linear kernel to predict user intents based on their input.
5. Diverse User Interactions:
The assistant can engage in various conversations, including greetings, farewells, weather inquiries, jokes, compliments, riddles, movie and music recommendations, game suggestions, and inspirational quotes.


<h3> Task - 2 </h3> 
<h1>BMI Calculatort</h1> 
Create a command-line BMI calculator in Python. Prompt users for their
weight (in kilograms) and height (in meters). Calculate the BMI and classify it into categories
(e.g., underweight, normal, overweight) based on predefined ranges. Display the BMI result and
category to the user.

1. BMI Calculation:
Program computes Body Mass Index (BMI) from user-input height and weight, providing a numerical measure of their relative weight.
2. Weight Status:
Determines user's weight status (underweight, healthy, or overweight) based on the calculated BMI, offering insights into overall health.
3. User Interaction:
Engages users by prompting them to input height and weight, ensuring a personalized and interactive experience.
4. Object-Oriented Design:
Utilizes an object-oriented class structure for organized code, encapsulating BMI-related functionalities and supporting ease of maintenance.
6. Readable Output:
Presents clear and readable output messages, conveying calculated BMI and weight status information for user comprehension.


<h3> Task - 3 </h3> 
<h1>Random Password Generator</h1> 
Create a command-line password generator in Python that generates random
passwords based on user-defined criteria, such as length and character types (letters, numbers,
symbols). Allow users to specify password length and character set preferences.

1. User Input and Validation:
The program prompts the user to input the desired length of the password, ensuring it is at least 12 characters.
It also asks the user whether to include letters, numbers, and symbols in the password.

2. Modular Function:
The generate_password function is responsible for creating a random password based on user preferences.
It uses the secrets module for secure random number generation.
The function validates user input, such as ensuring a positive password length and at least one character type selected.

3. Character Set Generation:
The program dynamically generates a character set based on the user's preference for including letters, numbers, and symbols.
It uses the string module to access predefined sets of ASCII characters (letters, digits, punctuation).

4. Error Handling:
The program provides error messages if there are issues with user input, such as a password length less than 12 or no character types selected.
Errors are handled in the generate_password function and displayed to the user in the main function.

5. Random Password Generation:
The program generates a random password by iteratively selecting characters from the generated character set using the secrets.choice function.
The resulting password is displayed to the user if it meets the specified criteria; otherwise, an error message is shown.
