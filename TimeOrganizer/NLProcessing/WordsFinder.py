import nltk
from nltk.corpus import wordnet 
from nltk.stem.wordnet import WordNetLemmatizer
from typing import List
import time
import re

def listOfSimWord(word: str, pos: str):
    wordList = [word]
    for syn in wordnet.synsets(word, pos):
        for l in syn.lemmas(): 
            wordList.append(l.name().lower())
    return set(wordList)

def listOfSimSentence(sentence: str, positions: str):

    posList = positions.split(' ')
    sentenceList = sentence.split(' ')

    synsList : List[List[str]] = []
    index = 0

    for word in sentenceList:
        regex = re.compile('[,\.!?]')
        word = regex.sub('', word)
        if (str(word).isalpha() or str(word).isnumeric()):
            synsList.append(listOfSimWord(word, posList[index]))
            index+=1
    # returning a symList
    return synsList



# THE CODE BEFORE THE CHANGE

class SingleSearch():
    # For not searching the same words
    def __init__(self, name:str, values: List[str]):
        self.__name = name
        self.__values = values

    def getValues(self):
        return self.__values

    def getName(self):
        return self.__name

class DescriptionSim():
    # For not searching the same descriptions
    def __init__(self, name:str, values: List[List[str]]):
        self.__name = name
        self.__values = values

    def getValues(self):
        return self.__values

    def getName(self):
        return self.__name

def listOfSimSentenceBefore(sentence: str, positions: str):
#                      doneSearches: List[SingleSearch] = [], 
#                      doneDescriptions:List[DescriptionSim] = []):

    # Checking if the same description accured before
    # NO NEED TO CHECK IT
#    for desc in doneDescriptions:
#        if(desc.getName() == sentence):
#            return desc.getValues(), doneSearches, doneDescriptions

    posList = positions.split(' ')
    sentenceList = sentence.split(' ')

    symList : List[List[str]] = []
    index = 0

    for word in sentenceList:
        # NO NEED
        #symilarWords = []
        #found = False
        #for search in doneSearches:
        #    # For example run.v happends twice,
        #    if(search.getName() == word + posList[index]):
        #        symilarWords = search.getValues()
        #        found = True
        #        break
        #if(not found):
        #    symilarWords = listOfSimWord(word, posList[index])
        #    doneSearches.append(SingleSearch(word + posList[index], symilarWords))       

        symList.append(listOfSimWord(word, posList[index]))
        index+=1

    #doneDescriptions.append(DescriptionSim(sentence,symList))
    # returning a symList
    return symList



def testing2():
    print(listOfSimWord('run', 'v'))
    print()
    desc1 = ['xd -', 'run v','description n', 'doing n', 'xd -', 'run v','description n', 'doing n', 'xd -', 'run v','description n', 'doing n', 'xd -', 'run v','description n', 'doing n', 'xd -', 'run v','description n', 'doing n',
              'doing n', 'xd -', 'run v','description n','doing n', 'xd -', 'run v','description n','doing n', 'xd -', 'run v','description n',
               'doing n', 'xd -', 'run v','description n','doing n', 'xd -', 'run v','description n','doing n', 'xd -', 'run v','description n']
    desc2 = ['xd -', 'run v','descriptio2 n', 'doing n', 'xd -', 'run v','description n', 'doing n', 'xd -', 'run v','description n', 'doing n', 'xd -', 'run v','description n', 'doing n', 'xd -', 'run v','description n', 'doing n',
              'doing n', 'xd -', 'run v','description n','doing n', 'xd -', 'run v','description n','doing n', 'xd -', 'run v','description n',
               'doing n', 'xd -', 'run v','description n','doing n', 'xd -', 'run v','description n','doing n', 'xd -', 'run v','description n']
    start = time.time()
    for i in range(100):
        for word in words:
            w = word.split(" ")
            if w[1] != "-":
                listOfSimWord(w[0], w[1])
                #print(listOfSimWord(w[0], w[1])) 
            else:
                pass
            #print()
    end = time.time()
    print(end-start)
