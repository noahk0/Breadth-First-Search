def countComponents(self, n: int, edges: List[List[int]]) -> int:
    find, union = {}, set()

    for v1, v2 in edges:
        while v1 != find.get(v1, v1):
            v1 = find.get(v1, v1)

        while v2 != find.get(v2, v2):
            v2 = find.get(v2, v2)

        find[v1] = v2

    for i in range(n):
        while i != find.get(i, i):
            i = find.get(i, i)

        union.add(i)
            
    return len(union)
