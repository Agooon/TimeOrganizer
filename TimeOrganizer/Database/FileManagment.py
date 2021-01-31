from Database.Classes import Event
from Database.Operations import addMultipleEvents
from datetime import datetime
import pytz
def addEventsFromFile(nameOfDatabase, fileName: str):
    try:
        addedAll = True
        notAdded = []
        number = 0
        fileExist = False
        filePlan = open(fileName, "r", encoding="utf-8")

        lines = filePlan.readlines()
        fileExist = True
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
                number+=1
                eventList.append(Event(**{
                'name': name,
                'dateStart': datetime(int(dateStart[0:4]),int(dateStart[4:6]),int(dateStart[6:8]),
                                      int(dateStart[9:11]),int(dateStart[11:13]), 
                                      tzinfo=pytz.timezone('UTC')).astimezone(pytz.timezone('Europe/Warsaw')),
                'dateEnd': datetime(int(dateEnd[0:4]),int(dateEnd[4:6]),int(dateEnd[6:8]),
                                      int(dateEnd[9:11]),int(dateEnd[11:13]), 
                                      tzinfo=pytz.timezone('UTC')).astimezone(pytz.timezone('Europe/Warsaw')),
                'description': description }))
                lastEvent = eventList[-1]
                moreThanDay = lastEvent.dateEnd.day - lastEvent.dateStart.day
                if(moreThanDay>1 or lastEvent.dateStart.date()> lastEvent.dateEnd.date()):
                    eventList.pop()
                    notAdded.append(number)
                    addedAll = False
        addMultipleEvents(nameOfDatabase, eventList)
        if(addedAll):
            return "All of events were added ", True
        elif(len(notAdded) > number/2  ):
            return "More than half of events weren't added!\nCheck the format of file", False
        else:
            return "Event numbers that weren't added: " + str(notAdded), False
    except:
        if(not fileExist):
            return "Couldn't open the file", False
        else:
            return "The file format isn't correct!", False


