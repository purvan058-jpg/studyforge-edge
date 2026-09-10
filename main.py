import os, json, requests, fitz
import streamlit as st

API_URL = os.getenv("STUDYFORGE_API_URL", "http://127.0.0.1:18181/v1/chat/completions")
MODEL = os.getenv("STUDYFORGE_MODEL", "ai-hub-models/Qwen3-4B-Instruct-2507")

st.set_page_config(page_title="StudyForge Edge", page_icon="⚡", layout="wide")

def extract_pdf(uploaded):
    doc = fitz.open(stream=uploaded.read(), filetype="pdf")
    text = "\n".join(page.get_text() for page in doc)
    return text[:50000]

def ask_local(prompt, temperature=0.2):
    payload = {
        "model": MODEL,
        "messages": [
            {"role":"system","content":
             "You are StudyForge Edge, a concise academic study assistant. "
             "Use only the supplied study material when answering. "
             "Do not invent facts. If information is absent, say so."},
            {"role":"user","content":prompt}
        ],
        "temperature": temperature,
        "max_tokens": 900
    }
    r = requests.post(API_URL, json=payload, timeout=180)
    r.raise_for_status()
    data = r.json()
    return data["choices"][0]["message"]["content"]

st.title("⚡ StudyForge Edge")
st.caption("Private, on-device AI study copilot for Snapdragon-powered PCs")

with st.sidebar:
    st.subheader("Local AI")
    st.code(API_URL, language="text")
    st.write("Model:", MODEL)
    st.info("Core generation is designed to run through the local GenieX endpoint.")

uploaded = st.file_uploader("Upload lecture notes (PDF)", type=["pdf"])
text = ""
if uploaded:
    text = extract_pdf(uploaded)
    st.success(f"Loaded {len(text):,} characters of study material.")

col1, col2, col3 = st.columns(3)
with col1:
    summary = st.button("Generate Summary", use_container_width=True)
with col2:
    quiz = st.button("Generate Quiz", use_container_width=True)
with col3:
    plan = st.button("Build Revision Plan", use_container_width=True)

if not uploaded:
    st.markdown("### Demo")
    st.write("Upload a PDF to generate study outputs locally.")
else:
    if summary:
        with st.spinner("Running local inference…"):
            out = ask_local(
                "Create an exam-focused summary from these notes. "
                "Use headings, 5–8 key points, important definitions, and formulas if present.\n\n"
                + text)
        st.subheader("Exam Summary")
        st.write(out)

    if quiz:
        with st.spinner("Generating questions locally…"):
            out = ask_local(
                "Create 5 exam-style questions from these notes. "
                "Give each question, 4 options, the correct answer, and a one-sentence explanation.\n\n"
                + text)
        st.subheader("Practice Quiz")
        st.write(out)

    if plan:
        with st.spinner("Building plan locally…"):
            out = ask_local(
                "Create a realistic 3-day revision plan from these notes. "
                "Prioritize high-value concepts and include active recall tasks. "
                "Do not assume information not present in the notes.\n\n"
                + text)
        st.subheader("Revision Plan")
        st.write(out)

st.divider()
st.subheader("Ask StudyForge")
question = st.text_area("Ask a question about the uploaded notes", placeholder="Explain this topic in very easy language…")
if st.button("Ask locally") and question and text:
    with st.spinner("Thinking on-device…"):
        out = ask_local("Answer this question using the notes below. Explain simply and give a short example if supported.\n\nQUESTION:\n"
                        + question + "\n\nNOTES:\n" + text)
    st.write(out)
elif st.button("Ask locally") and not text:
    st.warning("Upload a PDF first.")
