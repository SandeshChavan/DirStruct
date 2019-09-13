'''
    py script - Creates directory on provided an absolute path
    py libraries -
        1. os - Used to work with file directories and operating system
        2. os.path - Used to work with absolute paths
'''

import os
import os.path

class CreateDirectory:
    def __init__(self):
        pass

    #Method to create the directories by passing the absolute path as the function parameter
    def createDirectory(self,path):
        try:
                os.makedirs(path)
                return ((path,"TRUE"))
        except (os.error):
            print("Unable to create directories")
            return ((("NO such directory created", "FAlSE")))


obj= CreateDirectory()
print(obj.createDirectory("C:\\Users\\pc\\PycharmProjects\\myDir\\newTest\\test\\abc"))