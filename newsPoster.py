import requests
import random

url = ('http://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=') # Key removed to maintain private access of account
response = requests.get(url)

#print(type(response.json()))
#print (response.json())

# Fields for the response.json()
totalresults = (response.json().get('totalResults'))
status = (response.json().get('status'))
articleList = (response.json().get('articles'))

info = ""
title = ""
url = ""
description = ""
content = ""

def updateArticle():
    global info
    global title
    global url
    global description
    global content
    
    # Creates a random number int to select random headline
    num = random.randint(0, totalresults/2)
    count = 0

    # Iterates through each key-value pair in articleList of stories
    for item in articleList:
        if(count == num):
            if 'title' in item:
                if (item.get('source').get('name')== "Dailymail.co.uk"
                    or item.get('source').get('name')=="Youtube.com"
                    or item.get('source').get('name')=="TechRadar"):
                    updateArticle()
                    break
                info = item
                title = item.get('title')
                url = item.get('url')
                description = item.get('description')
                content = item.get('content')
                break
        count=count+1
    checkCopyright(content)

def checkCopyright(content):
    try:
        if(('Copyright' in content) or ('copyright' in content)):
            updateArticle()
    except:
        return

# Returns all the info on an article
def getInfo():
    return info

# Returns all the title of an article
def getTitle():
    return title
    
# Returns all the url of an article
def getUrl():
    return url

# Returns the description of an article
def getDescription():
    return description

# Returns content to be used in makeTweet()
def getContent():
    try:
        mystr = content[:199]
        count = len(mystr)
        for character in reversed(mystr):
            count = count-1
            if(character == '.'):
                print("period")
                mystr = mystr[:count+1]
                break
            if(character == ','):
                print("comma")
                mystr = mystr[:count] + "..."
                break

    # If the article content does not exist, gets the article description instead
    except:
        #print("exception in getContent()")
        mystr = getDescription()
    return mystr

# Creates the final tweet to be posted
def makeTweet():
    # Tries to make the tweet
    try:
        return getContent() + "\n" + getUrl()
    # If the attempt to make the tweet fails, resets the fields and remakes the tweet
    except:
        updateArticle()
        makeTweet()

#if __name__ == "__main__":
updateArticle()

# Testing
#print(makeTweet())
