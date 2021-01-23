from pydantic import BaseModel
from datetime import datetime
from datetime import timedelta
from typing import List
import re

class Event(BaseModel):
    id : int = None
    name : str = 'Default event name'
    dateStart : datetime = datetime.now()
    dateEnd : datetime = datetime.now() + timedelta(days=1)
    description : str = 'Default event description'

    length : timedelta = 0
    timeUntilStart : timedelta = 0
    timeUntilEnd : timedelta = 0

    # For NLP search, list of similar words for each word in sentence
    # !!!  NO NEED FOR IT !!!
    # similarWords: List[List[str]] = []


    def __str__(self):
        return ('''Id: {}
        Name: {}
        DateStart: {}
        DateEnd: {}
        Length: {}
        TimeUntilStart: {}
        TimeUntilEnd: {}
        Description: {}'''
        .format(self.id, self.name, 
                self.dateStart.strftime("%Y-%m-%d %H:%M:%S"), self.dateEnd.strftime("%Y-%m-%d %H:%M:%S"), 
                self.length, self.timeUntilStart, self.timeUntilEnd, self.description))

    def calcTimedeltas(self, actualTime: datetime):
        self.length = self.dateEnd - self.dateStart
        holderStart = max((self.dateStart - actualTime),timedelta(0))
        self.timeUntilStart = timedelta(days=holderStart.days, seconds=holderStart.seconds)
        holderEnd = max((self.dateEnd - actualTime),timedelta(0))
        self.timeUntilEnd = timedelta(days=holderEnd.days, seconds=holderEnd.seconds)

    def getWordsList(self):
        regex = re.compile('[,\.!?]')
        desc = regex.sub('', (self.name + " " + self.description).lower())
        return desc.split(" ")



#def testEvent():
#    ev = Event(**{
#            'name': 'Adam',

#            'description': 'test the thing',
#            'descriptionClass': 'v - n'})
#    print(ev.id)
#    print(ev.name)
#    print(ev.dateStart)
#    print(ev.dateEnd)
#    print(ev.description)
#    print(ev.descriptionClass)