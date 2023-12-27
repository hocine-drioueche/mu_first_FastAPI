from fastapi import FastAPI
import random

app=FastAPI()

@app.get('/')
def accueil():
    return{ "Message": "Bienvenue sur notre API de génération de nombre aléatoire"}



@app.get('/nombre_aleatoire')
def generer_nombre():
    """
   Cette fonction permet de générer des nombres aléatoires entre 0 et 1000
    """
    return{"nombre_aleatoire": random.randint(0,1000)}


@app.get('/nombre_aleatoire/{min}_{max}')
def generer_nombre(min:int=0, max:int=1000):
    """
   Cette fonction permet de générer des nombres aléatoires entre min et max
    """
    return{"nombre_aleatoire": random.randint(min,max)}

