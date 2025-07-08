import requests
from flask_babel import _
from app import app

def translate(text, source_language, dest_language):
    dest_language = dest_language.split('_')[0].split('-')[0] if dest_language else ''
    source_language = source_language.split('_')[0].split('-')[0] if source_language else ''
    if not dest_language:
        dest_language = 'en'
    if not source_language:
        source_language = 'en'
    if 'MS_TRANSLATOR_KEY' not in app.config or not app.config['MS_TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured.')
    headers = {
        'Ocp-Apim-Subscription-Key': app.config['MS_TRANSLATOR_KEY'],
        'Ocp-Apim-Subscription-Region': 'eastus',
        'Content-Type': 'application/json'
    }
    r = requests.post(
        'https://api.cognitive.microsofttranslator.com'
        '/translate?api-version=3.0&from={}&to={}'.format(
            source_language, dest_language), headers=headers, json=[{'Text': text}])
    if r.status_code != 200:
        return _('Error: the translation service failed.')
    result = r.json()
    try:
        return result[0]['translations'][0]['text']
    except (KeyError, IndexError):
        return _('Error: could not parse translation response.')