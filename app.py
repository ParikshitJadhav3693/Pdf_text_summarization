import streamlit as st
from utils.pdf_utils import extract_text_from_pdf
from utils.summarizer import summarize_text
from utils.qa_bot import answer_question

st.set_page_config(page_title="PDF Summarization & Q&A Chatbot")

st.title("📄 PDF Text Summarizer and Q&A Chatbot")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file:
    st.success("PDF uploaded successfully!")

    with st.spinner("Extracting text from PDF..."):
        text = extract_text_from_pdf(uploaded_file)

    st.subheader("Extracted Text Preview")
    st.text_area("PDF Text", text[:1000] + "...", height=200)

    if st.button("Generate Summary"):
        with st.spinner("Summarizing..."):
            summary = summarize_text(text)
        st.subheader("Summary")
        st.write(summary)

    st.subheader("Ask a Question about the PDF")
    user_question = st.text_input("Enter your question:")

    if user_question:
        with st.spinner("Finding answer..."):
            answer = answer_question(text, user_question)
        st.write(f"**Answer:** {answer}")
