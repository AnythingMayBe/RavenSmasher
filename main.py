import re
from cleanStrings import cleanstrings
class RavenSmasher:
    def __init__(self):
        super().__init__()
    
    def findStrings(self, path):
        r = []
        for string in re.findall("[a-zA-Z0-9]+",str(open("/Users/nojo/Downloads/Raven.jar","rb").read())):
            if string not in cleanstrings:
                r.append(string)
        return r

if __name__ == "__main__":
    smasher = RavenSmasher()