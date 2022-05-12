import collections


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        

        class trie_node:
            def __init__(self) -> None:
                self.children = collections.defaultdict(trie_node)
                self.is_end = False

        class trie_tree:
            def __init__(self) -> None:
                self.root = trie_node()
            
            def insert(self, file_path):
                now = self.root
                is_sub = False
                for folder in file_path:
                    now = now.children[folder]
                    if now.is_end:
                        is_sub = True
                now.is_end = True
                return is_sub

        folder = sorted(folder,key=lambda x: x.count('/'))
        t = trie_tree()
        res = []
        for folder_name in folder:
            f = folder_name.split('/')
            f.pop(0)
            if not t.insert(f):
                res.append(folder_name)

        return res




