"""
translator.py

This program is for translating Indian English text to French and vice-versa.
"""

from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    '''
    English text to French
    '''
    french_text = MyMemoryTranslator(source='en-IN', target='fr-FR').translate(english_text)
    return french_text

def french_to_english(french_text):
    '''
    French text to English
    '''
    english_text = MyMemoryTranslator(source='fr-FR', target='en-IN').translate(french_text)
    return english_text
