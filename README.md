# 🩺 Medical AI Pipeline

**End-to-End Medical NLP System for Transcription Analysis, Summarization & SOAP Notes**

---

## 📌 Overview

This project is an **end-to-end Medical AI pipeline** that processes doctor–patient conversations and produces:

- 🧬 **Medical Entity Extraction** (Symptoms, Diagnosis, Treatment, Duration, Prognosis)
- 📋 **Structured Medical Summary**
- 🧠 **Patient Sentiment & Intent Analysis**
- 📝 **SOAP Note Generation**
- 💬 **Interactive Streamlit Chat UI**

The system is designed to be:

- ✅ **CPU-only**
- ✅ **Modular & extensible**
- ✅ **Deployment-ready (Streamlit Cloud)**
- ✅ **Ideal for demos, interviews, and PoCs**

---

## 🏗️ Project Architecture

medical_ai_pipeline/
│
├── data/
│ ├── raw_transcripts/
│ │ └── sample.txt
│ ├── examples/
│ │ └── sample_output.json
│
├── app/
│ ├── config/
│ │ └── settings.py
│
│ ├── preprocessing/
│ │ └── text_cleaner.py
│
│ ├── medical_nlp/
│ │ ├── ner.py
│ │ ├── keyword_extractor.py
│ │ └── summarizer.py
│
│ ├── sentiment_intent/
│ │ ├── sentiment.py
│ │ └── intent.py
│
│ ├── soap/
│ │ └── soap_generator.py
│
│ ├── schemas/
│ │ ├── medical_summary.py
│ │ ├── sentiment.py
│ │ └── soap.py
│
│ └── pipeline.py
│
├── tests/
│ └── test_pipeline.py
│
├── requirements.txt
└── README.md


---

## 🧠 Core Features

### 1️⃣ Medical NLP (NER)

Extracts:
- Patient name
- Symptoms
- Diagnosis
- Treatments
- Duration & dates
- Prognosis

**Approach**
- Transformer-based models (BioBERT / DistilBERT)
- Lightweight medical rules for higher precision

---

### 2️⃣ Structured Medical Summary

Converts raw conversation into a clean, machine-readable JSON:

```json
{
  "Symptoms": ["Neck pain", "Back pain"],
  "Diagnosis": "Whiplash injury",
  "Treatment": ["Physiotherapy"],
  "Current_Status": "Occasional pain",
  "Prognosis": "Improving"
}
