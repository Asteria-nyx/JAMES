#
## Intern importation
#

from gpt4all import gpt4all, GPT4All

#Sélection du modèle IA mini Orca
model_orca = GPT4All("orca-mini-3b-gguf2-q4_0.gguf")
model_GPT = GPT4All("gpt4all-13b-snoozy-q4_0.gguf")


# with model.chat_session():
#     print(model.generate("Bonjour Orca, es tu là ?", max_tokens=1024))

# with model_GPT.chat_session():
#     reponse = model_GPT.generate("Bonjour Orca, peux tu me dire tout ce que tu es capable de faire ?")
#     print(reponse)

print("Assistant IA - Tapez 'quit' pour sortir.")
while True:
    user_input = input("Nathan: ")
    if user_input.lower() == "quit":
        print('Au revoir Nathan :) !')
        break
    with model_GPT.chat_session():
        reponse = model_GPT.generate(user_input, max_tokens=100)
        print(f'JAMES : {reponse}')