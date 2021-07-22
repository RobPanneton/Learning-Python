phrase = "Arbitrary phrase with numbers 123"
phrase2 = "Arbitraryphrasewithnumbers123"
phraseAlpha = "Arbitraryphrase"
print(phrase)
print(phrase.lower())
print(phrase.isalnum())
print(phrase2.isalnum())

print(phraseAlpha.upper().isupper())
print(len(phrase))

print(phrase[5])

print(phrase.index("A"))
print(phrase.index("phr"))

print(phrase.replace("Arbitrary", "Wacky"))
