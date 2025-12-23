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

## 🛠️ Installation (Step-by-Step)

### ✅ Prerequisites

- Python **3.9 – 3.11**
- `pip`
- Git

---

### 🔹 Step 1: Clone Repository

```bash
git clone https://github.com/<your-username>/medical_ai_pipeline.git
cd medical_ai_pipeline

Doctor: Hello, Ms. Jones. How are you feeling today?
Patient: I had a car accident. My neck and back hurt for four weeks.
Doctor: Did you receive treatment?
Patient: Yes, physiotherapy sessions helped.


---

If you want next:
- 🔖 **README badges**
- 📄 **One-page project summary**
- 🎯 **Interview-ready explanation**
- 🧪 **Sample outputs section**

Just tell me 👌

