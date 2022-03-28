"""
Assignment #3
Course: 1026A
Due Date: Nov 17th 2021
Description: This program will look at a file of tweets, and compute a "happiness" score
             for each tweet then compute a happiness score for each time zone then output
             a list for each timezone. The objective is to determine which timezone is
             the “happiest”.

Created by: Jordan Buckindale
Student #: 251246279
"""


def compute_tweets(tweets, keywords):

    # variables
    easternTweetsTotal = 0
    pacificTweetsTotal = 0
    mountainTweetsTotal = 0
    centralTweetsTotal = 0

    easternKeyTweetsTotal = 0
    pacificKeyTweetsTotal = 0
    mountainKeyTweetsTotal = 0
    centralKeyTweetsTotal = 0

    easternScore = 0
    pacificScore = 0
    mountainScore = 0
    centralScore = 0

    emptyTupleList = [(0, 0, 0,), (0, 0, 0,), (0, 0, 0,), (0, 0, 0,)]
    keywordDictionary = {}

    try:
        # open files
        tweetsFile = open(tweets, "r", encoding='utf-8')
        keywordsFile = open(keywords, "r", encoding='utf-8')

        # create dictionary for keywords
        for line in keywordsFile:
            keywordDictionary.update(processKeywordDictionary(line))

        # create list for keywords
        keywordList = keywordDictionary.keys()

        # ignore empty lines
        for line in tweetsFile:
            if line == "" or line == "\n":
                continue

            # create list with tweet
            tweetList = processTweetList(line)

            # find coordinates for longitude
            longitude = longitudeCoordinate(line)
            # find coordinates for latitude
            latitude = latitudeCoordinate(line)

            # find region
            region = (findRegion(longitude, latitude))

            # calculate total tweets, total key tweets  and score of region
            if region == "Eastern":
                easternTweetsTotal += 1
                if calculateScore(tweetList, keywordList, keywordDictionary) != 0:
                    easternKeyTweetsTotal += 1
                    easternScore += calculateScore(tweetList, keywordList, keywordDictionary)

            elif region == "Central":
                centralTweetsTotal += 1
                if calculateScore(tweetList, keywordList, keywordDictionary) != 0:
                    centralKeyTweetsTotal += 1
                    centralScore += calculateScore(tweetList, keywordList, keywordDictionary)

            elif region == "Mountain":
                mountainTweetsTotal += 1
                if calculateScore(tweetList, keywordList, keywordDictionary) != 0:
                    mountainKeyTweetsTotal += 1
                    mountainScore += calculateScore(tweetList, keywordList, keywordDictionary)

            elif region == "Pacific":
                pacificTweetsTotal += 1
                if calculateScore(tweetList, keywordList, keywordDictionary) != 0:
                    pacificKeyTweetsTotal += 1
                    pacificScore += calculateScore(tweetList, keywordList, keywordDictionary)

        # calculates happiness of each region
        if easternKeyTweetsTotal != 0:
            easternScore = easternScore / easternTweetsTotal
        if centralKeyTweetsTotal != 0:
            centralScore = centralScore / centralTweetsTotal
        if mountainKeyTweetsTotal != 0:
            mountainScore = mountainScore / mountainTweetsTotal
        if pacificKeyTweetsTotal != 0:
            pacificScore = pacificScore / pacificTweetsTotal

        # create new list of tuples
        tupleList = [(easternScore, easternKeyTweetsTotal, easternTweetsTotal),
                     (centralScore, centralKeyTweetsTotal, centralTweetsTotal),
                     (mountainScore, mountainKeyTweetsTotal, mountainTweetsTotal),
                     (pacificScore, pacificKeyTweetsTotal, pacificTweetsTotal)]

        # close files
        tweetsFile.close()
        keywordsFile.close()

        return tupleList

    # except errors and return empty list
    except IOError:
        print("Error: file not found.")
        return emptyTupleList
    except IndexError:
        print("Error: Invalid file or format.")
        return emptyTupleList


def processKeywordDictionary(line):  # FUNCTION TO ADD KEYWORDS TO DICTIONARY
    keywordSet = {}  # create new dictionary
    keywordline = line.rstrip().split(",")  # turns line into list split by comma
    keywordSet[keywordline[0]] = keywordline[1]  # adds keyword to dictionary with value
    return keywordSet  # returns keyword to dictionary


def processTweetList(line):  # FUNCTION TO REMOVE TWEET OF SPECIAL CHARACTERS AND INTEGERS
    tempList = line.lower().rstrip().split(" ")
    tweetList = []
    for word in tempList:
        word = processString(word)
        numberCheck = any(chr.isdigit() for chr in word)  # check to see if number in word
        if numberCheck is False:
            tweetList.append(word)
    return tweetList


def processString(word):  # FUNCTION TO REMOVE SPECIAL CHARACTERS
    for character in word:
        specialCharacters = "!@#$%^&*()_:/.?;"
        if character in specialCharacters:
            word = word.replace(character, "")
    return word


def findRegion(longitude, latitude):  # FUNCTION TO DETERMINE LOCATION
    # define variable
    region = ""
    # find the region of tweet
    if (24.660845 <= latitude <= 49.189787) and (-125.242264 <= longitude <= -67.4446574):
        if (24.660845 <= latitude <= 49.189787) and (-87.518395 <= longitude <= -67.4446574):
            region = "Eastern"
        elif (24.660845 <= latitude <= 49.189787) and (-101.998892 <= longitude <= -87.518395):
            region = "Central"
        elif (24.660845 <= latitude <= 49.189787) and (-115.236428 <= longitude <= -101.998892):
            region = "Mountain"
        elif (24.660845 <= latitude <= 49.189787) and (-125.242264 <= longitude <= -115.236428):
            region = "Pacific"
    return region


def calculateScore(tweetList, keywordList, keywordDictionary):  # FUNCTION TO CALCULATE SCORE
    # define variables
    score = 0

    for word in tweetList:
        if word in keywordList:
            score += float(keywordDictionary[word])
    if score != 0:
        return score
    else:
        return score


def latitudeCoordinate(line):  # FUNCTION TO DETERMINE LATITUDE
    tempList = line.lower().rstrip().split(" ")
    latVal1 = tempList[0].rstrip(',')
    latVal2 = latVal1.lstrip('[')  # grab longitude from list
    latitude = float(latVal2)
    return latitude


def longitudeCoordinate(line):  # FUNCTION TO DETERMINE LONGITUDE
    tempList = line.lower().rstrip().split(" ")
    longVal = tempList[1].rstrip(']')  # grab latitude from list
    longitude = float(longVal)
    return longitude
