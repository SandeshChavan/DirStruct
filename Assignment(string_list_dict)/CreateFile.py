'''
    py script - Creates file within directory on being  provided by an absolute path
    py libraries -
        1. os - Used to work with file directories and operating system
        2. os.path - Used to work with absolute paths
        3. re - Used to validate strings
'''
import os
import os.path

class CreateFile:
    def __init__(self):
        pass

    def createFile(self,path):
        try:
            os.mkdir(path)
            return ((path, "TRUE"))
        except (FileExistsError):
            print("Unable to create file.File already exists")
            return ((("NO such directory created", "FAlSE")))

obj= CreateFile()
print(obj.createFile("C:\\Users\\pc\\PycharmProjects\\myDir\\newTest\\ABc.txt"))