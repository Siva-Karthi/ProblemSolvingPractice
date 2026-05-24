from collections import defaultdict
from typing import List


# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         if not prerequisites:
#             return True
#         pre_req_graph = defaultdict(list)
#         for i in range(numCourses):
#             pre_req_graph[i] = []
#         for a, b in prerequisites:
#             if a == b:
#                 return False
#             pre_req_graph[a].append(b)
#
#         res = [self.is_cycle_exists(start_node, pre_req_graph) for start_node in range(numCourses)]
#         print(res)
#         can_complete = True
#         for i in res:
#             if i:
#                 can_complete = False
#         return can_complete
#
#
#         # res = self.is_cycle_exists(3, pre_req_graph)
#         # return not res
#
#
#     def is_cycle_exists(self, start_node, pre_req_graph):
#         visited = {start_node: True}
#         stack = []
#         stack.extend(pre_req_graph[start_node])
#         is_cycle = False
#         while stack:
#             cur = stack.pop(0)
#             if cur in visited:
#                 is_cycle = True
#                 break
#             visited[cur] = True
#             if pre_req_graph[cur]:
#                 stack.extend(pre_req_graph[cur])
#         return is_cycle

class Solution():
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for node in range(numCourses):
            graph[node] = []
        for pre_req in prerequisites:
            graph[pre_req[0]].append(pre_req[1])
        print(graph)
        for i in range(numCourses):
            if graph[i]:
                if self.is_cycle_exists(i, graph[i], graph):
                    return False
        return True

    def is_cycle_exists(self, curnt: int, next: List, graph: defaultdict):
        visited: dict = dict()
        visited[curnt] = True
        while next:
            curnt = next.pop(0)
            if curnt in visited:
                return True
            visited[curnt] = True
            if graph[curnt]:
                next.extend(graph[curnt])
        return False


if __name__ == '__main__':
    # n = 2
    # pr = [[0,1]]
    # n = 2
    # pr = [[1, 0], [0, 1]]

    # n = 3
    # pr = [[1, 0], [2, 0], [0, 2]]
    n = 3
    pr = [[0, 1], [0, 2], [1, 2]]
    # pr = [[0,1],[0,2],[1,2]]
    # pr = [[1,4],[2,4],[3,1],[3,2]]
    print(Solution().canFinish(n, pr))
