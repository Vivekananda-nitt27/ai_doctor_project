import os
from groq import Groq
# Load from environment variable
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not set")

# Initialize client
client = Groq(api_key=GROQ_API_KEY)


MODEL = "meta-llama/llama-4-scout-17b-16e-instruct"

def disease_followup_chat(doctor_response, user_question, history):
    prompt = f"""
Initial medical observation:
{doctor_response}

Conversation so far:
{history}

User question:
{user_question}

Rules:

- Focus on tests, precautions, disease understanding
-suggest medication
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    answer = response.choices[0].message.content

    history.append({
        "question": user_question,
        "answer": answer
    })

    return answer, history
