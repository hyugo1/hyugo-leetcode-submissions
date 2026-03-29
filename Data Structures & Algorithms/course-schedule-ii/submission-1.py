class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        prereqmap ={i : [] for i in range(numCourses)}
        for a, b in prerequisites:
            prereqmap[a].append(b)

        visit, cycle = set(), set()
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            cycle.add(crs)
            for pre in prereqmap[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            res.append(crs)
            return True
            
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res