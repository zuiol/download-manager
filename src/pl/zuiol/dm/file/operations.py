from os.path import os
def readFile():
    file = open('C:\\Damian\\python.txt', 'r')    
    print(file.read())
    
def moveFile(sourceFilePath, destinationFilePath):
    #os.renames - moves file and create missing dictionaries if needed
    os.renames(sourceFilePath, destinationFilePath)
 
def sayHello():
    print("Hello it is me!")
       
#moveFile()

