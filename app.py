# import streamlit as st
# from chatbot import get_response
# import datetime
# import json

# st.set_page_config(page_title="Manahil's Chatbot", page_icon="🤖", layout="centered")

# st.markdown(
#     "<bg style='color: blue'>"
#     "<h1 style='text-align: center; color: #C71585;'>🤖 Manahil's Chatbot</h1>"
#     "<p style='text-align: center;'>Ask me anything — I'm here to help!</p>",
#     unsafe_allow_html=True,
# )

# # New Avatars (simple and elegant)
# BOT_AVATAR = "https://cdn-icons-png.flaticon.com/512/4712/4712027.png"
# USER_AVATAR = "https://cdn-icons-png.flaticon.com/512/921/921347.png"

# # Initialize chat history
# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []

# # Real-time chat input
# user_input = st.chat_input("Type your message here...")

# if user_input:
#     with st.spinner("Thinking..."):
#         bot_reply = get_response(user_input)

#     st.session_state.chat_history.append(("user", user_input))
#     st.session_state.chat_history.append(("bot", bot_reply))

# for sender, message in st.session_state.chat_history:
#     with st.chat_message("user" if sender == "user" else "assistant", avatar=USER_AVATAR if sender == "user" else BOT_AVATAR):
#         if sender == "user":
#             st.markdown(message)
#         else:
#             st.markdown(message)
#             with st.expander("📋 Copy"):
#                 st.code(message, language="markdown")

# # Save chat history
# if st.button("💾 Save Chat"):
#     timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
#     filename = f"manahil_chat_{timestamp}.json"
#     with open(filename, "w", encoding="utf-8") as f:
#         json.dump(st.session_state.chat_history, f, indent=2, ensure_ascii=False)
#     st.success(f"Chat saved to {filename}")
import streamlit as st
from chatbot import get_response
import datetime
import json
import time

st.set_page_config(page_title="🎀 Manahil Chatbot 🎀", page_icon="🎀", layout="centered")

# --- Black and Pink Pookie Theme with Glitter and Animations ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Georgia&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Georgia', 'Great Vibes', cursive;
        background-color: #000000 !important;
        background-image: radial-gradient(circle at top left, #ff69b41a, #000000 60%) !important;
        background-attachment: fixed;
        color: #ffb6c1;
        overflow-x: hidden;
    }

    body::before {
        content: "";
        position: fixed;
        top: 0; left: 0;
        width: 100%; height: 100%;
        background: url('https://www.transparenttextures.com/patterns/glitter.png') repeat;
        opacity: 0.2;
        z-index: 0;
        pointer-events: none;
    }

    canvas.particle-bg {
        position: fixed;
        top: 0; left: 0;
        width: 100%; height: 100%;
        z-index: 1;
        pointer-events: none;
    }

    h1, p {
        color: #ff69b4;
        text-align: center;
        font-family: 'Great Vibes', cursive;
        font-size: 2.5em;
        position: relative;
        z-index: 2;
        text-shadow: 0 0 10px #ff69b4;
    }

    .stButton > button {
        background-color: #ff69b4;
        color: white;
        border-radius: 30px;
        border: none;
        padding: 0.6em 1.6em;
        font-weight: bold;
        box-shadow: 2px 2px 12px #ff69b4aa;
        transition: transform 0.3s ease, background-color 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #ff1493;
        transform: scale(1.1);
    }

    .chat-bubble {
        padding: 1em;
        background: linear-gradient(135deg, #ff69b4 0%, #ffb6c1 100%);
        border-radius: 25px;
        box-shadow: 0px 0px 20px #ff69b4;
        color: white;
        margin-bottom: 12px;
        animation: popIn 0.6s ease-out;
        position: relative;
        z-index: 2;
    }

    .user-bubble {
        background: linear-gradient(135deg, #ffc0cb 0%, #ffdde1 100%);
        text-align: right;
        color: black;
    }

    .copy-icon {
        text-align: right;
        margin-top: -10px;
        margin-right: 10px;
        cursor: pointer;
        font-size: 20px;
        color: #ffc0cb;
        transition: color 0.3s ease;
    }
    .copy-icon:hover {
        color: #fff;
    }

    @keyframes popIn {
        from { transform: translateY(10px); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
    }
    </style>
""", unsafe_allow_html=True)

# --- Title ---
st.markdown("""
<h1>🎀 Manahil Chatbot 🎀</h1>
<p>Your elegant, intelligent and pink-powered assistant 💖🎀</p>
""", unsafe_allow_html=True)

# --- Avatars ---
BOT_AVATAR = "https://cdn-icons-png.flaticon.com/512/6551/6551999.png"
USER_AVATAR = "https://cdn-icons-png.flaticon.com/512/4712/4712109.png"

# --- Onboarding Welcome ---
if "welcomed" not in st.session_state:
    st.balloons()
    st.toast("🎀 Welcome, lovely! I'm your pink-powered chatbot. Let's chat!", icon="💖")
    st.session_state.welcomed = True

# --- Initialize chat ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# --- Typing state ---
if "typing" not in st.session_state:
    st.session_state.typing = False

# --- Chat input ---
user_input = st.chat_input("Type your cute message here 🎀")

if user_input:
    st.session_state.chat_history.append(("user", user_input))
    st.session_state.typing = True
    with st.spinner("Thinking with sparkles 🎀..."):
        bot_reply = get_response(user_input)
    st.session_state.chat_history.append(("bot", bot_reply))
    st.session_state.typing = False

# --- Typewriter animation ---
def typewriter(text, speed=0.02):
    placeholder = st.empty()
    result = ""
    for char in text:
        result += char
        placeholder.markdown(f"<div class='chat-bubble'>{result}</div>", unsafe_allow_html=True)
        time.sleep(speed)

# --- Display chat ---
for sender, message in st.session_state.chat_history:
    if sender == "user":
        with st.chat_message("user", avatar=USER_AVATAR):
            st.markdown(f"<div class='chat-bubble user-bubble'>{message}</div>", unsafe_allow_html=True)
    else:
        with st.chat_message("assistant", avatar=BOT_AVATAR):
            typewriter(message)
            st.markdown(f"<div class='copy-icon' onclick=\"navigator.clipboard.writeText('{message}').then(()=>alert('Copied!'))\">📋</div>", unsafe_allow_html=True)

# --- Typing indicator ---
if st.session_state.typing:
    with st.chat_message("assistant", avatar=BOT_AVATAR):
        st.markdown("Manahil is typing... ✍️")

# --- Save chat ---
if st.button("🎀 Save Chat Log"):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"pookie_chat_{timestamp}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(st.session_state.chat_history, f, indent=2, ensure_ascii=False)
    st.success(f"Chat saved to {filename} 🎀")