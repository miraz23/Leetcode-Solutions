# Link: https://leetcode.com/problems/implement-stack-using-queues/

class MyStack(object):

    def __init__(self):
        self.q = deque()
    
    def push(self, x):
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
    
    def pop(self):
        return self.q.popleft()
    
    def top(self):
        return self.q[0]
    
    def empty(self):
        return not self.q