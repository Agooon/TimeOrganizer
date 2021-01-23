from Database.Classes import Event
from Database.Operations import addMultipleEvents
from datetime import datetime
import pytz
def addEventsFromFile(nameOfDatabase, fileName: str):
    try:
        filePlan = open(fileName, "r")

        lines = filePlan.readlines()

        eventList = []
        # 20201005T053000Z
        for line in lines:
            done = False
            if(line.startswith("DTSTART:")):
                dateStart = line[8:len(line)-1]
            elif(line.startswith("DTEND:")):
                dateEnd = line[6:len(line)-1]
            elif(line.startswith("DESCRIPTION:")):
                description = line[12:len(line)-1]
            elif(line.startswith("SUMMARY:")):
                name = line[8:len(line)-1]
                done = True
            
            if done:
                eventList.append(Event(**{
                'name': name,
                'dateStart': datetime(int(dateStart[0:4]),int(dateStart[4:6]),int(dateStart[6:8]),
                                      int(dateStart[9:11]),int(dateStart[11:13]), 
                                      tzinfo=pytz.timezone('UTC')).astimezone(pytz.timezone('Europe/Warsaw')),
                'dateEnd': datetime(int(dateEnd[0:4]),int(dateEnd[4:6]),int(dateEnd[6:8]),
                                      int(dateEnd[9:11]),int(dateEnd[11:13]), 
                                      tzinfo=pytz.timezone('UTC')).astimezone(pytz.timezone('Europe/Warsaw')),
                'description': description }))
        addMultipleEvents(nameOfDatabase, eventList)
    except e:
        print(e)


