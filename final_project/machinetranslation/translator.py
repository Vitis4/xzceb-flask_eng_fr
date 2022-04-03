from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('Ze4FnlJZIqXnQU19HR7ZaJ7u_itfvYXUOMitle0mdTXr')
language_translator = LanguageTranslatorV3(version='2018-05-01',authenticator=authenticator) 
language_translator.set_service_url('https://api.eu-gb.language-translator.watson.cloud.ibm.com')

def english_to_french(text4):
    """Function translates English to French"""
    frenchtranslation = language_translator.translate(text=text4, model_id='en-fr').get_result()
    text4 = frenchtranslation['translations'][0]['translation']
    return text4

def french_to_english(text5):
    """Function translates French to English"""
    englishtranslation = language_translator.translate(text=text5, model_id='fr-en').get_result()
    text5 = englishtranslation['translations'][0]['translation']
    return text5