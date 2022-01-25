import re
from cleanStrings import cleanstrings
from traces import strings, signatures
import time
import hashlib
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
    
    def md5Signatures(self, path):
        fileObj = open(path, 'rb')
        hash = hashlib.md5()
        while True:
            file = fileObj.read(8096)
            if not file:
                break
            hash.update(file)
        if hash.hexdigest() in signatures.md5:
            return hash.hexdigest()

if __name__ == "__main__":
    smasher = RavenSmasher()
    t = time.time()
    
    # Check MD5 Signature
    print("----- Singnatures -----")
    result = smasher.md5Signatures(sys.argv[1])
    if result != None:
        print("Flagged MD5 Signature. I recommend you to ban the player without any doubt.")
    print("------------------------")

    # Scan a mod
    print("------- Strings --------")
    try:
        result = smasher.stringsMod(sys.argv[1])
    except IndexError:
        print("Please specify the mod path to find.")
        exit(-1)
    per = result["detected"] / result["tested"] * 100
    print("Scan Ended. Took " + str(time.time() - t)  + "seconds.")
    print(str(per) + "% of strings detected (" + str(result["detected"] + "/" + str(result["tested"])))
    if per > 95: print("Detected. I would recommend you to ban the player")
    elif per > 60: print("Highly Suspicious. I would recommend you to check the file with a decompiler.")
    elif per > 20: print("Suspicious. I would recommend you to check the file with a decompiler.")
    else: print("Probably Clean, if you think something isn't good, you can check with a decompiler.")
    print("------------------------")