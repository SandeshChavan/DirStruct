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



from DirStruct.CreateDirectory.CreateDirectory import  *
from DirStruct.CreateFile.CreateFile import *
from DirStruct.DirectoryList.DirectoryList import *
from DirStruct.DirectoryCheck.DirectoryCheck import *
from DirStruct.DirectorySearch.DirectorySearch import *
from DirStruct.Logger.Logger import *


CreateDir=CreateDirectory()
createDirStatus=CreateDir.createDirectory("C:\\Users\\pc\\PycharmProjects\\myDir\\newTest")
CreateFile=CreateFile()
fileStatus=CreateFile.createFile("C:\\Users\\pc\\PycharmProjects\\myDir\\newTest\\test.txt")
DirCheck=DirectoryCheck()
existStatus=DirCheck.checkDirectory("C:\\Users\\pc\\PycharmProjects\\myDir\\newTest\\test.txt")
ListDir=ListDirectory()
List=ListDir.listDirectory("C:\\Users\\pc\\PycharmProjects\\myDir")
DirSearch=DirectorySearh()
paths=DirSearch.searchDirectory("C:\\Users\\pc\\PycharmProjects\\myDir",".txt")
Log=Logger()
Log.generateReport(createDirStatus,fileStatus,existStatus,List,paths)