"""
This File might contain functions maybe classes that should support determining what 
should be don e with particular file handled by application

The main goal is to determine destination folder of managed file
"""
from pl.zuiol.dm.file.operations import moveFile, getSubDirs
from configparser import SafeConfigParser

config = SafeConfigParser()
config.read("..\\..\\..\\..\\properties\\settings.ini")
destination = config['defaults']['destination']


def moveHandledFile(sourceFilePath, key_words):
    print("In moveHandledFile method")
    print(key_words)
    fileName = ""
    names = sourceFilePath.split("\\")
    for name in names:
        if "." in name:
            fileName = name
    
    destinationFilePath = determineDestinationDirectory(key_words) + "\\" + fileName #"C:\\Users\\sg0212049\\Downloads\\DownloadManager\\"    
    
    moveFile(sourceFilePath, destinationFilePath)
    
    
""" Function that returns final destination directory where file should be moved """ 
def determineDestinationDirectory(key_words):
    print("In determineDestinationDirectory method")
    #destinationDirectory = "C:\\Users\\sg0212049\\Downloads\\DownloadManager\\" #TODO this need to be configurable or global somehow.
    print(destination)
    destinationDirectory = destination #TODO this need to be configurable or global somehow.
    
    # for each word that has been entered by user we need to find the best path
    words = key_words.split(" ")
    for word in words:
        print("word:" + word)
        nextDirectory = findNextDirectory(destinationDirectory, word)
        destinationDirectory = nextDirectory
        #destinationDirectory = destinationDirectory.__add__(word + "\\")
    
    print("destination: " + destinationDirectory)

    return destinationDirectory
    
    
def findNextDirectory(destinationDirectory, word):
    foundDirs = getSubDirs(destinationDirectory, word)

    print("Back in findNextDirectory")
    for p in foundDirs:
        print(p)
        
    winner = (min(foundDirs, key = lambda t: t[0]))
    print(winner[1])
    return winner[1]
    
    