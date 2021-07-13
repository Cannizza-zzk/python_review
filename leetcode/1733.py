class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        def is_connect(i, j):
            set_i = set(languages[i])
            set_j = set(languages[j])
            if len(set_i & set_j) != 0:
                return True
            else:
                return False

        unconnect = []
        for friendship in friendships:
            if not is_connect(friendship[0]- 1,friendship[1]-1):
                unconnect.append(friendship)

        unconnectPerson = set()
        for friendship in unconnect:
            unconnectPerson.add(friendship[0]-1)
            unconnectPerson.add(friendship[1]-1)


        res = 500
        for candidate in range(1,n+1):
            cnt = 0
            for person in unconnectPerson:
                if candidate not in languages[person]:
                    cnt += 1
            if cnt < res: res = cnt
        
        return res