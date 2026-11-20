# 1. import the tools
import streamlit as st
import pandas as pd
from google import genai
from dotenv import load_dotenv

# 2. load the seceret key
load_dotenv()

# 3. using python read the match and count up facts
df = pd.read_csv("match.csv")
extras = df["extras"].sum()
scores = df.groupby("striker")["runs_off_bat"].sum() 
top_name = scores.idxmax()
top_runs = scores.max()
team_total = scores.sum() + extras

# 4. build the prompt

prompt = f"""
Write a 2-sentence cricket match report.
Facts:
- Top scorer: {top_name} with {top_runs} runs
- Runs per batter: {scores.to_dict()}
- Team total: {team_total}
- Extras: {extras} 
Use ONLY these facts, Do not add opinions and guesses """

# 5. call gemini and get the report 
client = genai.Client()
reply = client.interactions.create(model ="gemini-3.1-flash-lite", input=prompt)
st.write(reply.output_text)

# 6. use can ask the questions(using gurardrails)
question = st.text_input("Ask about the match:")
if question:
    qa_prompt = f"""Answer using ONLY these facts.
    Facts:
    - Runs per batter: {scores.to_dict()}
    - Team total: {team_total} 
    - Extras: {extras}
    If the answer is not in the facts, say "I don't have that data."
    Question: {question}
    """
    answer = client.interactions.create(model="gemini-3.1-flash-lite", input=qa_prompt)
    st.write(answer.output_text)