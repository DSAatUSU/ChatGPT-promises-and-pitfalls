class stack:
    data = []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def empty(self):
        return len(self.data) == 0
