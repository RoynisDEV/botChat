import openai 
import pyttsx3

openai.api_key = "Token de openIA"

conversation = ""

voice_id = 'spanish'
voice_id2 = 'spanish-latin-am'
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)
volume = engine.getProperty('volume')
engine.setProperty('volume', volume+0.50)
engine.setProperty('voice', voice_id2)

i = 1
while (i != 0):
    question = input("humano: ") 
    conversation += "\nHumano: " + question + "\nAI:"
    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = conversation,
        temperature = 0.0,
        max_tokens = 150,
        top_p = 1,
        frequency_penalty = 0,
        presence_penalty = 0.6,
        stop = ["\n", "Humano:", " AI:"]
    )
    anwer = response.choices[0].text.strip()
    conversation += anwer
    print("AI: " + anwer + "\n") 
    engine.say(anwer)
    engine.runAndWait()
