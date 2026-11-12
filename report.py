from dotenv import load_dotenv
from google import genai
import pandas as pd

load_dotenv()  # puts the key from .env where genai can find it

df = pd.read_csv("match.csv")
scores = df.groupby("striker")["runs_off_bat"].sum()
top_name = scores.idxmax()
top_runs = scores.max()

prompt = f"Write a 2-sentence cricket match report. Top scorer was {top_name} with {top_runs} runs."

client = genai.Client()
reply = client.interactions.create(model="gemini-3.1-flash-lite", input=prompt)
print(reply.output_text)

