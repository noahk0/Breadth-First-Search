def validTree(self, n: int, edges: List[List[int]]) -> bool:
    if n != len(edges) + 1:
        return False

    seen, graph = set(), defaultdict(list)

    for v1, v2 in edges:
        graph[v1].append(v2)
        graph[v2].append(v1)

    def dfs(s, pre):
        if s in seen:
            return True

        seen.add(s)

        for e in graph[s]:
            if e != pre:
                dfs(e, s)

    return not dfs(0, None) and n == len(seen)
