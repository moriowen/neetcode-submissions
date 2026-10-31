class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_map = {i:[] for i in range(numCourses)}

        for course, pre in prerequisites:
            pre_map[course].append(pre)
        
        visited = set()
        visiting = set()
        res = []

        def dfs(course):
            if course in visited:
                return True

            if course in visiting:
                return False
            
            visiting.add(course)

            for pre in pre_map[course]:
                if not dfs(pre):
                    return False
                
            visited.add(course)
            visiting.remove(course)
            res.append(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return res