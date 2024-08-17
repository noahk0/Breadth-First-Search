def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
    if node:
        q, graph = deque([node]), {node.val: Node(node.val)}

        while q:
            for neighbor in q[0].neighbors:
                if neighbor.val not in graph:
                    q.append(neighbor)
                    graph[neighbor.val] = Node(neighbor.val)

                graph[q[0].val].neighbors.append(graph[neighbor.val])

            q.popleft()

        return graph[node.val]
