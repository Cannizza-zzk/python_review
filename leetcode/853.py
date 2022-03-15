class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n_car = len(position)
        car_state = []
        for i in range(n_car):
            car_state.append([position[i],speed[i]])
        car_state.sort(key = lambda x : x[0],reverse=True)

        car_stack = []
        time_consume = (target - car_state[0][0]) / car_state[0][1]
        res = 1
        while len(car_state) != 0:
            car = car_state.pop(0)
            time_cur = (target - car[0]) / car[1]
            if time_consume >= time_cur:
                car_stack.append(car)
            else:
                res += 1
                car_stack = [car]
                time_consume = time_cur
        
        return res
