import collections
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        class trie_node:
            def __init__(self) -> None:
                self.children = collections.defaultdict(trie_node)
                self.suggestion = []
            
            def add_suggetion(self, product):
                if len(self.suggestion) < 3:
                    self.suggestion.append(product)
        
        class trie_tree:
            def __init__(self) -> None:
                self.root = trie_node()

            def insert(self, product):
                now = self.root
                for ch in product:
                    now = now.children[ch]
                    now.add_suggetion(product)
            
            def traversal(self,searchword):
                now, res = self.root, []
                for ch in searchword:
                    now = now.children[ch]
                    res.append(now.suggestion)
                return res

        products = sorted(products)
        Tire = trie_tree()
        for product in products:
            Tire.insert(product)
        
        return Tire.traversal(searchWord)

