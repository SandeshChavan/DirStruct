'''
    py script - Lists all the files in the specified path
    py libraries -
        1. os - Used to work with file directories and operating system
        2. os.path - Used to work with absolute paths
    classes-
            ListDirectory - Class to list the directory
'''

import os
import os.path

class ListDirectory:

    #Method returns dictionary of files and sub directories in the specified directory
    def listDirectory(self,path):
        list={"Files":[],"Sub Directories":[]}
        try:
            if(not(os.path.exists(path))):
                raise os.error
            for node in os.listdir(path):
                if (os.path.isfile(path+"\\"+str(node))):
                    list["Files"].append(node)
                else:
                    list["Sub Directories"].append(node)
        except os.error:
            print("Path not found")
        return list

# obj=ListDirectory()
# print(obj.listDirectory("C:\\Users\\pc\\PycharmProjects\\myDir"))

