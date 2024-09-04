def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    seen, graph = set(), defaultdict(list)

    for value, key in prerequisites:
        graph[key].append(value)

    def dfs(key):
        if key in seen:
            return True

        seen.add(key)

        for value in graph[key]:
            if dfs(value):
                return True

        del graph[key]
        seen.remove(key)

    for key in range(numCourses):
        if dfs(key):
            return False

    return True
