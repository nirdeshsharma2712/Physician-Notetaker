class MedicalIntentDetector:
    """
    Detects patient intent from dialogue.
    """

    def detect(self, text: str) -> str:
        text = text.lower()

        if any(word in text for word in ["worried", "scared", "afraid", "concerned"]):
            return "Seeking reassurance"

        if any(word in text for word in ["pain", "hurt", "ache", "discomfort"]):
            return "Reporting symptoms"

        if any(word in text for word in ["better", "improving", "okay now"]):
            return "Expressing improvement"

        return "General conversation"
