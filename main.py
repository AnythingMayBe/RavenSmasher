import re
from cleanStrings import cleanstrings
class RavenSmasher:
    def __init__(self):
        super().__init__()
    
    def findStrings(self, path):
        """
        Function for finding strings of a spefic path, who aren't in cleanStrings
        """
        r = []
        for string in re.findall("[a-zA-Z0-9]+",str(open(path,"rb").read())):
            if string not in cleanstrings: r.append(string)
        return r

if __name__ == "__main__":
    smasher = RavenSmasher()