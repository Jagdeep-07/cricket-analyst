from dotenv import load_dotenv
from google import genai
import pandas as pd

load_dotenv()  # puts the key from .env where genai can find it

df = pd.read_csv("match.csv")
scores = df.groupby("striker")["runs_off_bat"].sum()
top_name = scores.idxmax()
top_runs = scores.max()
team_runs = df["runs_off_bat"].sum() + df["extras"].sum()   # ← new


prompt = f"""Write a 2-sentence cricket match report.
Facts:
- Top scorer: {top_name} with {top_runs} runs
- Team total: {team_runs}
Use ONLY these facts. Do not add opinions or guesses."""

client = genai.Client()
reply = client.interactions.create(model="gemini-3.1-flash-lite", input=prompt)
print(reply.output_text)

