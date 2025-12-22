
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

DATA_DIR = BASE_DIR / "data"
RAW_TRANSCRIPTS_DIR = DATA_DIR / "raw_transcripts"

MEDICAL_NER_MODEL = "en_ner_bc5cdr_md"
SENTIMENT_MODEL = "distilbert-base-uncased"
INTENT_MODEL = "distilbert-base-uncased"

MAX_SEQUENCE_LENGTH = 512
DEVICE = "cpu"  

ALLOW_INFERENCE = False   

DOCTOR_ALIASES = {
    "doctor",
    "physician",
    "dr",
    "Physician"
    "dr.",
    "surgeon",
    "provider",
    "clinician"
}

PATIENT_ALIASES = {
    "patient",
    "pt",
    "patiient",
    "patientdocter" 
}
