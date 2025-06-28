# import google.generativeai as genai
# import streamlit as st

# # ✅ Load API key securely from Streamlit Secrets
# genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# # ✅ You can hardcode or move this into st.secrets too
# model_name = "models/gemini-1.5-flash"
# agent_name = "My Chatbot 🎀"
# agent_role = "Your cute, helpful assistant"

# # Initialize the model
# chat_model = genai.GenerativeModel(model_name)
# chat_session = chat_model.start_chat()

# def get_response(user_input):
#     prompt = (
#         f"You are {agent_name}. {agent_role}. "
#         f"Answer the following user query very intelligently, concisely and don't ask questions back:\n\n"
#         f"{user_input}"
#     )
#     response = chat_session.send_message(prompt)
#     return response.text
import google.generativeai as genai
import streamlit as st

# ✅ Configure Gemini with secret key
genai.configure(api_key=st.secrets["AIzaSyCUcJwIiNRvxDGHYqv8eVuO8anUCBGOaYk"])

# --- Model setup ---
model_name = "models/gemini-1.5-flash"
agent_name = "My Chatbot 🎀"
agent_role = "Your elegant, intelligent and pink-powered assistant"

# --- Initialize Gemini model and start chat session ---
chat_model = genai.GenerativeModel(model_name)
chat_session = chat_model.start_chat()

# --- Response function ---
def get_response(user_input):
    prompt = (
        f"You are {agent_name}. {agent_role}. "
        f"Answer clearly and intelligently. Do NOT ask questions back. "
        f"Here's what the user asked:\n\n{user_input}"
    )
    response = chat_session.send_message(prompt)
    return response.text


