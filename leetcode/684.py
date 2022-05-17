import collections


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        class Trie_node:
            def __init__(self) -> None:
                self.children = collections.defaultdict(Trie_node)
                self.rpath = False
                self.end = False
                self.rname = None
            
        class Trie_tree:
            def __init__(self) -> None:
                self.root = Trie_node()

            def insert(self, rword):
                now = self.root
                for ch in rword:
                    now = now.children[ch]
                    now.rpath = True
                now.end = True
                now.rname = rword

            def replace(self, succ):
                now = self.root
                for ch in succ:
                    now = now.children[ch]
                    if not now.rpath:
                        return succ
                    if now.end:
                        return now.rname
                return succ
                    
        t = Trie_tree()
        for root in dictionary:
            t.insert(root)

        slist = sentence.split(' ')
        for idx, succ in enumerate(slist):
            slist[idx] = t.replace(succ)
        return ' '.join(slist)