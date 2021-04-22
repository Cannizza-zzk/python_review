class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.Mdict = {}
        

    def buildDict(self, dictionary: List[str]) -> None:
        for string in dictionary:
            if self.Mdict.get(len(string)) == None:
                self.Mdict[len(string)] = []
                self.Mdict[len(string)].append(string)
            else:
                self.Mdict[len(string)].append(string)

    def search(self, searchWord: str) -> bool:
        if self.Mdict.get(len(searchWord)) == None:
            return False
        targlist = self.Mdict[len(searchWord)]
        def cmp_str(targstr, inputstr):
            cnt = 0
            flag = False
            for i in range(0,len(targstr)):
                if targstr[i] != inputstr[i]:
                    cnt += 1
                if cnt == 2:
                    flag = False
                    break
                elif cnt == 1:
                    flag = True
            return flag

        for targstr in targlist:
            if cmp_str(targstr, searchWord) == True:
                return True
        return False



# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)