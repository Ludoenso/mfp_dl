# Todo :
# - Dynamicly fix title name for file system

class song(object):

    __init__(self,url,name):

        self.url = url

        self.name = self.convert_name()

    def convert_name(self):
