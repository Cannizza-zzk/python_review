from collections import defaultdict
from re import L


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        is_ingredient = defaultdict(list)
        pre_recipe = [len(i) for i in ingredients]
        for idx in range(len(recipes)):
            for ing in ingredients[idx]:
                if ing in recipes:
                    is_ingredient[ing].append(idx)

        ans, re_stack = [] , []
        for idx in range(len(recipes)):
            for ing in ingredients[idx]:
                if ing in supplies:
                    pre_recipe[idx] -= 1

            if pre_recipe[idx] == 0:
                re_stack.append(idx)

        while re_stack:
            r_idx = re_stack.pop()
            r = recipes[r_idx]

            for item in is_ingredient[r]:
                pre_recipe[item] -= 1
                if pre_recipe[item] == 0:
                    re_stack.append(item)

        for i in range(len(recipes)):
            if pre_recipe[i] == 0:
                ans.append(recipes[i])
        return ans





