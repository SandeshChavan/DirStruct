'''
    py script - Returns all the substrings of the specifid path
    py libraries -
        1. os - Used to work with file directories and operating system
        2. os.path - Used to work with absolute paths
    classes-
            DirectorySearch - Class to check for all matching path with specified path
    DirectoryCheck methods-
          1.searchDirectory- returns all matching sub string
'''

import os
import os.path

class DirectorySearh:

    def searchDirectory(self,path,searchString):
        try:
            if(not(os.path.exists(path))):
                raise os.error
            for root, dirs, files in os.walk(path,topdown=True):
                for file in files:
                    str=root+"\\"+file
                    if str.endswith(searchString):
                        print(str)
                for dir in dirs:
                    str=root+"\\"+dir
                    if str.endswith(searchString):
                        print(str)
        except os.error:
            print("Path not found")

# obj=DirectorySearh()
# obj.searchDirectory("C:\\Users\\pc\\PycharmProjects\\myDir",".txt")