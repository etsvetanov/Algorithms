from typing import Optional


class MinHeap:
    def __init__(self):
        self.heap = [None]

    def insert(self, node):  # O(log n)
        self.heap.append(node)

        if len(self.heap) > 1:
            current = len(self.heap) - 1

            while current > 1 and self.heap[current // 2] > self.heap[current]:
                self.heap[current // 2], self.heap[current] = self.heap[current], self.heap[current // 2]
                current = current // 2

    def _swap(self, source, target):
        self.heap[source], self.heap[target] = self.heap[target], self.heap[source]
        return target

    @staticmethod
    def _get_children(index):
        return index * 2, index * 2 + 1

    def __len__(self):
        return len(self.heap)

    def _get_smallest_child(self, parent):
        left, right = self._get_children(parent)

        if right <= len(self):
            if self.heap[parent] < self.heap[left] or self.heap[parent] < self.heap[right]:
                return left if self.heap[left] < self.heap[right] else right
        elif left <= len(self):
            if self.heap[parent] > self.heap[left]:
                return left

        return None

    def remove(self) -> Optional[int]:
        if len(self.heap) > 2:
            smallest = self.heap[1]

            self.heap[1] = self.heap.pop()

            if len(self.heap) == 3:
                if self.heap[1] > self.heap[2]:
                    self._swap(1, 2)

                return smallest

            current = 1

            while True:
                smallest_child = self._get_smallest_child(current)

                if not smallest_child:
                    break

                current = self._swap(current, smallest_child)

            return smallest
        elif len(self.heap) == 2:
            self.heap.pop(1)
        else:
            return None
