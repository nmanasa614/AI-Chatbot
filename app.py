import streamlit as st
from chatbot import get_response
from memory import save_chat, load_history, clear_chat
from utils import extract_pdf_text, load_image
from ppt_generator import create_ppt

st.set_page_config(page_title="Advanced AI Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = load_history()

with st.sidebar:

    st.title("⚙️ Controls")
    if st.button("➕ New Chat"):
        st.session_state.messages = []
        st.rerun()
    
    if st.button("🗑 Clear Chat"):
        clear_chat()
        st.session_state.messages = []
        st.rerun()
    st.title("📥 Upload")

    uploaded_file = st.file_uploader(
        "📄 Upload PDF",
        type=["pdf"]
    )

    uploaded_image = st.file_uploader(
        "🖼 Upload Image",
        type=["png","jpg","jpeg"]
    )
    ppt_mode = st.checkbox(
        "📊 Generate PowerPoint"
    )
    st.markdown("### AI Tools")

    email_mode = st.checkbox("📧 Email Drafting")

    meeting_mode = st.checkbox(
        "📝 Meeting Summarizer"
    )
    report_mode = st.checkbox(
        "📊 AI Report Generator"
    )
    translator_mode = st.checkbox(
        "🌍 Translator"
    )
    sentiment_mode = st.checkbox(
        "😊 Sentiment Analysis"
    )

pdf_text = ""

if uploaded_file:
    pdf_text = extract_pdf_text(uploaded_file)

image = None

if uploaded_image:
    image = load_image(uploaded_image)
    st.image(image)

st.title("🤖 Advanced AI Chatbot")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

prompt = st.chat_input("Ask anything...")
if ppt_mode and prompt:

    ppt_file = create_ppt(prompt)

    with open(ppt_file, "rb") as file:

        st.download_button(
            label="📥 Download PowerPoint",
            data=file,
            file_name="AI_Presentation.pptx",
            mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
        )
if prompt:

    st.session_state.messages.append(
        {"role":"user","content":prompt}
    )

    save_chat("user",prompt)

    answer = get_response(
        prompt,
        pdf_text,
        image,
        meeting_mode,
        email_mode,
        report_mode,
        translator_mode,
        sentiment_mode
    )
    
    st.session_state.messages.append(
        {"role":"assistant","content":answer}
    )

    save_chat("assistant",answer)

    st.rerun()