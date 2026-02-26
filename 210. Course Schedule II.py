from collections import deque

class Solution:
    def findOrder(self, numCourses, prerequisites):
        # Step 1: Build adjacency list and in-degree count
        adj = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        
        for course, pre in prerequisites:
            adj[pre].append(course)
            in_degree[course] += 1
        
        # Step 2: Initialize queue with courses having no prerequisites
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        order = []
        
        # Step 3: Process courses
        while queue:
            current = queue.popleft()
            order.append(current)
            
            for neighbor in adj[current]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Step 4: Check if all courses are processed
        return order if len(order) == numCourses else []
