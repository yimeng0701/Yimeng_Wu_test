import re

class Solution:
    
    def checkInput(self,data):
        valid_input = re.compile(r"(v?[0-9]\d*)((\.[0-9]\d*)*)?([a-z])?(\s)(v?[0-9]\d*)((\.[0-9]\d*)*)?([a-z])?(\s*)?$")
        if valid_input.match(data):
            return True
        else: return False
        
    def cleanData(self,data):
        # remove the first 'v'
        data = re.sub("v","",data)
        # add "-" before the alpha (easy to spllit)
        data = re.sub("[a-z]",lambda x:"-"+x.group(0),data)
        data = data.strip()
        v1 = (data.split()[0]).split(".")
        v2 = (data.split()[1]).split(".")
        return v1,v2
        
    def compareVersion(self,data):
        version1,version2= data.split()[0],data.split()[1]
        v1,v2 = self.cleanData(data)
        n = len(v1)
        m = len(v2)
        if n<m:
            v1.extend(['0']*(m-n))
        elif n>m:
            v2.extend(['0']*(n-m))
        
        for i in range(len(v1)):
            t1 = v1[i].split("-")
            t2 = v2[i].split("-")
            if t1[0]==t2[0] and len(t1)>len(t2):
                return "{} is less than {}".format(version1,version2) 
            elif t1[0]==t2[0] and len(t1)<len(t2):
                return "{} is greater than {}".format(version1,version2) 
            else:
                if v1[i]>v2[i]:
                    return "{} is greater than {}".format(version1,version2) 
                elif v1[i]<v2[i]:
                    return "{} is less than {}".format(version1,version2)  
        return "{} is equal to {}".format(version1,version2)  

def main():
    while True:
        data = input("Please enter your test cases (e.g.: 1.0 1.0.1):")
        if Solution().checkInput(data):
            break
        else:
            print("Wrong versions! Try again:")
            continue
    ans = Solution().compareVersion(data)
    print("{}".format(ans))


if __name__ == "__main__": 
    main()
        
    
    

