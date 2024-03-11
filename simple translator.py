from mtranslate import translate


def translater(text, tran_lang='en'):
    translated_text = translate(text, tran_lang)
    return translated_text


text = input("Enter text for translate(in russian): ")
tran_lang = input("Enter target language(for ex. en): ")
translated_text = translater(text, tran_lang)
print("Result:", translated_text)