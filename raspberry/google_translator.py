from googletrans import Translator
import googletrans
translator = Translator()
translations = translator.translate(['The quick brown fox', 'jumps over', 'the lazy dog'], dest='fr')
for translation in translations:
    print(translation.origin, ' -> ', translation.text)
global x
def language_trans(language):
    dict = googletrans.LANGUAGES
    for i,j in dict.items():
        if j == language:
            x= translator.translate('good morning', dest=i)
    return x.pronunciatio
print(googletrans.LANGUAGES)
