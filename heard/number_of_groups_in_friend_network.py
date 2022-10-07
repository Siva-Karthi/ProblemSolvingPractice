# In a particular social network friends are automatically allocated to users by the system and users cannot add friends of their choice on their own. There are currently N users on the social network, labeled from 2 to N + 1. For every i-th user (where i ranges from 2 to N + 1), the system allocated all the users labeled with multiples of i as the user's friends (if possible). One day, all users of the social network come together for a meeting and form groups such that each person in a group is a direct friend or a friend of friend of every other person of that group.

# Example:

# input: 10
# Output: 3

# Explanation:

# Three groups will be formed:{2, 3, 4, 5, 6, 8, 9, 10}, {7} and {11}



N = 10
def friends_groups(N):
    graph = {}
    for parent in range(2, N+2):
        graph[parent] = list(range(parent,N+2,parent))[1:]
    for parent in graph:
        childs = graph[parent]
        for child in childs:
            if parent not in graph[child]:
                graph[child].append(parent)
    print(graph)
    tot_visited = 0
    visted = {node : False for node in range(2,N+2)}
    for node in graph:
        if not visted[node]:
            tot_visited += 1
            visted[node] = True
            childs = []
            childs.extend([i for i in reversed(graph[node]) if not visted[i]])
            while childs:
                child = childs.pop()
                visted[child] = True
                childs.extend([i for i in reversed(graph[child]) if not visted[i]])
            # print(node, "- ",visted,"\n")
    print("no of groups", tot_visited)
    return tot_visited

print("friends_groups",friends_groups(N))
