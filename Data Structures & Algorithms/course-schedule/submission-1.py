class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqmap = {i:[] for i in range(numCourses)}

        #[a, b]
        for course, pre in prerequisites:
            prereqmap[course].append(pre)

        visitedCourses = set()
        def dfs(crs):
            if crs in visitedCourses:
                return False

            if prereqmap[crs] == []:
                return True

            visitedCourses.add(crs)
            for pre in prereqmap[crs]:
                if not dfs(pre):
                    return False
            visitedCourses.remove(crs)
            prereqmap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True