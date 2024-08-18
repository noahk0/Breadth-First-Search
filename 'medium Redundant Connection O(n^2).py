def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    union = {}
        
    for v in edges:
        v1, v2 = v
            
        while v1 != union.get(v1, v1):
            v1 = union.get(v1, v1)

        while v2 != union.get(v2, v2):
            v2 = union.get(v2, v2)

        if v1 == v2:
            return v

        union[v1] = v2
