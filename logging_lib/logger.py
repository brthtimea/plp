from datetime import datetime

loggerDict = {'INFO': "info_log.txt",'DEBUG': "debug_log.txt" , 'WARNING':"warning_log.txt", 'ERROR':"error_log.txt" , 'CRITICAL': "critical_log.txt"}

class Logger(object):
    """custom Logger"""
    def __init__(self, name):
        self.name = name

    def setLevel(self, level):
        self.level = level

    def info(self, path, msg):
        self.log_to_file(path, msg)

    def debug(self, path, msg):
        self.log_to_file(path, msg)

    def warning(self, path, msg):
        self.log_to_file(path, msg)

    def error(self,path, msg):
        self.log_to_file(path, msg)

    def critical(self,path, msg):
        self.log_to_file(path, msg)        

    def generic_log(self, level, msg):
        self.level = level
        #loggerLevel = [x for x in loggerDict if x == level]
        for k in loggerDict:
            if k == level:
                self.log_to_file(loggerDict[k], msg) 

    def log_to_file(self, path, msg):
        f = open(path, 'a')
        f.write(str(msg) + ':' + str('{dt:%Y-%m-%d}.'.format(dt=datetime.now())) + '\n') 
        f.close()

    
                    