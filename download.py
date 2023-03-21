import pandas as pd
from tqdm import tqdm
import json
import matplotlib.pyplot as plt
import numpy as np
import requests
from PIL import Image
import os
from io import BytesIO



df = pd.read_csv('films_choisis.csv')

if not os.path.exists("bdd"):
        # Créer le dossier si ce n'est pas le cas
        os.makedirs("bdd")
        print("Le dossier", "bdd", "a été créé.")

for row in tqdm(df.itertuples()):
    genre = row.genre
    image_url = row.image
    number = row.film_id
    bdd = row.bdd

    if os.path.isfile("./bdd/" + bdd + "/" + genre + "/" + str(number) + ".png"):
        pass

    if not os.path.exists("./bdd/" + bdd + "/" + genre):
        # Créer le dossier si ce n'est pas le cas
        os.makedirs("./bdd/" + bdd + "/" + genre)
        print("Le dossier", genre, "a été créé.")

    try:
        response = requests.get(image_url)
        image = Image.open(BytesIO(response.content))

        # Enregistrer l'image localement
        image.save("./bdd/" + bdd + "/" + genre + "/" + str(number) + ".png")
    except Exception:
        print("un probleme a eu lieu pour une image")
