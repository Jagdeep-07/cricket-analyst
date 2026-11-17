from dotenv import load_dotenv
from google import genai
import pandas as pd

load_dotenv()  # puts the key from .env where genai can find it

df = pd.read_csv("match.csv")
scores = df.groupby("striker")["runs_off_bat"].sum()
extras = df["extras"].sum()
top_name = scores.idxmax()
top_runs = scores.max()
team_runs = df["runs_off_bat"].sum() + df["extras"].sum()

# --- Report ---
prompt = f"""Write a 2-sentence cricket match report.
Facts:
- Top scorer: {top_name} with {top_runs} runs
- Runs per batter: {scores.to_dict()}
- Team total: {team_runs}
- Extras: {extras}
Use ONLY these facts. Do not add opinions or guesses.
"""

client = genai.Client()
reply = client.interactions.create(model="gemini-3.1-flash-lite", input=prompt)
print(reply.output_text)

# --- Q&A ---
question = input("Ask about the match: ")

qa_prompt = f"""Answer using ONLY these facts.
Facts:
- Runs per batter: {scores.to_dict()}
- Team total: {team_runs}
- Extras: {extras}
If the answer is not in the facts, say "I don't have that data."
Question: {question}
"""

answer = client.interactions.create(model="gemini-3.1-flash-lite", input=qa_prompt)
print(answer.output_text)