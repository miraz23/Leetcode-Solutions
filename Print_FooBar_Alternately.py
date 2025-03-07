# Link: https://leetcode.com/problems/print-foobar-alternately/

class FooBar:
    def __init__(self, n):
        self.n = n
        self.first_done = threading.Event()
        self.second_done = threading.Event()
        self.first_done.set()

    def foo(self, printFoo):
        for _ in range(self.n):
            self.first_done.wait()
            printFoo()
            self.first_done.clear()
            self.second_done.set()

    def bar(self, printBar):
        for _ in range(self.n):
            self.second_done.wait()
            printBar()
            self.second_done.clear()
            self.first_done.set()