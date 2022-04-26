"""
high level support for doing this and that.
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    authenticator=authenticator,
    version='2022-04-26'
)

language_translator.set_service_url(url)

def englishToFrench(englishText):
    """ Translates English test to French """
    translation_response = language_translator.translate(englishText, model_id='en-fr').get_result()
    frenchText = translation_response['translations'][0]['translation']
    return frenchText

def frenchToEnglish(englishText):
    """ Translates French test to English """
    translation_response = language_translator.translate(englishText, model_id='fr-en').get_result()
    englishText = translation_response['translations'][0]['translation']
    return englishText
