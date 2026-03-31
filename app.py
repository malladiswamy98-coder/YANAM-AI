import streamlit as st
import google.generativeai as genai

# --- PAGE CONFIG ---
st.set_page_config(page_title="YANAM AI - Malladi Swamy", page_icon="🤖")

# --- HEADER ---
st.title("🤖 YANAM AI")
st.subheader("Created by **MALLADI SWAMY**")
st.info("Place: YANAM | Born: 29-10-2004")

# --- API KEY SETUP ---
API_KEY = "AIzaSyBZnBbGkF1sKGjrFp7L5UCw4a7W9vy8iUE"
genai.configure(api_key=API_KEY)

# Ikkada automatic ga available model ni vethukuthundi
def get_model():
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            return genai.GenerativeModel(m.name)
    return genai.GenerativeModel('gemini-1.5-flash')

model = get_model()

# --- CHAT HISTORY ---
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- INPUT & LOGIC ---
if prompt := st.chat_input("Ask YANAM AI anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Identity Logic (Always Works)
    low_prompt = prompt.lower()
    if any(word in low_prompt for word in ["who created", "swamy", "owner", "creator"]):
        ans = "Nannu **MALLADI SWAMY** create chesaru from YANAM. Born on 29-10-2004. Son of MALLADI LOVARAJU."
    else:
        try:
            with st.spinner("Thinking..."):
                response = model.generate_content(prompt)
                ans = response.text
        except Exception as e:
            ans = f"Maya, okasari malli adugu! (Error: {e})"

    with st.chat_message("assistant"):
        st.markdown(ans)
    st.session_state.messages.append({"role": "assistant", "content": ans})
