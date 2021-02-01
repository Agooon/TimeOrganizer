import Database.FileManagment as fileM 
import Database.Initialization as dbInit
import Database.Classes as dbClass
import Database.Operations as dbOper
from datetime import datetime, timedelta
import os
import calendar
from typing import List

from typing import List
import math


nameOfDatabase = 'Test.db'
msgOfDbNotExist="Database wasn't exist\nNew one has been created\nYou can repeat action"
#                                           #
#                                           #
########## Database operations ##############
#                                           #
#                                           #

def dbExist():
    return os.path.exists(nameOfDatabase)

def createNewDb():
    dbInit.createDatabase(True)



def updateEvent(event: dbClass.Event, eventId:int):
    if(dbExist):
        dbOper.updateEvent(nameOfDatabase, event, eventId)
        return "Event has been changed" , True
    else:
        createNewDb()
        return msgOfDbNotExist, False
#
#   Adding operations
#

def addEventsSingleEvent(event:dbClass.Event) -> [str,bool]:
    if(dbExist):
        dbOper.addEvent(nameOfDatabase, event)
        return "Added new event" , True
    else:
        createNewDb()
        return msgOfDbNotExist, False

def addEventList(eventList:List[dbClass.Event]) -> [str,bool]:
    if(dbExist()):
        dbOper.addMultipleEvents(nameOfDatabase, eventList)
        return "Added new events" , True
    else:
        createNewDb()
        return msgOfDbNotExist, False
#
#   Getting operations
#
def getEvent(eventId:int) ->dbClass.Event:
    try:
        return dbOper.getEvent(nameOfDatabase, eventId)
    except:
        return "Error"

def getEventsFromDay(date: datetime):
    if(dbExist()):
        return dbOper.getEventsFromDay(nameOfDatabase, date)
    else:
        createNewDb()
        return "Error"

def getEvents():
    if(dbExist()):
        return dbOper.getEvents(nameOfDatabase)
    else:
        createNewDb()
        return "Error"

def getEventsBefore(date: datetime):
    if(dbExist()):
        return dbOper.getEventsBefore(nameOfDatabase, date)
    else:
        createNewDb()
        return "Error"

def getEventsAfter(date: datetime):
    if(dbExist()):
        return dbOper.getEventsAfter(nameOfDatabase, date)
    else:
        createNewDb()
        return "Error"
#
#   Deleting operations
#
def deleteEvent(id):
    if(dbExist()):
        return dbOper.deleteEvent(nameOfDatabase, id)
    else:
        createNewDb()
        return "Error"
def deleteEventList(eventList):
    if(dbExist()):
        return dbOper.deleteEventList(nameOfDatabase, eventList)
    else:
        createNewDb()
        return "Error"


