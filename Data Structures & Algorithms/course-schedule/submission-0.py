class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prerequisiteMap = {i : [] for i in range(numCourses) }

        for course, pre in prerequisites:
            prerequisiteMap[course].append(pre)

        
        visitSet = set()
        def dfs(crs): 
            if crs in visitSet:
                return False
            if prerequisiteMap[crs] == []:
                return True

            visitSet.add(crs)
            for pre in prerequisiteMap[crs]:
                if not dfs(pre):
                    return False 
            visitSet.remove(crs)
            prerequisiteMap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True
        