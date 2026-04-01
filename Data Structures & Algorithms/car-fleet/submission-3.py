class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = [(pos,spd) for pos,spd in zip(position,speed)]
        cars.sort(reverse=True)
        for car in cars:
            stack.append((target-car[0]) / car[1])
            if len(stack)>=2 and stack[-2] >= stack[-1]:
                stack.pop()
        #print(cars)
        return len(stack)