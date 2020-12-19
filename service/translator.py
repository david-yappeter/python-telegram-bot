from googletrans import Translator

def TranslateIndoToEnglish(text):
    translator = Translator()
    resp = translator.translate(text)
    return resp.text