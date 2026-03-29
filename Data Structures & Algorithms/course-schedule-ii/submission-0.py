class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqMap = {i:[] for i in range(numCourses)}
        visited = set()
        
        for i, n in prerequisites:
            prereqMap[i].append(n)

        res = []
        visit, cycle = set(), set()


        def dfs(node):
            if node in cycle:
                return False

            if node in visit:
                return True

            cycle.add(node)

            for p in prereqMap[node]:
                if dfs(p) == False:
                    return False

            cycle.remove(node)
            visit.add(node)
            res.append(node)
            return True

        
        for c in range(numCourses):
            if not dfs(c):
                return []

        return res
                
