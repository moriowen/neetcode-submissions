class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        - stack 
        - sort as per position in reverse because we need to know wrt farthest car
        - collapse the individual cars by comparing how long it takes to them to get to target and if the time is smaller than the car ahead of them 
        """
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(key = lambda x: x[0], reverse=True)
        stack = []

        for car in pair:
            if not stack:
                stack.append(car)

            curr_time_to_target = (target - car[0])/car[1]
            top_time_to_target = (target - stack[-1][0])/stack[-1][1]
            
            if curr_time_to_target > top_time_to_target:
                stack.append(car)

        return len(stack)
