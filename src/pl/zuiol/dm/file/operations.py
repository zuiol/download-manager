from os.path import os
def readFile():
    file = open('C:\\Damian\\python.txt', 'r')    
    print(file.read())
    
def moveFile(sourceFilePath, destinationFilePath):
    #os.renames - moves file and create missing dictionaries if needed
    #os.renames(sourceFilePath, destinationFilePath)
    os.replace(sourceFilePath, destinationFilePath)
def sayHello():
    print("Hello it is me!")
       
def getSubDirs(directory, word):
    print("In GetSubDirs method")
    foundDirs = list()
    if os.path.isdir(directory):
        for root, dirs, files in os.walk(directory):
            """for name in dirs:
                print(name)"""
            print("Root: " + root)
            for d in dirs:
                print(d)
                if d == word:
                    print("Hurra!!")
                    p = os.path.join(root, d)
                    print(p)                
                    level = getDirLevel(p)
                    print(level)
                    tup = (level, p);
                    foundDirs.append(tup)
                    
        tup = (99, os.path.join(directory, word));
        foundDirs.append(tup)
        
        return foundDirs
                    
                
def getDirLevel(directory):
    print("In getDirLevel methond")
    level = directory.split("\\")
    count = 1
    for l in level:
        print(l)
        count = count + 1
    print("real level: %d" % count)
    return count
    
if __name__ == '__main__': 
    words = "BRD level one".split(" ")
    getSubDirs("C:\\Users\\xxxxxxxx\\Downloads\\DownloadManager\\", "BRD")
    