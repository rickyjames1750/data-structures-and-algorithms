class Solution:
    def canFinish(self, numCourses: int, prequisities: List[List[int]]) -> bool:
        graph = collections.defualtdict(list)
        for edge in prequisities:
            graph[edge[0]].append(edge[1])

        visited = set()

        # True if there is a cycle. False if there is not. 
        def visit(vertex):
            visited.add(vertex)
            for neighbor in graph[vertex]:
                if neighbor in visited or visit(neighbor):
                    return True
                
            visited.remove(vertex)
            return False

        for i in range(numCourses):
            if visit():
                return False
        return True