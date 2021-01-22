from typing import List
from datetime import datetime
import math

import NLProcessing.Strategies as nlpStrat
import Database.Operations as myDb
import NLProcessing.WordsFinder as wf
from NLProcessing.NLPClassDefault import NLPClassDefault
from NLProcessing.NLPSpacyClass import NLPSpacy
from Database.Initialization import nameOfDatabase
from Database.Classes import Event

acceptationValue = 0.5

class SearchEngine():
    def __init__(self, strategy: nlpStrat.StrategyClass, acceptationValue: float):
        self.__nlpClassification = nlpStrat.NLPClassification(strategy)
        self.__acceptationValue = acceptationValue
        self.__eventList : List[Event] = []

    def getEventList(self, type:str, date:datetime):
        if(type == 'all'):
            self.__eventList = myDb.getEvents(nameOfDatabase)
        elif(type == 'before'):
            self.__eventList = myDb.getEventsBefore(nameOfDatabase, date)
        else:
            self.__eventList = myDb.getEventsAfter(nameOfDatabase, date)

    # type has three values 'all', 'before', 'after'
    # Date is used, when type has value 'before' or 'after'
    def search(self, searchQuery: str, type: str, date:datetime) -> List[Event]:
        self.getEventList(type, date)

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
                    if (eventWord in sqWordSyns):
                        found = True
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



def testing3():
    #sEngine = SearchEngine(NLPClassDefault(),0.5)
    sEngine = SearchEngine(NLPSpacy(),0.5)

    for e in sEngine.search("call me 3a Two",'all', None):
        print(e)
        print()
