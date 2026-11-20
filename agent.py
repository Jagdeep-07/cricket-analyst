import pandas as pd
from dotenv import load_dotenv
from google import genai

load_dotenv()

def get_team_total() ->int:
    """Adds runs off the bat + extras for the whole team. Use for team score questions."""
    df = pd.read_csv("match.csv")
    total = df["runs_off_bat"].sum() + df["extras"].sum()
    return int(total)

team_total_menu = {
    "type": "function",
    "name": "get_team_total",
    "description": "Adds runs off the bat + extras for the whole team. Use for team score questions.",
    "parameters": {"type": "object", "properties": {}}
}

client = genai.Client()
interaction = client.interactions.create(
    model="gemini-3.1-flash-lite",
    input = "What did the team score?",
    tools=[team_total_menu],
    )
for step in interaction.steps:
    if step.type == "function_call":
        print("Gemini wants:", step.name)
        result = get_team_total()
        print("Python got:", result)

note = {
    "type": "function_result",
    "name": step.name,
    "call_id": step.id,
    "result": [{"type": "text", "text": str(result)}]
}

final = client.interactions.create(
    model="gemini-3.1-flash-lite",
    previous_interaction_id=interaction.id,
    tools=[team_total_menu],
    input=[note],
    )
print("Gemini says:", final.output_text)
