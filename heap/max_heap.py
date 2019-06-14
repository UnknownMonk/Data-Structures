class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        index = len(self.storage) - 1
        self._bubble_up(index)

    def delete(self):
        self.storage[0], self.storage[-1] = self.storage[-1], self.storage[0]
        deletedValue = self.storage.pop(-1)
        self._sift_down(0)
        return deletedValue

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):

        while index > 0:

            parent = (index - 1) // 2

            if self.storage[index] > self.storage[parent]:

                self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]

                index = parent

            else:

                break

    def _sift_down(self, index):
        left = (index * 2) + 1
        right = (index * 2) + 2
        largest = index
        if len(self.storage) > left and self.storage[largest] < self.storage[left]:
            largest = left
        if len(self.storage) > right and self.storage[largest] < self.storage[right]:
            largest = right
        if largest != index:
            self.storage[index], self.storage[largest] = self.storage[largest], self.storage[index]
            self._sift_down(largest)
