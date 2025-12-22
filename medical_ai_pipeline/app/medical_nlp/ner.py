from typing import Dict, List
import spacy
import re
from app.config.settings import MEDICAL_NER_MODEL

class MedicalNER:
    """
    Medical Named Entity Recognition using SciSpacy.
    """

    WORD_NUMBERS = {
        "one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
        "six": "6", "seven": "7", "eight": "8", "nine": "9", "ten": "10"
    }

    def __init__(self):
        self.nlp = spacy.load(MEDICAL_NER_MODEL)

    def extract_entities(self, text: str) -> Dict[str, List[str]]:
        """
        Extract medical entities from text.
        """
        doc = self.nlp(text)

        symptoms: List[str] = []
        diagnosis: List[str] = []
        treatments: List[str] = []
        prognosis: List[str] = []
        durations: List[str] = []
        patient_name: str = "Not specified"
        for ent in doc.ents:
            label = ent.label_.lower()
            value = ent.text.strip()

            if label == "disease":
                diagnosis.append(value)
            elif label == "chemical":
                treatments.append(value)
        text_lower = text.lower()

        symptom_keywords = ["pain", "ache", "hurt", "discomfort", "stiffness", "dizzy", "nausea"]
        for word in symptom_keywords:
            if word in text_lower:
                symptoms.append(word)

        if "physiotherapy" in text_lower:
            treatments.append("Physiotherapy")
        if "surgery" in text_lower:
            treatments.append("Surgery")
        if "medication" in text_lower or "painkillers" in text_lower:
            treatments.append("Medication")

        if "improving" in text_lower or "better" in text_lower:
            prognosis.append("Improving")

        duration_patterns = [
            r'for (?:the past )?(?:about |around )?(\d+|one|two|three|four|five|six|seven|eight|nine|ten)\s+(day|days|week|weeks|month|months|year|years)',
            r'past (\d+|one|two|three|four|five|six|seven|eight|nine|ten)\s+(day|days|week|weeks|month|months|year|years)',
            r'over (?:the )?past (\d+|one|two|three|four|five|six|seven|eight|nine|ten)\s+(day|days|week|weeks|month|months|year|years)',
            r'since ([A-Za-z0-9]+(?:\s[A-Za-z0-9]+){0,3})',
        ]

        durations = []

        for pattern in duration_patterns:
            matches = re.findall(pattern, text_lower, re.IGNORECASE)
            for m in matches:
                if isinstance(m, tuple):
                    num, unit = m[0], m[1]
                    num = self.WORD_NUMBERS.get(num.lower(), num)
                    durations.append(f"{num} {unit}")
                else:
                    durations.append(m.strip())

        durations = list(set(durations)) if durations else ["Not specified"]

        def extract_patient_name(text: str) -> str:
            """
            Ultra-simple, robust patient name extraction.
            Finds mr/ms/mrs in lowercase text and returns the next word.
            """

            text_lower = text.lower()

            titles = ["mr.", "ms.", "mrs."]

            for title in titles:
                if title in text_lower:
                   
                    after_title = text_lower.split(title, 1)[1]

               
                    name = after_title.strip().split()[0]

            
                    return f"{title.strip().capitalize()} {name.capitalize()}"

            return "Not specified"

        patient_name = extract_patient_name(text)
        symptoms = list(set([s.lower().rstrip('s') for s in symptoms]))
        diagnosis = list(set([d.lower().rstrip('s') for d in diagnosis]))
        treatments = list(set([t.capitalize() for t in treatments]))
        prognosis = list(set([p.capitalize() for p in prognosis]))

        return {
            "Patient_Name": patient_name,
            "Symptoms": symptoms if symptoms else ["Not specified"],
            "Diagnosis": diagnosis if diagnosis else ["Not specified"],
            "Treatment": treatments if treatments else ["Not specified"],
            "Duration": durations if durations else ["Not specified"],
            "Prognosis": prognosis if prognosis else ["Not mentioned"]
        }

