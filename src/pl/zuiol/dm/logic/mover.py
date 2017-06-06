"""
This File might contain functions maybe classes that should support determining what 
should be don e with particular file handled by application

The main goal is to determine destination folder of managed file
"""

def moveHandledFile(sourceFilePath, key_words):
    print("In moveHandledFile method")
    print(key_words)
    words = key_words.split(" ")
    #destinationFilePath = None
    #for word in words:
        