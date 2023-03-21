from tabulate import tabulate

while(1):

    unit = ""
       
    def Prompt():
        global hunters
        global success
        global golhunters
        global golsuccess
        golhuntersinput = input("Are you wanting to know # of hunters > or < that a certain # (G or L) ")
        golhunters = golhuntersinput.upper()
        huntersinput = input("Enter # of hunters: ")
        hunters = huntersinput
        golsuccessinput = input("Are you wanting to know success rate that is > or < than a certain rate (G or L) ")
        golsuccess = golsuccessinput.upper()
        success = input("Enter success rate: ")
        
    def BearControlled():
        unitData = open("2020BearControlled.txt", "r")
        removeHeader = unitData.readline()
        nextLine = unitData.readline()
        headersBearControlled = ["Hunt#", "TakeMethod", "Area", "Hunters", "Harvest", "Success%", "Days", "Boars", "Sows", "Fall", "Spring", "Bait"]
        while nextLine != "":
            splitline = nextLine.split()
            #print(splitline)
            if golhunters == "L" and golsuccess == "G":
                if int(splitline[3]) < int(hunters) and float(splitline[5]) > float(success):
                       bestUnits.append(splitline)
            if golhunters == "L" and golsuccess == "L":
                if int(splitline[3]) < int(hunters) and float(splitline[5]) < float(success):
                       bestUnits.append(splitline)
            if golhunters == "G" and golsuccess == "L":
                if int(splitline[3]) > int(hunters) and float(splitline[5]) < float(success):
                       bestUnits.append(splitline)
            if golhunters == "G" and golsuccess == "G":
                if int(splitline[3]) > int(hunters) and float(splitline[5]) > float(success):
                       bestUnits.append(splitline)
            nextLine = unitData.readline()
        print(tabulate(bestUnits,headers=headersBearControlled))
        print("Showing results for ", golhunters, "than ", hunters, "hunters", '\n' +
              "With a success rate ", golsuccess, "than ", success + "%")


    ##def BearGeneral():
    ##    unitData = open("2020BearGeneral.txt", "r")
    ##    removeHeader = unitData.readline()
    ##    nextLine = unitData.readline()
    ##    headersBearGeneral = ["Unit", "Harvest", "Boars", "Sows", "Fall", "Spring", "Bait", "Hounds" ,"Incidental","Still Stalk"]
    ##    while nextLine != "":
    ##        splitline = nextLine.split()
    ##        #print(splitline)
    ##        try:
    ##            if golhunters == "L" and golsuccess == "G":
    ##                if int(splitline[3]) < int(hunters) and float(splitline[5]) > float(success):
    ##                       bestUnits.append(splitline)
    ##            if golhunters == "L" and golsuccess == "L":
    ##                if int(splitline[3]) < int(hunters) and float(splitline[5]) < float(success):
    ##                       bestUnits.append(splitline)
    ##            if golhunters == "G" and golsuccess == "L":
    ##                if int(splitline[3]) > int(hunters) and float(splitline[5]) < float(success):
    ##                       bestUnits.append(splitline)
    ##            if golhunters == "G" and golsuccess == "G":
    ##                if int(splitline[3]) > int(hunters) and float(splitline[5]) > float(success):
    ##                       bestUnits.append(splitline)
    ##        except IndexError:
    ##            pass
    ##        nextLine = unitData.readline()
    ##    print(tabulate(bestUnits,headers=headersBearGeneral))
    ##    print("Showing results for ", golhunters, "than ", hunters, "hunters", '\n' +
    ##          "With a success rate ", golsuccess, "than ", success + "%")


    def CaliforniaSheepControlled():
        unitData = open("2021CaliforniaSheepControlled.txt", "r")
        removeHeader = unitData.readline()
        nextLine = unitData.readline()
        headersCaliforniaSheepControlled = ["Hunt#", "TakeMethod", "Area", "Hunters", "Harvest", "Success%",
                                            "Days", "Rams", "Ewes","Avg. Horn Length (in.)","Avg. Horn Circum. (in.)"]
        while nextLine != "":
            splitline = nextLine.split()
            #print(splitline)
            if golhunters == "L" and golsuccess == "G":
                if int(splitline[3]) < int(hunters) and float(splitline[5]) > float(success):
                       bestUnits.append(splitline)
            if golhunters == "L" and golsuccess == "L":
                if int(splitline[3]) < int(hunters) and float(splitline[5]) < float(success):
                       bestUnits.append(splitline)
            if golhunters == "G" and golsuccess == "L":
                if int(splitline[3]) > int(hunters) and float(splitline[5]) < float(success):
                       bestUnits.append(splitline)
            if golhunters == "G" and golsuccess == "G":
                if int(splitline[3]) > int(hunters) and float(splitline[5]) > float(success):
                       bestUnits.append(splitline)
            nextLine = unitData.readline()
        print(tabulate(bestUnits,headers=headersCaliforniaSheepControlled))
        print("Showing results for ", golhunters, "than ", hunters, "hunters", '\n' +
              "With a success rate ", golsuccess, "than ", success + "%")


    def DeerGeneral():
        unitData = open("2021DeerAnyGeneral.txt", "r")
        removeHeader = unitData.readline()
        nextLine = unitData.readline()
        headersDeer = ["Take Method","Unit", "Harvest", "Hunters","Success%", "Days", "Antlered", "Antlerless" ,"%4+Pts", "%5+Pts", "%Whitetail"]
        while nextLine != "":
            splitline = nextLine.split()
            #print(splitline)
            if golhunters == "L" and golsuccess == "G":
                if int(splitline[3]) < int(hunters) and float(splitline[4]) > float(success):
                       bestUnits.append(splitline)
            if golhunters == "L" and golsuccess == "L":
                if int(splitline[3]) < int(hunters) and float(splitline[4]) < float(success):
                       bestUnits.append(splitline)
            if golhunters == "G" and golsuccess == "L":
                if int(splitline[3]) > int(hunters) and float(splitline[4]) < float(success):
                       bestUnits.append(splitline)
            if golhunters == "G" and golsuccess == "G":
                if int(splitline[3]) > int(hunters) and float(splitline[4]) > float(success):
                       bestUnits.append(splitline)
            nextLine = unitData.readline()
        print(tabulate(bestUnits,headers=headersDeer))
        print("Showing results for ", golhunters, "than ", hunters, "hunters", '\n' +
              "With a success rate ", golsuccess, "than ", success + "%")

    def DeerGeneralUnitSearch():
        unitData = open("2021DeerAnyGeneral.txt", "r")
        removeHeader = unitData.readline()
        nextLine = unitData.readline()
        headersDeer = ["Take Method","Unit", "Harvest", "Hunters","Success%", "Days", "Antlered", "Antlerless" ,"%4+Pts", "%5+Pts", "%Whitetail"]
        while nextLine != "":
            splitline = nextLine.split()
            #print(splitline)
            if splitline[1] == str(unit):
                bestUnits.append(splitline)
            nextLine = unitData.readline()
        print(tabulate(bestUnits,headers=headersDeer))
        print("Showing Unit", unit)

    def DeerControlled():
        unitData = open("2021DeerControlled.txt", "r")
        removeHeader = unitData.readline()
        nextLine = unitData.readline()
        controlledUnitsSkipped = 0
        headersDeerControlled = ["Hunt#", "TakeMethod" ,"Area" ,"Hunters", "Harvest" , "Success%", "Days","Antlered" , "Antlerless" , "%4+Pts", "%5+Pts" , "%Whitetail"]
        while nextLine != "":
            splitline = nextLine.split()
            #print(splitline)
            try:
                if splitline[1] == "AnyWeapon":
                    if golhunters == "L" and golsuccess == "G":
                        if int(splitline[3]) < int(hunters) and float(splitline[5]) > float(success):
                               bestUnits.append(splitline)
                    if golhunters == "L" and golsuccess == "L":
                        if int(splitline[3]) < int(hunters) and float(splitline[5]) < float(success):
                               bestUnits.append(splitline)
                    if golhunters == "G" and golsuccess == "L":
                        if int(splitline[3]) > int(hunters) and float(splitline[5]) < float(success):
                               bestUnits.append(splitline)
                    if golhunters == "G" and golsuccess == "G":
                        if int(splitline[3]) > int(hunters) and float(splitline[5]) > float(success):
                               bestUnits.append(splitline)
            except IndexError:
                controlledUnitsSkipped = controlledUnitsSkipped + 1
                pass
            nextLine = unitData.readline()
        print(tabulate(bestUnits,headers=headersDeerControlled))
        print("Showing results for ", golhunters, "than ", hunters, "hunters", '\n' +
              "With a success rate ", golsuccess, "than ", success + "%")
        print("Units not displayed due to lack of data: ", controlledUnitsSkipped)

    def DeerControlledUnitSearch():
        unitData = open("2021DeerControlled.txt", "r")
        removeHeader = unitData.readline()
        nextLine = unitData.readline()
        headersDeerControlled = ["Hunt#", "TakeMethod" ,"Area" ,"Hunters", "Harvest" , "Success%", "Days","Antlered" , "Antlerless" , "%4+Pts", "%5+Pts" , "%Whitetail"]
        while nextLine != "":
            splitline = nextLine.split()
            #print(splitline)
            if splitline[0] == str(unit) or splitline[2] == str(unit):
                bestUnits.append(splitline)
            nextLine = unitData.readline()
        print(tabulate(bestUnits,headers=headersDeerControlled))
        print("Showing Unit/hunt number", unit)

    def ElkControlled():
        unitData = open("2021ElkControlled.txt", "r")
        removeHeader = unitData.readline()
        nextLine = unitData.readline()
        headersElkControlled = ["Hunt#","TakeMethod","Area","Hunters","Harvest","Success%","Days","Antlered","Antlerless","%Spike","%6+Pts"]
        while nextLine != "":
            splitline = nextLine.split()
            #print(splitline)
            if splitline[1] == "AnyWeapon":
                if golhunters == "L" and golsuccess == "G":
                    if int(splitline[3]) < int(hunters) and float(splitline[5]) > float(success):
                           bestUnits.append(splitline)
                if golhunters == "L" and golsuccess == "L":
                    if int(splitline[3]) < int(hunters) and float(splitline[5]) < float(success):
                           bestUnits.append(splitline)
                if golhunters == "G" and golsuccess == "L":
                    if int(splitline[3]) > int(hunters) and float(splitline[5]) < float(success):
                           bestUnits.append(splitline)
                if golhunters == "G" and golsuccess == "G":
                    if int(splitline[3]) > int(hunters) and float(splitline[5]) > float(success):
                           bestUnits.append(splitline)
          
            nextLine = unitData.readline()
        print(tabulate(bestUnits,headers=headersElkControlled))
        print("Showing results for ", golhunters, "than ", hunters, "hunters", '\n' +
              "With a success rate ", golsuccess, "than ", success + "%")

        
    def ElkGeneral():
        unitData = open("2021ElkAnyGeneral.txt", "r")
        removeHeader = unitData.readline()
        nextLine = unitData.readline()
        headersElk = ["Take Method","Unit","Harvest","Hunters","Success%","Days","Antlered","Antlerless","%Spike","%6+Pts"]
        while nextLine != "":
            splitline = nextLine.split()
            #print(splitline)
            if golhunters == "L" and golsuccess == "G":
                if int(splitline[3]) < int(hunters) and float(splitline[4]) > float(success):
                       bestUnits.append(splitline)
            if golhunters == "L" and golsuccess == "L":
                if int(splitline[3]) < int(hunters) and float(splitline[4]) < float(success):
                       bestUnits.append(splitline)
            if golhunters == "G" and golsuccess == "L":
                if int(splitline[3]) > int(hunters) and float(splitline[4]) < float(success):
                       bestUnits.append(splitline)
            if golhunters == "G" and golsuccess == "G":
                if int(splitline[3]) > int(hunters) and float(splitline[4]) > float(success):
                       bestUnits.append(splitline)
            nextLine = unitData.readline()
        print(tabulate(bestUnits,headers=headersElk))
        print("Showing results for ", golhunters, "than ", hunters, "hunters", '\n' +
              "With a success rate ", golsuccess, "than ", success + "%")

    def GoatControlled():
        unitData = open("2021GoatControlled.txt", "r")
        removeHeader = unitData.readline()
        nextLine = unitData.readline()
        headersGoat = ["Hunt#","TakeMethod","Area","Hunters","Harvest","Success%","Days",
                       "Billies","Nannies","Avg. Horn Length (in.)","Avg. Horn Circum. (in.)"]
        while nextLine != "":
            splitline = nextLine.split()
            #print(splitline)
            if golhunters == "L" and golsuccess == "G":
                if int(splitline[3]) < int(hunters) and float(splitline[5]) > float(success):
                       bestUnits.append(splitline)
            if golhunters == "L" and golsuccess == "L":
                if int(splitline[3]) < int(hunters) and float(splitline[5]) < float(success):
                       bestUnits.append(splitline)
            if golhunters == "G" and golsuccess == "L":
                if int(splitline[3]) > int(hunters) and float(splitline[5]) < float(success):
                       bestUnits.append(splitline)
            if golhunters == "G" and golsuccess == "G":
                if int(splitline[3]) > int(hunters) and float(splitline[5]) > float(success):
                       bestUnits.append(splitline)
            nextLine = unitData.readline()
        print(tabulate(bestUnits,headers=headersGoat))
        print("Showing results for ", golhunters, "than ", hunters, "hunters", '\n' +
              "With a success rate ", golsuccess, "than ", success + "%")
        

    def MooseControlled():
        skipped = 0
        unitData = open("2021MooseControlled.txt", "r")
        removeHeader = unitData.readline()
        nextLine = unitData.readline()
        headersMooseControlled = ["Hunt#","TakeMethod","Area","Hunters","Harvest","Success%","Days","Bulls","Cows","Avg. Antler Spread (in.)"]
        while nextLine != "":
            splitline = nextLine.split()
            #print(splitline)
            try:
                if splitline[1] == "AnyWeapon":
                    if golhunters == "L" and golsuccess == "G":
                        if int(splitline[3]) < int(hunters) and float(splitline[5]) > float(success):
                               bestUnits.append(splitline)
                    if golhunters == "L" and golsuccess == "L":
                        if int(splitline[3]) < int(hunters) and float(splitline[5]) < float(success):
                               bestUnits.append(splitline)
                    if golhunters == "G" and golsuccess == "L":
                        if int(splitline[3]) > int(hunters) and float(splitline[5]) < float(success):
                               bestUnits.append(splitline)
                    if golhunters == "G" and golsuccess == "G":
                        if int(splitline[3]) > int(hunters) and float(splitline[5]) > float(success):
                               bestUnits.append(splitline)
            except IndexError:
                skipped = skipped + 1
                pass
            nextLine = unitData.readline()
        print(tabulate(bestUnits,headers=headersMooseControlled))
        print("Showing results for ", golhunters, "than ", hunters, "hunters", '\n' +
              "With a success rate ", golsuccess, "than ", success + "%")
        if skipped > 1:
            print("Units skipped due to missing data:", skipped)

    def PronghornControlled():
        unitData = open("2021PronghornControlled.txt", "r")
        removeHeader = unitData.readline()
        nextLine = unitData.readline()
        headersPronghornControlled = ["Hunt#","TakeMethod","Area","Hunters","Harvest","Success%","Days","Horned","Hornless","Avg. Horn Length (in.)"]
        while nextLine != "":
            splitline = nextLine.split()
            #print(splitline)
            if splitline[1] == "AnyWeapon":
                if golhunters == "L" and golsuccess == "G":
                    if int(splitline[3]) < int(hunters) and float(splitline[5]) > float(success):
                           bestUnits.append(splitline)
                if golhunters == "L" and golsuccess == "L":
                    if int(splitline[3]) < int(hunters) and float(splitline[5]) < float(success):
                           bestUnits.append(splitline)
                if golhunters == "G" and golsuccess == "L":
                    if int(splitline[3]) > int(hunters) and float(splitline[5]) < float(success):
                           bestUnits.append(splitline)
                if golhunters == "G" and golsuccess == "G":
                    if int(splitline[3]) > int(hunters) and float(splitline[5]) > float(success):
                           bestUnits.append(splitline)
          
            nextLine = unitData.readline()
        print(tabulate(bestUnits,headers=headersPronghornControlled))
        print("Showing results for ", golhunters, "than ", hunters, "hunters", '\n' +
              "With a success rate ", golsuccess, "than ", success + "%")

    def RockyMtnSheepControlled():
        unitData = open("2021RockyMtnSheepControlled.txt", "r")
        removeHeader = unitData.readline()
        nextLine = unitData.readline()
        headersRockyMtnSheepControlled = ["Hunt#","TakeMethod","Area","Hunters","Harvest","Success%","Days","Rams","Ewes",
                                          "Avg. Horn Length (in.)","Avg. Horn Circum. (in.)"]
        while nextLine != "":
            splitline = nextLine.split()
            #print(splitline)
            if splitline[1] == "AnyWeapon" or splitline[1] == "AnyWeapon_Lottery_Tag" or splitline[1] == "AnyWeapon_Auction_Tag":
                if golhunters == "L" and golsuccess == "G":
                    if int(splitline[3]) < int(hunters) and float(splitline[5]) > float(success):
                           bestUnits.append(splitline)
                if golhunters == "L" and golsuccess == "L":
                    if int(splitline[3]) < int(hunters) and float(splitline[5]) < float(success):
                           bestUnits.append(splitline)
                if golhunters == "G" and golsuccess == "L":
                    if int(splitline[3]) > int(hunters) and float(splitline[5]) < float(success):
                           bestUnits.append(splitline)
                if golhunters == "G" and golsuccess == "G":
                    if int(splitline[3]) > int(hunters) and float(splitline[5]) > float(success):
                           bestUnits.append(splitline)
          
            nextLine = unitData.readline()
        print(tabulate(bestUnits,headers=headersRockyMtnSheepControlled))
        print("Showing results for ", golhunters, "than ", hunters, "hunters", '\n' +
              "With a success rate ", golsuccess, "than ", success + "%")
        
    bestUnits = []


    animalList = ['California Sheep Controlled', 'Deer Controlled', 'Deer General',
                  'Elk Controlled', 'Elk General','Goat Controlled', 'Moose Controlled', 'Pronghorn Controlled', 'Rocky Mtn Sheep Controlled']

    animalPrompt = input('Enter animal: (To view list of animals enter "view list"), (to look for specific unit/hunt# enter "search") ')

    if animalPrompt.lower() == "view list":
        print(*animalList, sep='\n')
        animalPrompt = input('Enter animal: (To view list of animals enter "view list"), (to look for specific unit/hunt# enter "search") ')

    if animalPrompt.lower() == "search":
        print(*animalList, sep='\n',)
        unitanimalPrompt = input("What animal are you hunting? ")
        if unitanimalPrompt.lower() == "deer general":
            unitPrompt = input("Enter unit: ")
            unit = unitPrompt
            DeerGeneralUnitSearch()
        if unitanimalPrompt.lower() == "deer controlled":
            unitPrompt = input("Enter unit or hunt number: ")
            unit = unitPrompt
            DeerControlledUnitSearch()
            
            

    if animalPrompt.lower() == "deer general":
        Prompt()
        DeerGeneral()

    if animalPrompt.lower() == "deer controlled":
        Prompt()
        DeerControlled()

##    if animalPrompt.lower() == "bear controlled":
##        Prompt()
##        BearControlled()

    if animalPrompt.lower() == "bear general":
        Prompt()
        BearGeneral()

    if animalPrompt.lower() == "california sheep controlled":
        Prompt()
        CaliforniaSheepControlled()

    if animalPrompt.lower() == "elk controlled":
        Prompt()
        ElkControlled()

    if animalPrompt.lower() == "elk general":
        Prompt()
        ElkGeneral()

    if animalPrompt.lower() == "goat controlled":
        Prompt()
        GoatControlled()

    if animalPrompt.lower() == "moose controlled":
        Prompt()
        MooseControlled()

    if animalPrompt.lower() == "pronghorn controlled":
        Prompt()
        PronghornControlled()

    if animalPrompt.lower() == "rocky mtn sheep controlled":
        Prompt()
        RockyMtnSheepControlled()
    
