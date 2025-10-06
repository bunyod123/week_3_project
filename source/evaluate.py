import logging

logger = logging.getLogger(__name__)

class qosh:
    def __init__(self, num):
        self.num = num
        
    def kop(self,num):
        return num ** 3
        logger.info("3 ga kopaytirildi") 