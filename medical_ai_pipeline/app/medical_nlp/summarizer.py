from typing import Dict, List


class MedicalSummarizer:
    """
    Builds a structured medical summary
    from extracted entities and keywords.
    """

    def __init__(
        self,
        entities: Dict[str, List[str]],
        keywords: List[str],
        patient_text: str,
    ):
        self.entities = entities
        self.keywords = keywords
        self.patient_text = patient_text.lower()

    def _current_status(self) -> str:
        """
        Infer current patient status conservatively.
        """
        if "occasional" in self.patient_text:
            return "Occasional symptoms present"
        if "better" in self.patient_text or "improving" in self.patient_text:
            return "Symptoms improving"
        if "pain" in self.patient_text:
            return "Ongoing pain reported"
        return "Status not clearly stated"

    def _prognosis(self) -> str:
        """
        Infer prognosis only if explicitly hinted.
        """
        prognosis = self.entities.get("Prognosis", [])
        if prognosis:
            return prognosis[0]
        return "Not mentioned"

    def build_summary(self) -> Dict[str, object]:
        """
        Build final structured medical summary.
        """
        return {
            "Symptoms": self.entities.get("Symptoms", []),
            "Diagnosis": (
                self.entities["Diagnosis"][0]
                if self.entities.get("Diagnosis")
                else "Not mentioned"
            ),
            "Treatment": self.entities.get("Treatment", []),
            "Current_Status": self._current_status(),
            "Prognosis": self._prognosis(),
            "Keywords": self.keywords,
        }

