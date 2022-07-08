"""
This program translates text from one language to another (English to French) and vice versa.
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3( version='2018-05-01',authenticator=authenticator)
language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com')

def english_to_french(english_text):
    """Performs english to french translation

    Args:
        englishTest (String): French text to be translated

    Returns:
        frenchText (String): Translated text in french
    """
    try:
        french_text = language_translator.translate(
          text=english_text, model_id='en-fr').get_result()
        return french_text['translations'][0]['translation']
    except:
        return ""

def french_to_english(french_text):
    """_summary_: Performs french to english translation

    Args:
        frenchText (String): French text to be translated

    Returns:
        englishText (String) : Translated text in english
    """
    try:
        english_text = language_translator.translate(
        text=french_text, model_id='fr-en').get_result()
        return english_text['translations'][0]['translation']
    except:
        return ""
