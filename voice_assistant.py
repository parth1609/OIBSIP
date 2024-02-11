import pyttsx3
'''
    
    :param text: The `text` parameter is the text that the assistant will speak out loud. It is used in
    the `speak` function to convert the text into speech using the pyttsx3 library
'''
# The above code is performing several tasks related to natural language processing and machine
# learning.
import speech_recognition as sr
# The above code is importing the TfidfVectorizer class from the sklearn.feature_extraction.text
# module. This class is used for converting a collection of raw documents into a matrix of TF-IDF
# features.
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
# The above code is importing the nltk library in Python.
import nltk
from sklearn.model_selection import train_test_split
import random
# The code is importing the `warnings` module and then setting the warning filter to ignore all
# warnings.
import warnings
warnings.simplefilter('ignore')

# The above code is written in Python and is using the nltk library to download the "punkt" package.
# The "punkt" package is used for tokenization, which is the process of splitting text into individual
# words or sentences.
# nltk.download("punkt")

def speak(text):
    """
    The `speak` function uses the pyttsx3 library to convert text into speech using the Microsoft Speech
    Platform.
    
    :param text: The "text" parameter is the input text that you want the assistant to speak out loud
    """
    engine = pyttsx3.init()
    Id = r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0"
    engine.setProperty('voice',Id)
    print("")
    print(f" Assistant : {text}")
    print("")
    engine.say(text=text)
    engine.runAndWait()

