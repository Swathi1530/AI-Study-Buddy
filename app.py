import streamlit as st
from transformers import pipeline

# Load Models
summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)

qa_model = pipeline(
    "text2text-generation",
    model="google/flan-t5-base"
)

st.set_page_config(page_title="AI Study Buddy")

st.title("📚 AI-Powered Study Buddy")
st.write("Your Personal AI Learning Assistant")

option = st.sidebar.selectbox(
    "Choose Feature",
    ["Ask Doubt", "Summarize Notes", "Generate Quiz"]
)

# Ask Doubt
if option == "Ask Doubt":
    question = st.text_input("Enter your question")

    if st.button("Get Answer"):
        prompt = f"Answer this educational question: {question}"
        result = qa_model(prompt, max_length=150)

        st.success(result[0]["generated_text"])

# Summarize Notes
elif option == "Summarize Notes":

    notes = st.text_area("Paste your notes")

    if st.button("Summarize"):
        summary = summarizer(
            notes,
            max_length=100,
            min_length=30,
            do_sample=False
        )

        st.success(summary[0]["summary_text"])
# Generate Quiz
elif option == "Generate Quiz":

    topic = st.text_input("Enter Topic")

    if st.button("Generate Quiz"):

        prompt = f"""
        Generate 5 multiple-choice questions about {topic}
        with answers.
        """

        quiz = qa_model(
            prompt,
            max_length=300
        )

        st.write(quiz[0]["generated_text"])
