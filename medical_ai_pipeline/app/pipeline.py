
from app.config.settings import RAW_TRANSCRIPTS_DIR
from app.preprocessing.text_cleaner import TextPreprocessor
from app.medical_nlp.ner import MedicalNER
from app.medical_nlp.keyword_extractor import MedicalKeywordExtractor
from app.medical_nlp.summarizer import MedicalSummarizer
from app.sentiment_intent.sentiment import MedicalSentimentAnalyzer
from app.sentiment_intent.intent import MedicalIntentDetector
from app.soap.soap_generator import SOAPNoteGenerator
import json

def run_pipeline(sample_file: str):

    with open(sample_file, "r", encoding="utf-8") as f:
        transcript = f.read()
    preprocessor = TextPreprocessor(transcript)
    processed = preprocessor.preprocess()  

    ner = MedicalNER()
    entities = ner.extract_entities(processed["full_text"])

    keyword_extractor = MedicalKeywordExtractor()
    keywords = keyword_extractor.extract_keywords(processed["full_text"])

    sentiment_analyzer = MedicalSentimentAnalyzer()
    intent_detector = MedicalIntentDetector()

    sentiment = sentiment_analyzer.analyze(processed["full_text"])
    intent = intent_detector.detect(processed["full_text"])
    print(sentiment)
    print(intent)
   
    summarizer = MedicalSummarizer(
        entities=entities,
        keywords=keywords,
        patient_text=processed["patient_text"]
    )
    summary = summarizer.build_summary()


    # Gemini API used for this - so add in .env and remove comment from code - 


    # SOAP note
    # soap_generator = SOAPNoteGenerator(
    #     transcript_text=processed["full_text"],
    #     entities=entities,
    #     keywords=keywords
    # )
    # soap_note = soap_generator.generate_soap_note()

    return {
        "Entities": entities,
        "Structured_Summary": summary,
        "Patient_Sentiment": sentiment,
        "Patient_Intent": intent,
        # "SOAP_Note": soap_note
    }
