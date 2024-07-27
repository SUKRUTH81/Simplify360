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
