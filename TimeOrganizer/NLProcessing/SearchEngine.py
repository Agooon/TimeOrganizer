from typing import List
from datetime import datetime
import math
import re

import NLProcessing.Strategies as nlpStrat
import NLProcessing.WordsFinder as wf
from NLProcessing.NLPClassDefault import NLPClassDefault
from NLProcessing.NLPSpacyClass import NLPSpacy
from Database.Classes import Event

class SearchEngine():
    def __init__(self, strategy: nlpStrat.StrategyClass, acceptationValue: float):
        self.__nlpClassification = nlpStrat.NLPClassification(strategy)
        self.__acceptationValue = acceptationValue
        self.__eventList : List[Event] = []


    # type has three values 'all', 'before', 'after'
    # Date is used, when type has value 'before' or 'after'
    def searchWithList(self, searchQuery: str, eList: List[Event]) -> List[Event]:
        if(searchQuery == ""):
            return eList
        self.__eventList = eList

        # Classification of words in search query
        print("START classification of query")
        sqClass = self.__nlpClassification.getClassification(searchQuery)
        print("END classification of query")
        # Looking for similiar words of search query

        print("START similar words of query")
        sqSynsList = wf.listOfSimSentence(searchQuery, sqClass)
        print("END similar words of query")

        return self.filterEvents(sqSynsList, sqClass)


    def filterEvents(self, sqSynsList:List[List[str]], sqClass) -> List[Event]:

        length = len(sqSynsList)
        accurateEvents: List[Event] = []

        requiredMatches = math.ceil(self.__acceptationValue * length)

        # START OF for e in self.__eventList
        for e in self.__eventList:
            matches = 0
            # List of description words
            eventWords = e.getWordsList()
           
            for sqWordSyns in sqSynsList:
                found = False
                for eventWord in eventWords:
                    regex = re.compile('[,\.!?]')
                    eventWord = regex.sub('', eventWord)
                    eventWord = eventWord.rstrip()
                    for queryWord in sqWordSyns:
                        if (eventWord.lower() == queryWord.lower()):
                            found = True
                            break
                    if(found):
                        break
                    
                # If the word matches any of similar words
                if(found == True):
                    matches+=1
                    # If the event have already enough words to be displayed
                    # It doesn't check rest of description
                    if(matches >= requiredMatches):
                        accurateEvents.append(e)
                        break;
        # END OF for e in self.__eventList

        return accurateEvents

def getEngineSpacyModel():
    return SearchEngine(NLPSpacy(),0.5)