
import re
from typing import Dict, List
from app.config.settings import DOCTOR_ALIASES, PATIENT_ALIASES


class TextPreprocessor:
    def __init__(self, raw_text: str):
        self.raw_text = raw_text
    def _clean_formatting(self, line: str) -> str:
        """
        Removes markdown symbols, bullets, and formatting.
        """
        line = re.sub(r"^>\s*", "", line)
        line = re.sub(r"\*{1,2}", "", line)
        line = re.sub(r"\s+", " ", line).strip()

        return line

    def _identify_speaker(self, line: str) -> str | None:
        """
        Identify speaker type using alias matching.
        """
        match = re.match(r"^([a-zA-Z\s\.]+):", line)
        if not match:
            return None

        speaker_raw = match.group(1).lower().strip()
        speaker_clean = re.sub(r"[^\w]", "", speaker_raw)

        if speaker_clean in DOCTOR_ALIASES:
            return "doctor"
        if speaker_clean in PATIENT_ALIASES:
            return "patient"

        return None

    def separate_speakers(self) -> Dict[str, str]:
        doctor_lines: List[str] = []
        patient_lines: List[str] = []

        for raw_line in self.raw_text.splitlines():
            raw_line = raw_line.strip()
            if not raw_line:
                continue
            line = self._clean_formatting(raw_line)

            speaker = self._identify_speaker(line)
            content = re.sub(r"^[^:]+:", "", line).strip()

            if speaker == "doctor":
                doctor_lines.append(content)
            elif speaker == "patient":
                patient_lines.append(content)
            else:
                patient_lines.append(content)

        return {
            "doctor_text": " ".join(doctor_lines),
            "patient_text": " ".join(patient_lines),
            "full_text": " ".join(doctor_lines + patient_lines),
        }

    def normalize_text(self, text: str) -> str:
        """
        Normalize medical text.
        """
        text = text.lower()

        text = re.sub(r"\bfour weeks\b", "4 weeks", text)
        text = re.sub(r"\bten\b", "10", text)

        text = re.sub(r"\s+", " ", text).strip()

        return text

    def preprocess(self) -> Dict[str, str]:
        """
        Full preprocessing pipeline.
        """
        separated = self.separate_speakers()

        return {
            "doctor_text": self.normalize_text(separated["doctor_text"]),
            "patient_text": self.normalize_text(separated["patient_text"]),
            "full_text": self.normalize_text(separated["full_text"]),
        }
