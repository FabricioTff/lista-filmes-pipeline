import requests
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

url = os.getenv('URL')

querystring = {"page":"3"}

headers = {
    "X-RapidAPI-Key": os.getenv("API_KEY"),
    "X-RapidAPI-Host": os.getenv("API_HOST")
}

response = requests.get(url, headers=headers, params=querystring)

df = pd.json_normalize(response.json()['results'], record_prefix=None)

df = df[["id","originalTitleText.text","releaseYear.year"]]

df.to_csv("lista_filmes.csv")
