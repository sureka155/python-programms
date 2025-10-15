class MaxHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def insert(self, job):
        self.heap.append(job)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, i):
        while i > 0 and self.heap[self.parent(i)][0] < self.heap[i][0]:
            self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i = self.parent(i)

    def extract_max(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_down(self, i):
        largest = i
        l = self.left(i)
        r = self.right(i)

        if l < len(self.heap) and self.heap[l][0] > self.heap[largest][0]:
            largest = l
        if r < len(self.heap) and self.heap[r][0] > self.heap[largest][0]:
            largest = r

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self._heapify_down(largest)

    def peek_max(self):
        if not self.heap:
            return None
        return self.heap[0]

    def display_tree(self):
        if not self.heap:
            print("Heap is empty")
            return

        n = len(self.heap)

        # Calculate levels without math
        level = 0
        total_nodes = 0
        while total_nodes < n:
            level += 1
            total_nodes += 2 ** (level - 1)

        max_width = 80  # max width for printing

        index = 0
        for lvl in range(level):
            nodes_at_level = 2 ** lvl
            space_between = max_width // (nodes_at_level + 1)
            line = ""
            for i in range(nodes_at_level):
                if index >= n:
                    break
                priority, job = self.heap[index]
                node_str = f"{priority}:{job}"
                line += node_str.center(space_between)
                index += 1
            print(line)
        print()

# Example usage
scheduler = MaxHeap()

scheduler.insert((5, "JobA"))
scheduler.insert((3, "JobB"))
scheduler.insert((17, "JobC"))
scheduler.insert((10, "JobD"))
scheduler.insert((84, "JobE"))
scheduler.insert((19, "JobF"))
scheduler.insert((6, "JobG"))
scheduler.insert((22, "JobH"))
scheduler.insert((9, "JobI"))

print("Heap displayed as a binary tree:")
scheduler.display_tree()
