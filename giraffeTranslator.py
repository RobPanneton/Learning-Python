
def translate(phrase):
    translated = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translated += "g"
        else:
            translated += letter
    return translated


print(translate(input("type in your input: ")))
