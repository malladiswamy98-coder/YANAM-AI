import streamlit as st
import google.generativeai as genai

# --- PAGE CONFIG ---
st.set_page_config(page_title="YANAM AI - Malladi Swamy", page_icon="🤖", layout="centered")

# --- STYLE (Kasta colors add chedham) ---
st.markdown("""
    <style>
    .stApp { background-color: #0f172a; color: white; }
    .stChatMessage { border-radius: 15px; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_stdio=True)

# --- API KEY SETUP ---
API_KEY = "AIzaSyBZnBbGkF1sKGjrFp7L5UCw4a7W9vy8iUE"
genai.configure(api_key=API_KEY)

# Automatic ga model ni vethukuntundhi
try:
    model = genai.GenerativeModel('gemini-pro')
except:
    model = genai.GenerativeModel('gemini-1.5-flash')

# --- HEADER ---
st.title("🤖 YANAM AI")
st.subheader("Created by **MALLADI SWAMY**")
st.info("Place: YANAM (Savithrinagar) | Born: 29-10-2004")

# --- CHAT HISTORY ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- USER INPUT & AI RESPONSE ---
if prompt := st.chat_input("Ask YANAM AI anything..."):
    # User message chupinchadam
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Logic
    low_prompt = prompt.lower()
    if any(word in low_prompt for word in ["who created", "swamy", "owner", "creator"]):
        full_response = "Nannu **MALLADI SWAMY** create chesaru from YANAM. Ayana details: Born on 29-10-2004. Son of **MALLADI LOVARAJU**."
    else:
        try:
            with st.spinner("YANAM AI is thinking..."):
                response = model.generate_content(prompt)
                full_response = response.text
        except Exception as e:
            full_response = f"Error vachindi Maya! {e}"

    # AI Response chupinchadam
    with st.chat_message("assistant"):
        st.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})
