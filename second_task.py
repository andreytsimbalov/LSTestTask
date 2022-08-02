class FifoFirst:
    def __init__(self, size=10, array=None):
        if array is None:
            array = []
        self.size = size
        self.array = array[-size:]

    def add(self, value):
        self.array.append(value)
        if len(self.array) > self.size:
            self.array.pop(0)

    def pop(self):
        if len(self.array) == 0:
            return None
        return self.array.pop(0)

    def read(self):
        return self.array


class FifoSecond:
    def __init__(self, size=10, array=None):
        if array is None:
            array = []
        self.size = size
        self.array = array[-size:] + [None] * (size - len(array))
        self._write_iter = min(size, len(array)) % size
        self._read_iter = 0
        self._len = min(size, len(array))

    def _iterate_write_iter(self):
        self._write_iter = (self._write_iter + 1) % self.size

    def _iterate_read_iter(self):
        self._read_iter = (self._read_iter + 1) % self.size

    def add(self, value):
        self.array[self._write_iter] = value
        self._iterate_write_iter()
        if self._len == self.size:
            self._iterate_read_iter()
        self._len = min(self._len + 1, self.size)

    def pop(self):
        if self._len == 0:
            return None
        result_value = self.array[self._read_iter]
        self.array[self._read_iter] = None
        self._iterate_read_iter()
        self._len = max(self._len - 1, 0)
        return result_value

    def read(self):
        if self._len == 0:
            return []
        if self._read_iter < self._write_iter:
            return self.array[self._read_iter:self._write_iter]
        else:
            return self.array[self._read_iter:] + self.array[:self._write_iter]
