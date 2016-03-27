def wash(dateList):
    dateList =  map(lambda x : x.split(), dateList)
    cleanList = []
    for each in dateList:
        if each:
            cleanList.append(each[0])
    return cleanList
