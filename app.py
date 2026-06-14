import streamlit as st
import google.generativeai as genai

# Get API key from Streamlit Secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash")

st.set_page_config(
    page_title="AI-Powered Study Buddy",
    page_icon="📚"
)

st.title("📚 AI-Powered Study Buddy")
st.write("Learn smarter with AI!")

feature = st.sidebar.selectbox(
    "Select Feature",
    ["Ask Doubt", "Summarize Notes", "Generate Quiz"]
)

# Ask Doubt
if feature == "Ask Doubt":
    question = st.text_input("Ask your question")

    if st.button("Get Answer"):
        if question:
            response = model.generate_content(
                f"Explain clearly and simply: {question}"
            )
            st.success(response.text)

# Summarize Notes
elif feature == "Summarize Notes":
    notes = st.text_area("Paste your notes")

    if st.button("Summarize"):
        if notes:
            response = model.generate_content(
                f"Summarize these notes in bullet points:\n\n{notes}"
            )
            st.success(response.text)

# Generate Quiz
elif feature == "Generate Quiz":
    topic = st.text_input("Enter Topic")

    if st.button("Generate"):
        if topic:
            response = model.generate_content(
                f"Generate 5 multiple-choice questions with answers on {topic}"
            )
            st.write(response.text)
