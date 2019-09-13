'''
    py script - Checks whether the file exists  in the specified path
    py libraries -
        1. os - Used to work with file directories and operating system
        2. os.path - Used to work with absolute paths
    classes-
            DirectoryCheck - Class to check if the file exists in the given directory
    '''

import os
import os.path

class DirectoryCheck:
    #Method returns a boolean value if the file or directory exists
    def checkDirectory(self,path):
        return (os.path.exists(path))



obj=DirectoryCheck()
print(obj.checkDirectory("C:\\Users\\pc\\PycharmProjects\\myDir\\newTest\\ABc.txt"))