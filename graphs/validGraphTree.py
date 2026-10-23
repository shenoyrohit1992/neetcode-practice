class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True

        adj = {i: [] for i in range(n)}
        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)

        visit = set()  # tracks already visited nodes & counter

        def dfs(curr, prev):
            # prev required because parent needs to be skipped-undirected
            if curr in visit:
                return False

            visit.add(curr)
            for nei in adj[curr]:
                if nei == prev:
                    continue
                if dfs(nei, curr) == False:
                    return False
            return True

        # dummy val for node 0; and for a tree every node should be connected (check len)
        return dfs(0, -1) and n == len(visit)
