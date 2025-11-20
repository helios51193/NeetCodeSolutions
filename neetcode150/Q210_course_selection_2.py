from collections import defaultdict, deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:

       # Create a prequisite list and a graph
        preq = {i:set() for i in range(numCourses)}

        graph = defaultdict(set)

        for i,j in prerequisites:
            preq[i].add(j)
            graph[j].add(i)
        
        # add all the course for which there are no prerequisite couse in a queue
        q = deque([])
        for k, v in preq.items():
            if len(v) == 0:
                q.append(k)
        
        taken = []
        while q:
            course = q.popleft()
            taken.append(course)
            # return if we have visited all courses
            if len(taken) == numCourses:
                return taken
            
            # If the course we've just taken was a prereq for the next course, remove it from its prereqs.
            for cor in graph[course]:
                preq[cor].remove(course)
                # If we've taken all of the preqs for the new course, we'll visit it.
                if not preq[cor]:
                    q.append(cor)
        
        return []

"""
    Last Looked
    20-11-25

""" 



        