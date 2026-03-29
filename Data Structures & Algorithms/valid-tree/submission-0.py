class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        
        prev = -1
        visitSet = set()
        adj = { i:[] for i in range(n)}

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        
        def dfs(i, prev):
            if i in visitSet:
                return False
            visitSet.add(i)

            for j in adj[i]:
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False

            return True
        
        
        return dfs(0, prev) and n == len(visitSet)