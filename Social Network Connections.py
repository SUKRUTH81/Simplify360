import collections

def find_friends(graph, person):
    return graph[person]

def common_friends(graph, person1, person2):
    return set(graph[person1]).intersection(graph[person2])

def nth_connection(graph, start, end):
    if start == end:
        return 0
    
    visited = set()
    queue = collections.deque([(start, 0)])
    visited.add(start)

    while queue:
        current, depth = queue.popleft()
        for neighbor in graph[current]:
            if neighbor not in visited:
                if neighbor == end:
                    return depth + 1
                queue.append((neighbor, depth + 1))
                visited.add(neighbor)
  
    return -1

if __name__ == "__main__":
    graph = {
        'Alice': ['Bob', 'Charlie'],
        'Bob': ['Alice', 'David', 'Eve'],
        'Charlie': ['Alice', 'David'],
        'David': ['Bob', 'Charlie', 'Frank'],
        'Eve': ['Bob'],
        'Frank': ['David']
    }

    alice_friends = find_friends(graph, 'Alice')
    bob_friends = find_friends(graph, 'Bob')
    common = common_friends(graph, 'Alice', 'Bob')
    connection = nth_connection(graph, 'Alice', 'Frank')

    print(f"Alice's friends: {alice_friends}")
    print(f"Bob's friends: {bob_friends}")
    print(f"Common friends of Alice and Bob: {common}")
    print(f"Connection between Alice and Frank: {connection}")
