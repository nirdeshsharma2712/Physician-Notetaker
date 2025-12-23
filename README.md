# 🩺 Medical AI Pipeline
**End-to-End Medical NLP System for Transcription Analysis, Summarization & SOAP Notes**

# Live preview - https://physician-notetaker.streamlit.app/

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


## 🛠️ Installation (Step-by-Step)

### ✅ Prerequisites

- Python **3.10.7**
- `pip`
- Git


### 🔹 Step 1: Clone Repository

<code>git clone https://github.com/nirdeshsharma2712/Physician-Notetaker.git <code>
<code>cd medical_ai_pipeline<code>

### 🔹 Step 2: Create Virtual Environment

<code>python -m venv venv</code>


### 🔹 Step 3: Activate the Virtual Environment

Windows -  <code>venv\Scripts\activate</code>
Linux / macOS - <code>source venv/bin/activate</code>

### 🔹 Step 4: Install Dependencies

<code> pip install -r requirements.txt</code>


### 🔹 Step 4: Environment Variables 

Create a `.env` file in the project root:

<code> OPENAI_API_KEY=your_openai_key_here</code>
or
<code>GEMINI_API_KEY=your_gemini_key_here</code>

## ▶️ Running the Pipeline (CLI)

### 1️⃣ Add Medical Conversation

 - Place your conversation in the file below:
 - `data/raw_transcripts/sample.txt`

Example - 
<pre>
  Doctor: Hello, Ms. Jones. How are you feeling today?
  Patient: I had a car accident. My neck and back hurt for four weeks.
  Doctor: Did you receive treatment?
  Patient: Yes, physiotherapy sessions helped.
</pre>

### 2️⃣ Run the Pipeline
<code> python app/pipeline.py </code>


## 💬 Running the Streamlit UI

<code> streamlit run app/ui/streamlit_app.py</code>
Open the browser and interact with the chat-style medical analysis UI.


## 📦 Dependencies Explained

- `transformers` → NLP models
- `torch` → CPU-based inference
- `streamlit` → Web UI
- `openai` / `google-generativeai` → LLM integration
- `regex` → Temporal & medical entity extraction
- `python-dotenv` → Environment variable management

  
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

`{
  "Symptoms": ["Neck pain", "Back pain"],
  "Diagnosis": "Whiplash injury",
  "Treatment": ["Physiotherapy"],
  "Current_Status": "Occasional pain",
  "Prognosis": "Improving"
}`

### 👨‍💻 Author

- Built with ❤️ as an end-to-end Medical AI system, designed to demonstrate:
- NLP engineering
- ML pipeline design
- Clean, modular architecture
- Production-ready UI

