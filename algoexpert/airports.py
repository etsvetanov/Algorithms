from typing import List, Set, Tuple, Dict
from queue import LifoQueue


# class Node:
#     def __init__(self, val, edges):
#         self.val = val
#         self.edges = edges


class Graph:
    def __init__(self, links):
        self.graph: Dict[str, Set] = {}

        for source, target in links:
            self.graph[source] = target

    def __getitem__(self, item):
        return self.graph[item]

    def dfs(self, head):
        visited = set()
        to_visit = LifoQueue()
        to_visit.put(head)

        while not to_visit.empty():
            curr = to_visit.get()

            for neigh in self[curr]:
                if neigh not in visited:
                    to_visit.put(neigh)
                    visited.add(neigh)


class Solution:
    def answer(self, airports: Set[str], routes: Set[Tuple[str, str]]):
        pass

    @staticmethod
    def graph_build(edges, reverse):
        pass


airports = {'BGI', 'CDG', 'DEL', 'DOH', 'DSM', 'EWR', 'EYW', 'HND', 'ICN',
            'JFK', 'LGA', 'LHR', 'ORD', 'SAN', 'SFO', 'SIN', 'TLV', 'BUD'}

routes = {
    ('DSM', 'ORD'),
    ('ORD', 'BGI'),
    ('BGI', 'LGA'),
    ('SIN', 'CDG'),
    ('CDG', 'SIN'),
    ('CDG', 'BUD'),
    ('DEL', 'DOH'),
    ('DEL', 'CDG'),
    ('TLV', 'DEL'),
    ('EWR', 'HND'),
    ('HND', 'ICN'),
    ('HND', 'JFK'),
    ('ICN', 'JFK'),
    ('JFK', 'LGA'),
    ('EYW', 'LHR'),
    ('LHR', 'SFO'),
    ('SFO', 'SAN'),
    ('SFO', 'DSM'),
    ('SAN', 'EYW')
}

solution(airports=airports, routes=routes)
