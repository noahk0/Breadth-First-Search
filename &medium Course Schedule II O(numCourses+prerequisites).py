def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    order, seen, scheduled, graph = [], set(), set(), defaultdict(list)

    for course, prereq in prerequisites:
        graph[course].append(prereq)

    def dfs(course):
        if course in seen:
            return True
            
        if course not in scheduled:
            seen.add(course)

            for prereq in graph[course]:
                if dfs(prereq):
                    return True

            seen.remove(course)
            order.append(course)
            scheduled.add(course)

    for course in range(numCourses):
        if dfs(course):
            return []

    return order
