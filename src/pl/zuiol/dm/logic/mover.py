"""
This File might contain functions maybe classes that should support determining what 
should be don e with particular file handled by application

The main goal is to determine destination folder of managed file
"""
from pl.zuiol.dm.file.operations import moveFile

def moveHandledFile(sourceFilePath, key_words):
    print("In moveHandledFile method")
    print(key_words)
    
    words = key_words.split(" ")
    destinationFilePath = "C:\\Users\\sg0212049\\Downloads\\DownloadManager\\"
    for word in words:
        print(word)
        destinationFilePath = destinationFilePath.__add__(word + "\\")
    
    print("destination: " + destinationFilePath)
    print("source: " + sourceFilePath)
    
    names = sourceFilePath.split("\\")
    for name in names:
        if "." in name:
            destinationFilePath = destinationFilePath.__add__(name)
            
    moveFile(sourceFilePath, destinationFilePath)
    