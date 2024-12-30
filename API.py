#
## Importation externe
#
from flask import Flask, request, jsonify

#Chargement modèle
model_GPT = GPT4All("gpt4all-13b-snoozy-q4_0.gguf")

app = Flask(__name__)

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get("message", '')
    reponse = model_GPT.generate(user_input)
    retur jsonify({"reponse" : reponse})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)