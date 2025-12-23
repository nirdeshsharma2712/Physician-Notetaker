# 🩺 Medical AI Pipeline  
### End-to-End Medical NLP System for Transcription Analysis, Summarization & SOAP Notes

An end-to-end **Medical AI pipeline** that processes **doctor–patient conversations** and automatically generates structured clinical insights such as **medical entities, summaries, patient sentiment, intent, and SOAP notes**.

This project is designed for **CPU-only environments**, making it ideal for **demos, interviews, PoCs, and Streamlit Cloud deployment**.

---

## 📌 Key Capabilities

✅ Medical Entity Extraction  
✅ Structured Medical Summarization  
✅ Patient Sentiment & Intent Analysis  
✅ SOAP Note Generation  
✅ Interactive Streamlit Chat UI  
✅ Modular, extensible architecture  
✅ Deployment-ready (Streamlit Cloud)

---

## 🧠 System Overview

The pipeline takes raw doctor–patient conversations and produces:

- 🧬 **Medical Entities** (Symptoms, Diagnosis, Treatment, Duration, Prognosis)
- 📋 **Structured Medical Summary (JSON)**
- 🧠 **Patient Sentiment & Intent**
- 📝 **SOAP Notes (Subjective, Objective, Assessment, Plan)**
- 💬 **Interactive Chat-based UI**

---


## 🛠️ Installation (Step-by-Step)

### ✅ Prerequisites
- Python **3.9 – 3.11**
- pip
- Git

---

### 🔹 Step 1: Clone Repository
```bash
git clone https://github.com/<your-username>/medical_ai_pipeline.git
cd medical_ai_pipeline


## 🧬 Core Features

### 1️⃣ Medical NLP (NER)

Extracts the following entities:
- Patient Name  
- Symptoms  
- Diagnosis  
- Treatments  
- Duration & Temporal References  
- Prognosis  

**Techniques Used:**
- Transformer-based models (BioBERT / DistilBERT)
- Lightweight medical rule-based heuristics
- Regex-based temporal & name extraction

---

### 2️⃣ Structured Medical Summary

Converts raw conversations into a clean, structured JSON format.

**Example Output:**
```json
{
  "Symptoms": ["Neck pain", "Back pain"],
  "Diagnosis": "Whiplash injury",
  "Treatment": ["Physiotherapy"],
  "Current_Status": "Occasional pain",
  "Prognosis": "Improving"
}
