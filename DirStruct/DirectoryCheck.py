'''
    py script - Checks whether the file exists  in the specified path
    py libraries -
        1. os - Used to work with file directories and operating system
        2. os.path - Used to work with absolute paths
    classes-
            DirectoryCheck - Class to check if the file exists in the given directory
    DirectoryCheck methods-
          1.checkDirectory- returns a boolean depending on existence of the file
'''

import os
import os.path

class DirectoryCheck:

    def checkDirectory(self,path):
        return (os.path.exists(path))



# obj=DirectoryCheck()
# print(obj.checkDirectory("C:\\Users\\pc\\PycharmProjects\\myDir\\test1.txt"))