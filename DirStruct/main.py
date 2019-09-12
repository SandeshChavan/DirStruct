'''
    py script - Implements linux directory structure
    py modules -
            CreateDirectory - Module to create directory
            CreateFile - Module to create files
            DirectoryList -  Module to list the directory
            DirectoryCheck - Module to check existence of file or directory
            DirectorySearch - Module to list all the directories or file with matching sub string
    classes-
            DirectryStructure - Class to implement all the directory operations
    '''
from DirStruct.CreateDirectory import *
from DirStruct.CreateFile import *
from DirStruct.DirectoryList import *
from DirStruct.DirectoryCheck import *
from DirStruct.DirectorySearch import *

obj=DirectoryCheck()
print(obj.checkDirectory("C:\\Users\\pc\\PycharmProjects\\myDir\\test1.txt"))
