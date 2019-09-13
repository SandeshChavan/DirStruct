'''
    py script - Log details to log file
    py libraries -
        1. logging - Used to implement log functions
    classes-
            Logger - Class to Log detaisl
    Methods-
          1.generateReport- takes in the status of different operation and logs it with timestamp
'''


import logging

class Logger:
    #Appends the report of the previous implementation with the respective timestamp
    def generateReport(self,createDirStatus,fileStatus,existStatus,List,paths):
        logging.basicConfig(filename="Dir.log", level=logging.DEBUG, format='%(levelname)s: %(asctime)s %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')
        logging.info(createDirStatus)
        logging.info(fileStatus)
        logging.info(existStatus)
        logging.info(List)
        logging.info(str(paths)+"\n")

