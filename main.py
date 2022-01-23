import re
from cleanStrings import cleanstrings
from traces import strings
import time
import sys

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
    
    def findUncheckedStrings(self, path):
        """
        Function for finding strings of a specific path, without checking if they're in cleanStrings
        """
        return re.findall("[a-zA-Z0-9]+",str(open(path,"rb").read()))

    def stringsMod(self, path):
        """
        Function for scanning mods to check if it's detected or not
        """
        r = {}
        r["detected"] = 0
        r["tested"] = 0
        for string in re.findall("[a-zA-Z0-9]+",str(open(path,"rb").read())):
            t = time.time()
            if string in strings.strings: r["detected"] += 1
            if string not in cleanstrings: r["tested"] += 1
        return r

if __name__ == "__main__":
    smasher = RavenSmasher()
