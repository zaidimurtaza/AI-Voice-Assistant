import time
import openai
import speech_recognition as sr
import pyttsx3
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """ 
Your Name is : jarvis

Your Owner Name : Murtaza Sir

Answer the question below.

Here is the conversation history :{context}

Question : {question}

Answer:

"""
model = OllamaLLM(model='llama3.2')
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# print(result)

# Initialize OpenAI API and TTS engine

# "LzbOd6pvh5gtQ9lXc4Wsk-acdOGe10yIgknn1qjXlNljWT3BlbkFJXCxHeSv98aCXNWIRbM4ck-r6qgeMaQC_2bsl2BwvkA"
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            print('m')
            audio = recognizer.listen(source)
            # return recognizer.recognize_google(audio)
        except sr.RequestError:
            return "Sorry, the service is down."

def chat_with_ollama():
    context = ""
    while True:
        user_input = listen()
        if user_input == "quit" or user_input == "exit":
            # print("kkk")
            break
        
        print('You : ',user_input)
        result = chain.invoke({"context": context,"question": user_input})
        print("Bot: ",result)
        speak(result)
        context += f"\nUser: {user_input}\nAI: {result}"

if __name__ == "__main__":
    chat_with_ollama()
