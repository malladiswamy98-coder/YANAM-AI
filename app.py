import streamlit as st
import requests

# --- PAGE CONFIG ---
st.set_page_config(page_title="YANAM AI - Malladi Swamy", page_icon="🤖")

st.markdown("""
    <style>
    .stApp { background-color: #0f172a; color: white; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.title("🤖 YANAM AI")
st.subheader("Created by **MALLADI SWAMY**")
st.info("Place: YANAM | Born: 29-10-2004")

# --- CHAT HISTORY ---
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- AI LOGIC (HuggingFace Free Brain) ---
def get_ai_response(prompt):
    # Identity Logic (Always Works)
    low_prompt = prompt.lower()
    if any(word in low_prompt for word in ["who created", "swamy", "owner", "creator"]):
        return "Nannu **MALLADI SWAMY** create chesaru from YANAM. Born on 29-10-2004. Son of MALLADI LOVARAJU."
    
    try:
        # Free AI Model (No API Key needed for this URL)
        API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
        response = requests.post(API_URL, json={"inputs": prompt})
        data = response.json()
        return data[0]['generated_text']
    except:
        return "Brain is busy Swamy, okasari malli adugu!"

# --- INPUT ---
if prompt := st.chat_input("Ask anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response_text = get_ai_response(prompt)
        st.markdown(response_text)
    
    st.session_state.messages.append({"role": "assistant", "content": response_text})
