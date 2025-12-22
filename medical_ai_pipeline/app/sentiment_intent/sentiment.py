from transformers import pipeline


class MedicalSentimentAnalyzer:
    """
    Classifies patient sentiment into:
    Anxious, Neutral, Reassured
    """

    def __init__(self):
        self.classifier = pipeline(
            "sentiment-analysis",
            model="distilbert-base-uncased-finetuned-sst-2-english"
        )

    def analyze(self, text: str) -> str:
        """
        Analyze patient sentiment.
        """
        text_lower = text.lower()
        anxiety_keywords = [
            "worried",
            "scared",
            "anxious",
            "concerned",
            "afraid"
        ]

        reassurance_keywords = [
            "better",
            "improving",
            "relieved",
            "okay now",
            "fine"
        ]

        if any(word in text_lower for word in anxiety_keywords):
            return "Anxious"

        if any(word in text_lower for word in reassurance_keywords):
            return "Reassured"
        result = self.classifier(text)[0]

        if result["label"] == "NEGATIVE":
            return "Anxious"

        return "Neutral"

