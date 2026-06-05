import re
import logging

logger = logging.getLogger(__name__)

def detect_language(text: str) -> str:
    """
    Detects language of a text string.
    Returns 'kn' for Kannada, 'hi' for Hindi, and 'en' for English.
    """
    if not text:
        return "en"
        
    # Check for Kannada characters (Unicode range: U+0C80 to U+0CFF)
    if re.search(r'[\u0c80-\u0cff]', text):
        logger.info("Language detected: Kannada (kn)")
        return "kn"
        
    # Check for Hindi/Devanagari characters (Unicode range: U+0900 to U+097F)
    if re.search(r'[\u0900-\u097f]', text):
        logger.info("Language detected: Hindi (hi)")
        return "hi"
        
    # Default fallback
    logger.info("Language detected: English (en)")
    return "en"
