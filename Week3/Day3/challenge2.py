from translate import Translator
french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"] 

translator = Translator(to_lang="en", provider='mymemory', from_lang="fr")
# print(translator.translate(french_words))
res = {}
for x in french_words:
    translation = translator.translate(x)
    res[x] = translation

print(res)