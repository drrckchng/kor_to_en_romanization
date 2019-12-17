import string
import os
from os import walk
from hangul_romanize import Transliter
from hangul_romanize.rule import academic
from alphabet_detector import AlphabetDetector


path = 'C:\\Users\\user\\Music\\test\\'

def kor2en(str):
    ad = AlphabetDetector()
    inputTitle = str
    outputTitle = ""
    # set invalid chars except . for extension
    invalidChars = set(string.punctuation.replace(".", ""))
    # replace invalid chars
    for i in range(len(inputTitle)):
        if inputTitle[i] not in invalidChars:
            outputTitle += inputTitle[i]
        i+=1
    if not ad.only_alphabet_chars(outputTitle,"LATIN"):
        transliter = Transliter(academic)
        outputTitle = transliter.translit(outputTitle)
    return outputTitle

# rename
for filename in os.listdir(path):
    os.rename(os.path.join(path, filename), os.path.join(path, kor2en(filename)))
