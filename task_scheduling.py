import collections

def find_completion_times(num_tasks, durations, dependencies):

    graph = collections.defaultdict(list)
    in_degree = [0] * num_tasks
    

    EST = [0] * num_tasks
    EFT = [0] * num_tasks
    

    for u, v in dependencies:
        graph[u].append(v)
        in_degree[v] += 1


    queue = collections.deque()
    for i in range(num_tasks):
        if in_degree[i] == 0:
            queue.append(i)

    topo_order = []
    while queue:
        node = queue.popleft()
        topo_order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)


    for node in topo_order:
        for neighbor in graph[node]:
            if EST[neighbor] < EFT[node]:
                EST[neighbor] = EFT[node]
            EFT[neighbor] = EST[neighbor] + durations[neighbor]


    LFT = [float('inf')] * num_tasks
    LST = [0] * num_tasks

    LFT[topo_order[-1]] = EFT[topo_order[-1]]
    for node in reversed(topo_order):
        if LFT[node] == float('inf'):
            LFT[node] = EFT[node]
        for neighbor in graph[node]:
            if LST[node] == 0 or LFT[neighbor] - durations[neighbor] < LST[node]:
                LST[node] = LFT[neighbor] - durations[neighbor]
            LFT[node] = min(LFT[node], LST[neighbor])

    return EFT[topo_order[-1]], LFT[topo_order[-1]]
if __name__ == "__main__":
    num_tasks = 6
    durations = [2, 4, 3, 1, 5, 2]
    dependencies = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4), (4, 5)]
    earliest_completion, latest_completion = find_completion_times(num_tasks, durations, dependencies)
    print(f"Earliest completion time: {earliest_completion}")
    print(f"Latest completion time: {latest_completion}")
