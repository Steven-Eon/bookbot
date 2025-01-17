def main():
    filePath = "./books/frankenstein.txt"
    try:
        data = openFile(filePath)
        wordCount = getWordCount(data)
        charCount = getCharCount(data)

        print(f"--- Beginning report of {filePath}. ---")
        print(f"There is approximately {wordCount} words in this file. \n")
        for i in charCount.keys():
            if (not i.isalpha()):
                continue
            print(f"There is approximately {charCount[i]} instances of the character '{i}'.")
        print(f"--- End of report for {filePath}. --- \n")
    except Exception as e:
        print(e)

def getWordCount(data):
    if (type(data) != str):
        raise Exception("String not provided.")
    wordSplit = data.split()
    return len(wordSplit)

def getCharCount(data):
    if (type(data) !=  str):
        raise Exception("String not provided.")
    charCount = {}
    for i in data.split():
        for j in range(len(i)):
            if i[j].lower() in charCount:
                charCount[i[j].lower()] = charCount[i[j].lower()] + 1
            else:
                charCount[i[j].lower()] = 1
    return charCount

def openFile(filePath):  
    with open(filePath) as f:
        return f.read()

main()
