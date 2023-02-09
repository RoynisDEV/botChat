import openai 
from gtts import gTTS
from playsound import playsound
from os import remove  

openai.api_key = "Token OpenIA"

conversation = ""

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
    tts = gTTS(anwer, lang='es')
    tts.save("audio.mp3")
    SalidaAudio = "audio.mp3"
    playsound(SalidaAudio)
    remove('audio.mp3')