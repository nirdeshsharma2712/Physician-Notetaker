
from typing import Dict, Any
import os
import json
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

class SOAPNoteGenerator:
    """
    Generates structured SOAP notes using Gemini (OpenAI-compatible API).
    """

    def __init__(
        self,
        transcript_text: str,
        entities: Dict[str, Any],
        keywords: list,
        gemini_api_key: str | None = None,
    ):
        self.transcript = transcript_text
        self.entities = entities
        self.keywords = keywords

        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables.")
        self.client = OpenAI(
            api_key=self.api_key,
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
        )

    def generate_soap_note(self) -> Dict[str, Any]:
        system_prompt = """
You are a medical documentation system.
Your task is to generate a SOAP note used by clinicians.
You MUST:
- Use ONLY the information provided
- Do NOT hallucinate new findings
- Return VALID JSON ONLY
- Follow the exact structure provided
"""

        user_prompt = f"""
Conversation Transcript:
{self.transcript}

Extracted Medical Entities:
{json.dumps(self.entities, indent=2)}

Important Keywords:
{self.keywords}

Generate a SOAP note in EXACTLY the following JSON format.
Do not add or remove keys.
Do not add explanations.
Do not include markdown.

{{
  "Subjective": {{
    "Chief_Complaint": "",
    "History_of_Present_Illness": ""
  }},
  "Objective": {{
    "Physical_Exam": "",
    "Observations": ""
  }},
  "Assessment": {{
    "Diagnosis": "",
    "Severity": ""
  }},
  "Plan": {{
    "Treatment": "",
    "Follow-Up": ""
  }}
}}
"""

        response = self.client.chat.completions.create(
            model="gemini-2.5-flash",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.0,
        )

        content = response.choices[0].message.content.strip()

        try:
            return json.loads(content)
        except json.JSONDecodeError:
            return {
                "error": "Invalid JSON returned by Gemini",
                "raw_output": content
            }
