'''
    py script - Implements linux directory structure
    py modules -
            CreateDirectory - Module to create directory
            CreateFile - Module to create files
            DirectoryList -  Module to list the directory
            DirectoryCheck - Module to check existence of file or directory
            DirectorySearch - Module to list all the directories or file with matching sub string
            Logger - Module to log the details to a log file with TimeStamp
    '''



from DirStruct.CreateDirectory import *
from DirStruct.CreateFile import *
from DirStruct.DirectoryList import *
from DirStruct.DirectoryCheck import *
from DirStruct.DirectorySearch import *
from DirStruct.Logger import *


obj=CreateDirectory()
createDirStatus=obj.createDirectory("C:\\Users\\pc\\PycharmProjects\\myDir\\newTest")
obj=CreateFile()
fileStatus=obj.createFile("C:\\Users\\pc\\PycharmProjects\\myDir\\newTest\\test.txt")
obj=DirectoryCheck()
existStatus=obj.checkDirectory("C:\\Users\\pc\\PycharmProjects\\myDir\\newTest\\test.txt")
obj=ListDirectory()
List=obj.listDirectory("C:\\Users\\pc\\PycharmProjects\\myDir")
obj=DirectorySearh()
paths=obj.searchDirectory("C:\\Users\\pc\\PycharmProjects\\myDir",".txt")
obj=Logger()
obj.generateReport(createDirStatus,fileStatus,existStatus,List,paths)