def speechrecognition():
    """
    The function `speechrecognition()` uses the SpeechRecognition library in Python to listen to audio
    input from a microphone, recognize speech using Google's speech recognition API, and return the
    recognized speech as a lowercase string.
    :return: the recognized speech query as a lowercase string.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source,0,8)

    try:
        print("Recogizing....")
        query = r.recognize_google(audio,language="en")
        print(f" Assistant : {query}")
        return query.lower()

    except:
        return ""


# The above code defines a dictionary called "intents" which contains various categories of user
# intents along with their corresponding patterns and responses. Each intent category has a list of
# patterns that represent user inputs and a list of responses that the program can provide for those
# inputs. This code is used to create a dataset for training a chatbot or a natural language
# processing model.
intents = {
    "greetings": {
        "patterns": ["hello", "hi", "hey", "howdy", "greetings", "good morning", "good afternoon", "good evening", "hi there", "hey there", "what's up", "hello there"],
        "responses": ["Hello! How can I assist you?", "Hi there!", "Hey! What can I do for you?", "Howdy! What brings you here?", "Greetings! How may I help you?", "Good morning! How can I be of service?", "Good afternoon! What do you need assistance with?", "Good evening! How may I assist you?", "Hey there! How can I help?", "Hi! What's on your mind?", "Hello there! How can I assist you today?"]
    },
    "farewell": { "patterns": ["bye", "goodbye", "see you", "see you later", "take care", "have a nice day", "have a good one", "bye bye", "cya", "later"], "responses": ["Bye! It was nice chatting with you.", "Goodbye! I hope I was helpful.", "See you soon! Have a great day.", "Take care! Thank you for using Copilot.", "Have a nice day! Im always here if you need me.", "Have a good one! I enjoyed our conversation.", "Bye bye! Come back anytime.", "Cya! Im glad you visited.", "Later! I look forward to hearing from you again.", "Farewell! I appreciate your time."] },

    "weather": { "patterns": ["weather", "how is the weather", "what is the weather like", "is it hot", "is it cold", "is it sunny", "is it rainy", "is it cloudy", "is it windy", "is it snowy"], "responses": ["The weather is fine today.", "It is a beautiful day outside.", "It is a bit chilly today.", "It is very hot today.", "It is sunny and bright today.", "It is raining cats and dogs today.", "It is cloudy and gloomy today.", "It is windy and dusty today.", "It is snowy and white today.", "Im sorry, I dont know the weather in your location."] },

    "jokes": { "patterns": ["joke", "tell me a joke", "make me laugh", "funny", "humor", "hilarious", "laugh"], "responses": ["What do you call a fish that wears a bowtie? Sofishticated.", "How do you make a tissue dance? You put a little boogie in it.", "Why did the chicken go to the seance? To get to the other side.", "What do you call a bear with no teeth? A gummy bear.", "What do you get when you cross a snowman with a vampire? Frostbite.", "How do you stop a bull from charging? You cancel its credit card.", "What do you call a boomerang that doesn’t come back? A stick.", "What do you call a dog that can tell time? A watch dog.", "What do you call a snake that works for the government? A civil serpent.", "What do you call a fish that wears a crown? A king fish."] },

    "compliments": { "patterns": ["compliment", "say something nice", "praise me", "flatter me", "boost my ego", "make me feel good", "say something positive"], "responses": ["You are awesome.", "You are very smart.", "You are very kind.", "You are very talented.", "You are very beautiful.", "You are very funny.", "You are very creative.", "You are very brave.", "You are very generous.", "You are very amazing."] },

    "riddles": { "patterns": ["riddle", "tell me a riddle", "puzzle me", "brain teaser", "challenge me", "test my logic", "test my intelligence"], "responses": ["What has a face and two hands but no arms or legs? A clock.", "What can you break, even if you never pick it up or touch it? A promise.", "I have keys, but no locks and space, but no rooms. You can enter, but can’t go outside. What am I? A keyboard.", "This belongs to you, but everyone else uses it. Your name.", "I have many keys, but usually only two or three are used to unlock me. What am I? A piano.", "I have a heart that never beats. I have blood, but I don’t breathe. I can die without ever being born. What am I? A book.", "What invention lets you look right through a wall? A window.", "This belongs to you, but everyone else can see it. Your reflection.", "What can you catch, but not throw? A cold.", "What is black when it’s clean and white when it’s dirty? A chalkboard."] },

    "movies": { "patterns": ["movie", "recommend me a movie", "suggest me a movie", "what movie should I watch", "what is your favorite movie", "best movie", "latest movie", "popular movie", "classic movie", "movie genre"], "responses": ["You should watch The Shawshank Redemption. It is a masterpiece of storytelling and cinematography.", "You should watch The Lion King. It is a timeless tale of courage and friendship.", "You should watch Inception. It is a mind-bending thriller that will keep you guessing.", "You should watch The Godfather. It is a masterpiece of crime and drama.", "You should watch Titanic. It is a romantic and tragic story of love and sacrifice.", "You should watch The Avengers. It is a fun and action-packed superhero movie.", "You should watch Parasite. It is a brilliant and dark comedy that won the Oscar for best picture.", "You should watch The Matrix. It is a sci-fi classic that explores the nature of reality.", "You should watch The Lord of the Rings. It is an epic fantasy adventure that will take you to a magical world.", "You should watch Forrest Gump. It is a heartwarming and inspiring story of a man who lives a remarkable life."] },

    "music": { "patterns": ["music", "recommend me a song", "suggest me a song", "what song should I listen to", "what is your favorite song", "best song", "latest song", "popular song", "classic song", "music genre"], "responses": ["You should listen to Bohemian Rhapsody by Queen. It is a masterpiece of rock and opera.", "You should listen to Imagine by John Lennon. It is a beautiful and inspiring song.", "You should listen to Bad Guy by Billie Eilish. It is a catchy and edgy pop song.", "You should listen to Stairway to Heaven by Led Zeppelin. It is a legendary and epic rock song.", "You should listen to My Heart Will Go On by Celine Dion. It is a powerful and emotional ballad.", "You should listen to Old Town Road by Lil Nas X. It is a fun and catchy country rap song.", "You should listen to Despacito by Luis Fonsi and Daddy Yankee. It is a popular and upbeat Latin song.", "You should listen to Smells Like Teen Spirit by Nirvana. It is a grunge and alternative rock anthem.", "You should listen to Thriller by Michael Jackson. It is a classic and iconic pop song.", "You should listen to Happy by Pharrell Williams. It is a cheerful and uplifting song."] },

    "games": { "patterns": ["game", "recommend me a game", "suggest me a game", "what game should I play", "what is your favorite game", "best game", "latest game", "popular game", "classic game", "game genre"], "responses": ["You should play The Witcher 3: Wild Hunt. It is a masterpiece of role-playing and storytelling.", "You should play Minecraft. It is a creative and sandbox game that lets you build anything you want.", "You should play Among Us. It is a fun and social game that tests your deception and deduction skills.", "You should play The Legend of Zelda: Breath of the Wild. It is a beautiful and immersive open-world adventure.", "You should play Grand Theft Auto V. It is a thrilling and action-packed crime game.", "You should play Fortnite. It is a popular and competitive battle royale game.", "You should play Red Dead Redemption 2. It is a stunning and realistic western game.", "You should play Super Mario Bros. It is a classic and iconic platformer game.", "You should play Half-Life 2. It is a sci-fi and shooter game that revolutionized the genre.", "You should play Portal. It is a clever and witty puzzle game that challenges your logic and physics."] },

    "quotes": { "patterns": ["quote", "tell me a quote", "inspire me", "motivate me", "wisdom", "philosophy", "life advice", "say something profound"], "responses": ["The journey of a thousand miles begins with a single step. - Lao Tzu", "Be the change that you wish to see in the world. - Mahatma Gandhi", "Don’t cry because it’s over, smile because it happened. - Dr. Seuss", "The only thing we have to fear is fear itself. - Franklin D. Roosevelt", "Be yourself; everyone else is already taken. - Oscar Wilde", "The more you know, the more you realize how much you don’t know. - Albert Einstein", "The unexamined life is not worth living. - Socrates", "The most important thing is to enjoy your life - to be happy - it’s all that matters. - Audrey Hepburn", "The only true wisdom is in knowing you know nothing. - Socrates", "The truth is rarely pure and never simple. - Oscar Wilde"] }
        
}

training_data,labels = [], []


# The above code is iterating over a dictionary called `intents`. For each key-value pair in
# `intents`, it is iterating over the list of patterns in the value. It appends each pattern
# (converted to lowercase) to a list called `training_data` and appends the corresponding intent (key)
# to a list called `labels`.
for intent , data in intents.items():
    for pattern in data['patterns']:
        training_data.append(pattern.lower())
        labels.append(intent)


# The above code is performing text vectorization using the TF-IDF (Term Frequency-Inverse Document
# Frequency) technique.
Vectorizer = TfidfVectorizer(tokenizer=nltk.word_tokenize,stop_words="english",max_df=0.8,min_df=1)
X_train = Vectorizer.fit_transform(training_data)
X_train,X_test,Y_train,Y_test = train_test_split(X_train,labels,test_size=0.4,random_state=42,stratify=labels)

# The above code is creating an instance of the Support Vector Classifier (SVC) model with a linear
# kernel. The `probability` parameter is set to True, which allows the model to output probability
# estimates. The `C` parameter is set to 1.0, which controls the regularization strength of the model.
model = SVC(kernel='linear', probability=True, C=1.0)
model.fit(X_train, Y_train)

# The above code is making predictions using a trained machine learning model on the test data
# (X_test). The predicted values are stored in the variable "predictions".
predictions = model.predict(X_test)

def predict_intent(user_input):
    """
    The function `predict_intent` takes a user input, converts it to lowercase, vectorizes it using a
    pre-trained vectorizer, and predicts the intent using a pre-trained model.
    
    :param user_input: The user's input, which is a string representing their query or statement
    :return: The function `predict_intent` returns the predicted intent based on the user input.
    """
    user_input = user_input.lower()
    input_vector = Vectorizer.transform([user_input])
    intent = model.predict(input_vector)[0]
    return intent

speak("Assistant: Hello! How can I assist you?")
# The above code is creating an infinite loop that continuously prompts the user for input using
# speech recognition. If the user says "exit", the loop will break and the program will print "AI
# Assistant: Goodbye!" before terminating.
while True:
    user_input = speechrecognition()
    if user_input.lower() == 'exit':
        print("AI Assistant: Goodbye!")
        break

    # The above code is a Python code snippet that is used to generate a response based on the user's
    # input. It first predicts the intent of the user's input using a function called
    # `predict_intent`. If the predicted intent is found in a dictionary called `intents`, it selects
    # a random response from the list of responses associated with that intent. Finally, it speaks the
    # selected response.
    intent = predict_intent(user_input)
    if intent in intents:
        responses = intents[intent]['responses']
        response = random.choice(responses)
        speak(response)

    else:
        speak("Assistant: Sorry, I'm not sure how to respond to that.")

