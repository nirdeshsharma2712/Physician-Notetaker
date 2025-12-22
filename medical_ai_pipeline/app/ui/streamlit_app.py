import sys
from pathlib import Path
import streamlit as st
import json

CURRENT_FILE = Path(__file__).resolve()

for parent in CURRENT_FILE.parents:
    if (parent / "app").exists():
        sys.path.append(str(parent))
        break


from app.pipeline import run_pipeline

st.set_page_config(
    page_title="Medical AI Pipeline",
    layout="wide"
)

st.title("🩺 Medical AI Pipeline")
st.caption("Medical NLP • Summarization • Sentiment • SOAP Notes")

st.subheader("💬 Enter Doctor–Patient Conversation")

conversation = st.text_area(
    "Paste the medical conversation below:",
    height=250,
    placeholder="Doctor: Hello, Ms. Jones...\nPatient: I had a car accident..."
)

if st.button("🚀 Run Analysis"):
    if not conversation.strip():
        st.warning("Please enter a medical conversation.")
    else:

        data_path = PROJECT_ROOT / "data" / "raw_transcripts" / "sample.txt"
        data_path.write_text(conversation, encoding="utf-8")

        with st.spinner("Running medical AI pipeline..."):
            output = run_pipeline(str(data_path))

        st.success("Analysis completed successfully")

        st.divider()

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("🧬 Medical Entities")
            st.json(output.get("Entities", {}))

        with col2:
            st.subheader("📋 Structured Medical Summary")
            st.json(output.get("Structured_Summary", {}))

        st.divider()

        st.subheader("🧠 Patient Sentiment & Intent")
        st.json({
            "Sentiment": output.get("Patient_Sentiment", "Not available"),
            "Intent": output.get("Patient_Intent", "Not available")
        })

        st.divider()

        # st.subheader("📝 SOAP Note")
        # st.json(output.get("SOAP_Note", {}))
