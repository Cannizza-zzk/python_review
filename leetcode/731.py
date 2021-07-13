class MyCalendarTwo:

    def __init__(self):
        self.booked = []
        self.double_booked = []
        
    def has_intersec(self, s1,e1,s2,e2):
        if s1 < e2  and s1 >= s2:
            return [s1,min(e1,e2)]
        elif s2 < e1 and s2 >= s1:
            return [s2,min(e1,e2)]
        else:
            return False

    def book(self, start: int, end: int) -> bool:
        #print(self.booked)
        #print(self.double_booked)
        for timeSeg in self.double_booked:
            if self.has_intersec(start,end,timeSeg[0],timeSeg[1]) != False:
                return False
            
        for timeSeg in self.booked:
            if self.has_intersec(start,end,timeSeg[0],timeSeg[1]) != False:
                self.double_booked.append(self.has_intersec(start,end,timeSeg[0],timeSeg[1]))
        self.booked.append([start,end])
        
        return True
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)