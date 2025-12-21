from dotenv import load_dotenv
load_dotenv()

import base64
from groq import Groq

MODEL = "meta-llama/llama-4-scout-17b-16e-instruct"  

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def analyze_image_with_query(query, image_path):
    client = Groq()

    encoded_image = encode_image(image_path)

    messages = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": query},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{encoded_image}"
                    },
                },
            ],
        }
    ]

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages
    )

    return response.choices[0].message.content
