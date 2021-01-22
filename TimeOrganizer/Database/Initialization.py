import sqlite3
import pathlib
import os
from Database.Operations import *
from datetime import datetime
from datetime import timedelta

nameOfDatabase = str(pathlib.Path().absolute()) + "\\" + "Test.db"

def createDatabase(replace:bool=False):
    global nameOfDatabase
  
    if replace or not os.path.exists(nameOfDatabase):
        if os.path.exists(nameOfDatabase):
            os.remove(nameOfDatabase)
        createFile()
        testAdding()

def createFile():
    createEventTable(nameOfDatabase)

def testAdding():
    ev = [Event(**{
            'name': 'OneTwoThree',
            'dateStart': datetime.now() + timedelta(days=2,hours=5),
            'dateEnd': datetime.now() + timedelta(days=2,hours=6,minutes=30),
            'description': "Doctor appointment. Very importnant , don't miss it!"}),
          Event(**{
            'name': 'Two',
            'dateStart': datetime.now() + timedelta(days=14,hours=5,minutes=55),
            'dateEnd': datetime.now() + timedelta(days=14,hours=6,minutes=55),
            'description': "Bartek birthday. Important, get a gift!"}),
          Event(**{
            'name': 'Three',
            'dateStart': datetime.now() - timedelta(days=2,hours=5),
            'dateEnd': datetime.now() + timedelta(weeks=117,days=14,hours=3,minutes=15),
            'description': "Final exam, get some crucial knowledge!"})]
    addMultipleEvents(nameOfDatabase, ev)

#    actualDate = datetime.now()

#    listOfEvents = getEvents(nameOfDatabase)
#    addMultipleEvents(nameOfDatabase, ev)
#    print()
#    print("----------")

#    for event in listOfEvents:
#        event.calcTimedeltas(actualDate)
#        print(event)



#    listOfEvents = getEventsAfter(nameOfDatabase, actualDate)

#    print()
#    print("----AFTER-----")

#    for event in listOfEvents:
#        event.calcTimedeltas(actualDate)
#        print(event)

#    listOfEvents = getEventsBefore(nameOfDatabase, actualDate)

#    print()
#    print("----BEFORE-----")

#    for event in listOfEvents:
#        event.calcTimedeltas(actualDate)
#        print(event)

#    #deleteEvent(nameOfDatabase, 3)
#    listOfEvents = getEvents(nameOfDatabase)
#    print()
#    print("----------")

#    for event in listOfEvents:
#        event.calcTimedeltas(actualDate)
#        print(event)


#    deleteAllEvents(nameOfDatabase)
#    listOfEvents = getEvents(nameOfDatabase)
#    print()
#    print("----------")

#    for event in listOfEvents:
#        event.calcTimedeltas(actualDate)
#        print(event)
