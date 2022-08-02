def sort(array):
    MINIMUM = 32

    def _find_minrun(n):
        r = 0
        while n >= MINIMUM:
            r |= n & 1
            n >>= 1
        return n + r

    def _insertion_sort(array, left, right):
        for i in range(left + 1, right + 1):
            element = array[i]
            j = i - 1
            while element < array[j] and j >= left:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = element
        return array

    def _merge(array, l, m, r):
        left_array_length = m - l + 1
        right_array_length = r - m
        left_array = array[l: l + left_array_length]
        right_array = array[m + 1: m + 1 + right_array_length]

        i = 0
        j = 0
        k = l
        while j < right_array_length and i < left_array_length:
            if left_array[i] <= right_array[j]:
                array[k] = left_array[i]
                i += 1
            else:
                array[k] = right_array[j]
                j += 1
            k += 1
        while i < left_array_length:
            array[k] = left_array[i]
            k += 1
            i += 1
        while j < right_array_length:
            array[k] = right_array[j]
            k += 1
            j += 1

    array_len = len(array)
    size = minrun = _find_minrun(array_len)

    for start in range(0, array_len, minrun):
        end = min(start + minrun - 1, array_len - 1)
        _insertion_sort(array, start, end)

    while size < array_len:
        for left in range(0, array_len, 2 * size):
            mid = min(array_len - 1, left + size - 1)
            right = min((left + 2 * size - 1), (array_len - 1))
            _merge(array, left, mid, right)
        size = 2 * size

    return array
