#
## Intern importation
#
import schedule
import time
from gpt4all import gpt4all, GPT4All

#Sélection du modèle IA mini Orca
model_orca = GPT4All("orca-mini-3b-gguf2-q4_0.gguf")
model_GPT = GPT4All("gpt4all-13b-snoozy-q4_0.gguf")


# with model.chat_session():
#     print(model.generate("Bonjour Orca, es tu là ?", max_tokens=1024))

# with model_GPT.chat_session():
#     reponse = model_GPT.generate("Bonjour Orca, peux tu me dire tout ce que tu es capable de faire ?")
#     print(reponse)
def prompt():
    print("Assistant IA - Tapez 'quit' pour sortir.")
    while True:
        user_input = input("Nathan: ")
        if user_input.lower() == "quit":
            print('Au revoir Nathan :) !')
            break
        with model_GPT.chat_session():
            reponse = model_GPT.generate(user_input, max_tokens=150, temp=0.7)
            print(f'JAMES : {reponse}')


#Début daily motivation
def daily_motivation():
    prompt = "Donne-moi une citation motivante pour la journée."
    response = gpt.generate(prompt)
    print(response)

schedule.every().day.at("09:00").do(daily_motivation)

while True:
    schedule.run_pending()
    time.sleep(1)
#Fin daily motivation

