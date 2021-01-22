from Database.Classes import Event
import sqlite3
from datetime import datetime
from datetime import timedelta
from typing import List

#                       #
#  Creating Operations  #
#                       #

# Create Table EventTable
def createEventTable(nameOfDatabase: str):

    connection = sqlite3.connect(nameOfDatabase)
    cursor = connection.cursor()

    cursor.execute(''' CREATE TABLE EventTable (
         Id INTEGER PRIMARY KEY,
         Name text,
         DateStart date,
         DateEnd date,
         Description text
        )''')
    connection.commit()

#                       #
#   Adding Operations   #
#                       #

# Add Single Event
def addEvent(nameOfDatabase: str, event:Event):

    connection = sqlite3.connect(nameOfDatabase)
    cursor = connection.cursor()

    cursor.execute('''INSERT INTO EventTable(Name, DateStart, DateEnd, Description) 
                VALUES (?,?,?,?)''',
                (event.name, event.dateStart, event.dateEnd, event.description))

    connection.commit()
    connection.close()

# Add Event list
def addMultipleEvents(nameOfDatabase: str, events: List[Event]):

    connection = sqlite3.connect(nameOfDatabase)
    cursor = connection.cursor()

    for event in events:
        cursor.execute('''INSERT INTO EventTable(Name, DateStart, DateEnd, Description) 
                VALUES (?,?,?,?)''',
                (event.name, event.dateStart, event.dateEnd, event.description))

    connection.commit()
    connection.close()

#                       #
#  Getting Operations   #
#                       #

# Get Single Event
def getEvent(nameOfDatabase: str, eventId:Event) -> Event:

    connection = sqlite3.connect(nameOfDatabase)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM EventTable WHERE Id = '%s'" % eventId)

    call = cursor.fetchone()

    connection.close()

    if call is None:
        return Event(**{'name':"FAILED"})

    return Event(**{
            'id': call[0],
            'name': call[1],
            'dateStart': call[2],
            'dateEnd': call[3],
            'description': call[4]})

# Get all events
def getEvents(nameOfDatabase: str) -> List[Event]:

    connection = sqlite3.connect(nameOfDatabase)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM EventTable")

    listOfEvents = []

    for eventCall in cursor.fetchall():
        listOfEvents.append(Event(**{
            'id': eventCall[0],
            'name': eventCall[1],
            'dateStart': eventCall[2],
            'dateEnd': eventCall[3],
            'description': eventCall[4]}))


    connection.close()

    return listOfEvents

# Get all events after certain date
def getEventsAfter(nameOfDatabase: str, afterDate: datetime) -> List[Event]:

    connection = sqlite3.connect(nameOfDatabase)
    cursor = connection.cursor()

    cursor.execute(
        '''SELECT * FROM EventTable WHERE strftime('%s', DateStart) > strftime('%s','{}')'''.format(
            afterDate.strftime("%Y-%m-%d %H:%M:%S")))

    listOfEvents = []

    for eventCall in cursor.fetchall():
        listOfEvents.append(Event(**{
            'id': eventCall[0],
            'name': eventCall[1],
            'dateStart': eventCall[2],
            'dateEnd': eventCall[3],
            'description': eventCall[4]}))

    connection.close()

    return listOfEvents

# Get all events before certain date
def getEventsBefore(nameOfDatabase: str, beforeDate: datetime) -> List[Event]:

    connection = sqlite3.connect(nameOfDatabase)
    cursor = connection.cursor()
    cursor.execute(
        '''SELECT * FROM EventTable WHERE strftime('%s', DateStart) < strftime('%s', '{}')'''.format(
            beforeDate.strftime("%Y-%m-%d %H:%M:%S")))

    listOfEvents = []

    for eventCall in cursor.fetchall():
        listOfEvents.append(Event(**{
            'id': eventCall[0],
            'name': eventCall[1],
            'dateStart': eventCall[2],
            'dateEnd': eventCall[3],
            'description': eventCall[4]}))

    connection.close()

    return listOfEvents


#                       #
#  Deleting Operations  #
#                       #

# Delete single Event
def deleteEvent(nameOfDatabase: str, eventId: int):

    connection = sqlite3.connect(nameOfDatabase)
    cursor = connection.cursor()

    cursor.execute("DELETE FROM EventTable WHERE Id = '%s'" % eventId)

    connection.commit()
    connection.close()

# Delete all events
def deleteAllEvents(nameOfDatabase: str):

    connection = sqlite3.connect(nameOfDatabase)
    cursor = connection.cursor()

    cursor.execute("DELETE FROM EventTable")

    connection.commit()
    connection.close()

# Delete all events after date
def deleteAllEventsAfter(nameOfDatabase: str, afterDate: datetime):

    connection = sqlite3.connect(nameOfDatabase)
    cursor = connection.cursor()

    cursor.execute('''DELETE FROM EventTable WHERE strftime('%s', DateStart) > strftime('%s', '{}')'''.format(
            afterDate.strftime("%Y-%m-%d %H:%M:%S")))

    connection.commit()
    connection.close()

# Delete all events after date
def deleteAllEventsBefore(nameOfDatabase: str, beforeDate: datetime):

    connection = sqlite3.connect(nameOfDatabase)
    cursor = connection.cursor()

    cursor.execute('''DELETE FROM EventTable WHERE strftime('%s', DateStart) < strftime('%s', '{}')'''.format(
            beforeDate.strftime("%Y-%m-%d %H:%M:%S")))

    connection.commit()
    connection.close()