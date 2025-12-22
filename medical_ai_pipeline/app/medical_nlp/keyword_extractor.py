
from typing import List
import re


class MedicalKeywordExtractor:
    """
    Extracts important medical keywords and phrases
    from clinical or conversational text.
    """

    def __init__(self):
        self.phrase_patterns = [
            r"whiplash injury",
            r"car accident",
            r"back pain",
            r"neck pain",
            r"lower back pain",
            r"physiotherapy sessions?",
            r"physical therapy",
            r"pain management",
            r"soft tissue injury"
        ]

    def extract_keywords(self, text: str) -> List[str]:
        """
        Extract important medical phrases from text.
        """
        text = text.lower()
        keywords = set()
        for pattern in self.phrase_patterns:
            matches = re.findall(pattern, text)
            for match in matches:
                keywords.add(match)
        tokens = re.findall(r"\b[a-z]{4,}\b", text)
        medical_terms = {
            "physiotherapy",
            "discomfort",
            "accident",
            "recovery",
            "injury",
            "treatment"
        }

        for token in tokens:
            if token in medical_terms:
                keywords.add(token)

        return sorted(keywords)
