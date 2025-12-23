# 🩺 Medical AI Pipeline  - Live preview : [Here](https://physician-notetaker.streamlit.app/)

### End-to-End Medical NLP System for Transcription Analysis, Summarization & SOAP Notes

An end-to-end **Medical AI pipeline** that processes **doctor–patient conversations** and automatically generates structured clinical insights such as **medical entities, summaries, patient sentiment, intent, and SOAP notes**.

This project is designed for **CPU-only environments**, making it ideal for **demos, interviews, PoCs, and Streamlit Cloud deployment**.


## 🛠️ Installation (Step-by-Step)

### ✅ Prerequisites

> - Python **3.9 – 3.11**
> - pip
> - Git


### 🔹 Step 1: Clone Repository
<pre>
  - git clone https://github.com/<your-username>/medical_ai_pipeline.git 
  - cd medical_ai_pipeline
</pre> 

### 🔹 Step 2: Create Virtual Environment

<pre> 
  - python -m venv venv
</pre>

### 🔹 Step 3: Activate the Environment

<pre>
  Windows - venv\Scripts\activate
  Linux / macOS - source venv/bin/activate
</pre>

### 🔹 Step 4: Install Dependencies
<pre>
  - pip install -r requirements.txt
</pre>

### 🔹 Step 5: Environment Variables (Optional)

- Required only if using OpenAI or Gemini for SOAP note generation.
- Create a .env file in the project root:
  > - OPENAI_API_KEY=your_openai_key_here
  > - GEMINI_API_KEY=your_gemini_key_here


## ▶️ Running the Pipeline (CLI)

### 1️⃣ Add Conversation Transcript
-  Place your conversation in:
> - data/raw_transcripts/sample.txt

Example:
<pre> 
  - Doctor: Hello, Ms. Jones. How are you feeling today?
  - Patient: I had a car accident. My neck and back hurt for four weeks.
  - Doctor: Did you receive treatment?
  - Patient: Yes, physiotherapy sessions helped.
</pre>

### 2️⃣ Run the Pipeline

> - python app/pipeline.py


## 💬 Running the Streamlit UI
> - streamlit run app/ui/streamlit_app.py


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
```

## 🤝 Contributions
- Contributions, suggestions, and improvements are welcome.
- Feel free to open an issue or submit a pull request.

