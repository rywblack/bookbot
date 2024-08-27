def getText():
    with open("books/frankenstein.txt") as f:
        return f.read()

def getWordCount(text):
    words = text.split()
    wc = len(words)
    return wc

def sort_on(d):
    print(f"sort on recieved: {d}")
    return d['value']

def getCharCount(text):
    characters = list(text.lower())
    characterCount = {}
    for c in characters:
        if c not in characterCount:
            characterCount[c] = 1
        else:
            characterCount[c] += 1
    dictList = []
    for char in characterCount:
        if char.isalpha():
            dictList.append({'name': char, 'value': characterCount[char]})

    dictList.sort(reverse=True, key=sort_on)

    for d in dictList:
        print(f"The '{d['name']}' character was found {d['value']} times")

def main():
    text = getText()
    wordCount = getWordCount(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{wordCount} words found in doc")
    getCharCount(text)
    print("--- End report ---")

main()