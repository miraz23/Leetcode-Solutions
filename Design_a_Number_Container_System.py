#Link: https://leetcode.com/problems/design-a-number-container-system/

class NumberContainers:
    def __init__(self):
        self.index_number = {}
        self.number_indices = {}

    '''
        index_number           number_indices
        k | v                  k | list(v)
        2 | 10                 10 | [2, 1, 3, 5] -> SortedSet [1, 2, 3, 5]
        1 | 10                 20 | [1]                 
        3 | 10  
        5 | 10
        1 | 20            
    '''

    def change(self, index, number):
        if index in self.index_number:
            old_number = self.index_number[index]
            self.number_indices[old_number].discard(index)
            if not self.number_indices[old_number]:
                del self.number_indices[old_number]

        self.index_number[index] = number
        if number not in self.number_indices:
            self.number_indices[number] = SortedSet()
        self.number_indices[number].add(index)

    def find(self, number):
        if number not in self.number_indices:
            return -1
        return self.number_indices[number][0]