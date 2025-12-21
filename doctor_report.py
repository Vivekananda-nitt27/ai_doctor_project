from groq import Groq
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from datetime import date
import os

MODEL = "meta-llama/llama-4-scout-17b-16e-instruct"




import json


client = Groq()

def format_medical_report_with_groq(doctor_response: str) -> dict:
    prompt = f"""
You are a medical documentation assistant.

Return ONLY valid JSON.
No markdown.
No ```json.
No explanation.

Format:
{{"observation": "...", "medication": "..."}}

Doctor Response:
{doctor_response}
"""

    response = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    content = response.choices[0].message.content.strip()

    # Extra safety
    if content.startswith("```"):
        content = content.split("```")[1].strip()

    return json.loads(content)



def generate_handwritten_medical_pdf(observation: str, medication: str) -> str:
    from reportlab.lib.pagesizes import A4
    from reportlab.pdfgen import canvas
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from datetime import date
    import os

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    FONT_PATH = os.path.join(BASE_DIR, "fonts", "DoctorHandwriting.ttf")
    SIGNATURE_PATH = os.path.join(BASE_DIR, "assets", "signature.jpeg")

    output_path = os.path.join(BASE_DIR, "medical_report.pdf")

    pdfmetrics.registerFont(TTFont("Handwriting", FONT_PATH))

    c = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4

    c.setFont("Helvetica-Bold", 50)
    c.drawString(50, height - 50, "Medical Observation Report")

    c.setFont("Helvetica", 20)
    c.drawString(50, height - 75, f"Date: {date.today()}")

    c.setFont("Handwriting", 20)
    text = c.beginText(50, height - 120)
    text.textLine("Observation:")
    text.textLines(observation)
    c.drawText(text)

    text = c.beginText(50, height - 300)
    text.textLine("Medication:")
    text.textLines(medication)
    c.drawText(text)

    c.setFont("Helvetica", 8)
    c.drawString(
        50, 150,
        "This AI-generated report is for educational purposes only. "
        "Consult a licensed medical professional."
    )

    c.drawImage(SIGNATURE_PATH, 50, 100, width=140, height=45)
    c.setFont("Helvetica", 9)
    c.drawString(50, 85, "Dr. AI MedAssist")

    c.save()
    return output_path



def create_medical_report(doctor_response: str) -> str:
    """
    Main function to be imported into Gradio
    """

    structured = format_medical_report_with_groq(doctor_response)
    return generate_handwritten_medical_pdf(
        structured["observation"],
        structured["medication"]
    )