def addEventButton(eventNameI, eventDescI,eventDateStartI, eventTimeStartHI, eventTimeEndHI, eventTimeStartMI, eventTimeEndMI,
                   evenTimeEndNextDayCheck, eventRecurrCheck, eventRecurrAmountI, menuRecurrVal) -> [str,bool]:

    if(eventNameI.replace(" ", "") == ""):
        return "Event name can't contain only whitespaces", False
    if(eventDescI.replace(" ", "").replace("\n", "") == ""):
        return "Description can't contain only whitespaces", False
    if(eventTimeStartHI == ""):
        return "You have to put starting hour", False
    if(eventTimeEndHI == ""):
        return "You have to put ending hour", False
    if(eventTimeStartMI == ""):
        return "You have to put starting minute", False
    if(eventTimeEndMI == ""):
        return "You have to put starting minute", False

    startTime = timedelta(hours=int(eventTimeStartHI),minutes=int(eventTimeStartMI))
    endTime = timedelta(hours=int(eventTimeEndHI),minutes=int(eventTimeEndMI))
    if(int(evenTimeEndNextDayCheck) == 1):
        endTime = endTime + timedelta(days=1)
    else:
        if(startTime >= endTime):
            return "StartTime is larger then EndTime", False

    dateStart =  datetime.strptime(eventDateStartI.strftime("%Y-%m-%d %H:%M:%S"),"%Y-%m-%d %H:%M:%S") + startTime
    dateEnd =  datetime.strptime(eventDateStartI.strftime("%Y-%m-%d %H:%M:%S"),"%Y-%m-%d %H:%M:%S") + endTime

    # Single time event
    if(int(eventRecurrCheck) == 0):

        newEvent = dbClass.Event(**{
        'name': eventNameI,
        'dateStart': dateStart,
        'dateEnd': dateEnd,
        'description': eventDescI})
        print(newEvent)
        
        msg,succ=addEventsSingleEvent(newEvent)

        return msg,succ
    else:
        if(eventRecurrAmountI == ""):
            return "Set amount of repeats", False
        if(int(eventRecurrAmountI) == 0):
            return "Amount of repeats can't be 0", False
        # Recurring event
        # "Every day","Every week", "Every month", "Every Year"
        option = menuRecurrVal
        listofEvents =[]
        if(option =="Every day"):
            for i in range(int(eventRecurrAmountI)+1):
                newEvent = dbClass.Event(**{
                'name': eventNameI,
                'dateStart': dateStart + timedelta(days=i),
                'dateEnd': dateEnd+ timedelta(days=i),
                'description': eventDescI})
                listofEvents.append(newEvent)

            for e in listofEvents:
                print(e)
            msg, succ = addEventList(listofEvents)
            return msg, succ
        if(option =="Every week"):
            for i in range(int(eventRecurrAmountI)+1):
                newEvent = dbClass.Event(**{
                'name': eventNameI,
                'dateStart': dateStart + timedelta(weeks=i),
                'dateEnd': dateEnd+ timedelta(weeks=i),
                'description': eventDescI})
                listofEvents.append(newEvent)

            for e in listofEvents:
                print(e)
            msg, succ = addEventList(listofEvents)
            return msg, succ
        if(option =="Every month"):
            dayStart = dateStart.day 
            dayEnd = dateEnd.day 
            currMonth=dateEnd.month
            currYear = dateEnd.year
            for i in range(int(eventRecurrAmountI)+1):

                if(currMonth%13 == 0):
                    currYear+=1
                    currMonth=1
                if(dayEnd <= calendar.monthrange(currYear, currMonth)[1] and dateStart.month == dateEnd.month):
                    # Date end from 1 up to max value of current month, daystart happens in the same month
                    if(currYear == dateEnd.year):
                        dateStart = dateStart.replace(month=currMonth, day = dayStart)
                        dateEnd = dateEnd.replace(month=currMonth,  day = dayEnd)
                    else:
                        dateStart = dateStart.replace(month=currMonth, year=currYear,  day = dayStart)
                        dateEnd = dateEnd.replace(month=currMonth, year=currYear, day = dayEnd)
                else:
                    # Happening on the same day
                    if(dayStart == dayEnd):
                        if(currYear == dateEnd.year):
                            dateStart = dateStart.replace(month=currMonth, day=calendar.monthrange(currYear, currMonth)[1])
                            dateEnd = dateEnd.replace(month=currMonth, day=calendar.monthrange(currYear, currMonth)[1])
                        else:
                            dateStart = dateStart.replace(month=currMonth, year=currYear, day=calendar.monthrange(currYear, currMonth)[1])
                            dateEnd = dateEnd.replace(month=currMonth, year=currYear, day=calendar.monthrange(currYear, currMonth)[1])
                    else:
                        # Last 2 days of month
                        if(dateStart.month == dateEnd.month):
                            if(currYear == dateEnd.year):
                                dateStart = dateStart.replace(month=currMonth, day=calendar.monthrange(currYear, currMonth)[1]-1)
                                dateEnd = dateEnd.replace(month=currMonth, day=calendar.monthrange(currYear, currMonth)[1])
                            else:
                                dateStart = dateStart.replace(month=currMonth, year=currYear, day=calendar.monthrange(currYear, currMonth)[1]-1)
                                dateEnd = dateEnd.replace(month=currMonth, year=currYear, day=calendar.monthrange(currYear, currMonth)[1])
                        else:
                            # Last and first day of 2 months
                            # 31 and 1 december of january
                            # 31 grudnia 2020
                            # 1 styczeń currYear 2021
                            if(dateStart.year != dateEnd.year):
                                if(currMonth == 1):
                                    dateStart = dateStart.replace(month=12, year=currYear-1, day=31)
                                    dateEnd = dateEnd.replace(month=1, year=currYear, day=1)
                                else:
                                    dateStart = dateStart.replace(month=currMonth-1, year=currYear, day=calendar.monthrange(currYear, currMonth-1)[1])
                                    dateEnd = dateEnd.replace(month=currMonth, year=currYear, day=1)
                            else:
                                if(currYear == dateEnd.year):
                                    dateStart = dateStart.replace(month=currMonth-1, day=calendar.monthrange(currYear, currMonth-1)[1])
                                    dateEnd = dateEnd.replace(month=currMonth, day=1)
                                else:
                                    dateStart = dateStart.replace(month=12, year=currYear, day=calendar.monthrange(currYear, 12)[1])
                                    dateEnd = dateEnd.replace(month=currMonth, year=currYear, day=1)
                currMonth+=1
                newEvent = dbClass.Event(**{
                'name': eventNameI,
                'dateStart': dateStart,
                'dateEnd': dateEnd,
                'description': eventDescI})
                listofEvents.append(newEvent)

            for e in listofEvents:
                print(e)
            msg, succ = addEventList(listofEvents)
            return msg, succ
        if(option =="Every Year"):
            daystoAdd=0
            for i in range(int(eventRecurrAmountI)+1):
                addDays = 365
                if(calendar.monthrange(dateStart.year+i, 2)[1] == 29):
                    addDaysS=366
                if(i!=0):   
                    daystoAdd+= addDays
                newEvent = dbClass.Event(**{
                'name': eventNameI,
                'dateStart': dateStart + timedelta(days=daystoAdd),
                'dateEnd': dateEnd+ timedelta(days=daystoAdd),
                'description': eventDescI})
                listofEvents.append(newEvent)

            for e in listofEvents:
                print(e)
            msg, succ = addEventList(listofEvents)
            return msg, succ
#                                           #
#                                           #=
############# NLP operations ################
#                                           #
#                                           #

def filterNLP(eventList : List[dbClass.Event], searchQuery: str, engine):
    return engine.searchWithList(searchQuery[:-1], eventList)


#                                           #
#                                           #
############ FILE operations ################
#                                           #
#                                           #

def addEventsFromFile(nameOfFile:str) -> [str,bool]:
    if(dbExist()):
        return fileM.addEventsFromFile(nameOfDatabase,nameOfFile)
    else:
        createNewDb()
        return msgOfDbNotExist, False

