# Task Scheduling Problem

## Problem Statement
Determine the earliest and latest times all tasks will be completed given their dependencies.

## Approach
1. **Graph Representation**: Represent tasks and dependencies as a directed graph.
2. **Topological Sorting**: Determine the order of task execution based on dependencies.
3. **Calculating EST and EFT**: Calculate Earliest Start Time (EST) and Earliest Finish Time (EFT).
4. **Calculating LFT and LST**: Calculate Latest Finish Time (LFT) and Latest Start Time (LST).

## Instructions to Run
1. Ensure Python is installed on your system.
2. Run the script using the command: `python task_scheduling.py`

## Time and Space Complexity
- **Time Complexity**: O(V + E)
- **Space Complexity**: O(V + E)



# Social Network Connections Problem

## Problem Statement
Find the friends of Alice and Bob, their common friends, and the nth connection between any two friends in a social network.

## Approach
1. **Graph Representation**: Represent the social network as an adjacency list.
2. **Finding Friends**: Directly access the adjacency list.
3. **Finding Common Friends**: Use set intersection on the friends lists of two people.
4. **Finding nth Connection**: Use Breadth-First Search (BFS) to find the shortest path between two people.

## Instructions to Run
1. Ensure Python is installed on your system.
2. Run the script using the command: `python social_network_connections.py`

## Time and Space Complexity
- **Time Complexity**: O(V + E)
- **Space Complexity**: O(V + E)
