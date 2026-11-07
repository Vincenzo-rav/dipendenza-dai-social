from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/home")
def home():
    return "<h1>Home page</h1>"

@app.route("/random_fact")
def curiosità():
    curiosità = ["La maggior parte delle persone che soffrono di dipendenza tecnologica sperimentano un forte stress quando si trovano al di fuori dell'area di copertura della rete o non possono utilizzare i loro dispositivi", "Secondo uno studio del 2019, oltre 60 persone su 100 risponde ai messaggi di lavoro sul proprio smartphone entro 15 minuti dall'uscita dal lavoro."]
    fatto = random.choice(curiosità)
    return f"Un particolare curioso è : {fatto}"

@app.route("/secret")
def risultato():
    risultato = ["Testa", "Croce"]
    caso = random.choice(risultato)
    return f"Il risultato è: {caso}"

app.run(debug=True)

#https://docs.google.com/spreadsheets/d/1QoySRw2Si2Z7hW6mhju0519nGZoAvrpNZBDMpWRvwB4/edit?gid=0#gid=0