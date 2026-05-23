import streamlit as st
from transformers import pipeline

# Page title
st.title("AI Text Summarizer")

st.write("Enter long text and get a short summary.")

# Load summarization model
@st.cache_resource
def load_model():
    summarizer = pipeline(
        "summarization",
        model="t5-small"
    )
    return summarizer

summarizer = load_model()

# User input
text = st.text_area(
    "Enter your text here:",
    height=250
)

# Summarize button
if st.button("Generate Summary"):

    if len(text.split()) < 20:
        st.warning("Please enter at least 20 words.")

    else:
        with st.spinner("Generating summary..."):

            # Add summarize prefix
            input_text = "summarize: " + text

            # Generate summary
            summary = summarizer(
                input_text,
                max_length=60,
                min_length=15,
                do_sample=False
            )

            # Display result
            st.subheader("Summary")
            st.success(summary[0]['summary_text'])