import streamlit as st
import google.generativeai as genai

# --- PAGE CONFIG ---
st.set_page_config(page_title="YANAM AI - Malladi Swamy", page_icon="🤖")

# --- STYLE ---
st.markdown("""
    <style>
    .stApp { background-color: #0f172a; color: white; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.title("🤖 YANAM AI")
st.subheader("Created by **MALLADI SWAMY**")
st.info("Place: YANAM | Born: 29-10-2004")

# --- API KEY SETUP ---
# Direct ga connect avthunnam, List Models lanti permissions avasaram ledhu
API_KEY = "AIzaSyBZnBbGkF1sKGjrFp7L5UCw4a7W9vy8iUE"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')

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
        ans = "Nannu **MALLADI SWAMY** create chesaru from YANAM. Born on 29-10-2004. Son of **MALLADI LOVARAJU**."
    else:
        try:
            with st.spinner("YANAM AI is thinking..."):
                # Real AI Response
                response = model.generate_content(prompt)
                ans = response.text
        except Exception as e:
            # Okavela Gemini Pro pani cheyakapothe, alternate model
            try:
                model_alt = genai.GenerativeModel('gemini-1.5-flash')
                response = model_alt.generate_content(prompt)
                ans = response.text
            except:
                ans = "Error vachindi Maya, okasari malli adugu!"

    with st.chat_message("assistant"):
        st.markdown(ans)
    st.session_state.messages.append({"role": "assistant", "content": ans})
