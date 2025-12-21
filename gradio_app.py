import gradio as gr
from voice_of_the_patient import transcribe_with_groq
from brain_of_the_doctor import analyze_image_with_query
from voice_of_the_doctor import text_to_speech_with_elevenlabs
from doctor_report import create_medical_report
from disease_chat import disease_followup_chat

SYSTEM_PROMPT = """
You have to act as a professional doctor i know you are not but this is for learning purpose
Whats in this image Do you find anything wrong with it medically
If you make a differential suggest some remedies for them
please give a brief descripting of the problem 
Important include the medication and medicine in oder for the patient
Donot add any numbers or special characters in your response
Your response should be in one long paragraph
Always answer as if you are answering a real person
Donot say In the image I see but say With what I see I think you have
Dont respond as an AI model or in markdown
Mimic an actual doctor not an AI bot
in last please ask the person for the consult a doctor and give wishesto get well soon
No preamble start your answer right away
"""


def get_session():
    return {"chat_history": []}



# --------------------------
# GLOBAL CHAT HISTORY
# --------------------------
chat_history = []  # list of dicts: [{"question":..., "answer":...}]


# --------------------------
# INITIAL PROCESS FUNCTION
# --------------------------
def process_initial(audio_filepath, image_filepath):
    global chat_history

    if audio_filepath is None and image_filepath is None:
        return "", [], None

    patient_text = transcribe_with_groq(audio_filepath)
    if patient_text.strip() == "":
        patient_text = "Analyze this medical image."

    final_query = f"{SYSTEM_PROMPT}\nPatient says: {patient_text}"

    if image_filepath:
        doctor_response = analyze_image_with_query(final_query, image_filepath)
    else:
        doctor_response = "Please upload an image."

    doctor_voice = text_to_speech_with_elevenlabs(doctor_response)

    # Reset chat history and add initial conversation
    chat_history = [{"question": patient_text, "answer": doctor_response}]

    # Convert to tuples for Chatbot
    chatbot_history = [(patient_text, doctor_response)]

    return "", chatbot_history, doctor_voice


# --------------------------
# CONTINUE CHAT FUNCTION (Text-only)
# --------------------------
def continue_chat(user_message):
    global chat_history

    if len(chat_history) == 0:
        return "", []

    initial_doctor_response = chat_history[0]["answer"]
    history_list = chat_history[1:]

    # Call follow-up chat function
    answer, updated_history = disease_followup_chat(
        doctor_response=initial_doctor_response,
        user_question=user_message,
        history=history_list
    )

    chat_history = [chat_history[0]] + updated_history

    # Convert to tuples for Chatbot display
    chatbot_history = [(entry["question"], entry["answer"]) for entry in chat_history]

    return "", chatbot_history


# --------------------------
# FINAL REPORT FUNCTION
# --------------------------
def generate_final_report():
    global chat_history

    full_text = "\n".join([f"Patient: {entry['question']}\nDoctor: {entry['answer']}" for entry in chat_history])
    report_path = create_medical_report(full_text)
    return report_path


# ===============================
# GRADIO UI
# ===============================
with gr.Blocks(title="AI Doctor with Vision, Voice, and Chat") as demo:
    gr.Markdown("# 🩺 AI Doctor with Vision, Voice, and Chat")

    with gr.Row():
        audio_input = gr.Audio(type="filepath", label="Patient Voice")
        image_input = gr.Image(type="filepath", label="Upload Image")
        submit_btn = gr.Button("Submit Initial")

    chatbot = gr.Chatbot(label="Doctor Chat")
    user_message = gr.Textbox(label="Type your message here")
    send_btn = gr.Button("Send Message")

    final_report_btn = gr.Button("Generate Final Report")
    report_file = gr.File(label="Download Final Medical Report (PDF)")

    # Initial submission
    submit_btn.click(
        fn=process_initial,
        inputs=[audio_input, image_input],
        outputs=[user_message, chatbot, gr.Audio(autoplay=True)]
    )

    # Continue chat (text-only)
    send_btn.click(
        fn=continue_chat,
        inputs=[user_message],
        outputs=[user_message, chatbot]
    )

    # Final report
    final_report_btn.click(
        fn=generate_final_report,
        inputs=[],
        outputs=[report_file]
    )

demo.launch()
