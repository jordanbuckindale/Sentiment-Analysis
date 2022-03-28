"""
Assignment #3
Course: 1026A
Due Date: Nov 17th 2021
Description: This program will look at a file of tweets, and compute a "happiness" score
             for each tweet then compute a happiness score for each time zone then output
             a list for each timezone.

             files:
             - assign3.py
             - sentiment_analysis.py

             - histogram.py
             - graphics.py



Created by: Jordan Buckindale
Student #: 251246279
"""

# import function
from sentiment_analysis import compute_tweets
from histogram import drawSimpleHistogram

# prompt user input
tweets = input("Please enter tweets file: ")
keywords = input("Please keywords file: ")

# get return from function
tupleOutput = compute_tweets(tweets, keywords)

# create lists
happinessScoreInfo = [element[0] for element in tupleOutput]
keywordTweetsInfo = [element[1] for element in tupleOutput]
totalTweetsInfo = [element[2] for element in tupleOutput]

# print output
print("\nEastern Region:\n",
      " " * 15, "Happiness score: ", happinessScoreInfo[0], "\n",
      " " * 15, "Keyword Tweets: ", keywordTweetsInfo[0], "\n",
      " " * 15, "Total tweets in Eastern Region: ", totalTweetsInfo[0])

print("\nCentral Region:\n",
      " " * 15, "Happiness score: ", happinessScoreInfo[1], "\n",
      " " * 15, "Keyword Tweets: ", keywordTweetsInfo[1], "\n",
      " " * 15, "Total tweets in Central Region: ", totalTweetsInfo[1])

print("\nMountain Region:\n",
      " " * 15, "Happiness score: ", happinessScoreInfo[2], "\n",
      " " * 15, "Keyword Tweets: ", keywordTweetsInfo[2], "\n",
      " " * 15, "Total tweets in Central Region: ", totalTweetsInfo[2])

print("\nPacific Region:\n",
      " " * 15, "Happiness score: ", happinessScoreInfo[3], "\n",
      " " * 15, "Keyword Tweets: ", keywordTweetsInfo[3], "\n",
      " " * 15, "Total tweets in Central Region: ", totalTweetsInfo[3])

drawSimpleHistogram(happinessScoreInfo[0], happinessScoreInfo[1], happinessScoreInfo[2], happinessScoreInfo[3])
