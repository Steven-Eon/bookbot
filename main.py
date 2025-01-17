def getWordCount(data):
    wordSplit = data.split()
    return len(wordSplit)

with open("./books/frankenstein.txt") as f:
    file_contents = f.read()
    print(getWordCount(file_contents))
