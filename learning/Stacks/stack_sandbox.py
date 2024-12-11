class Stack:
    def __init__(self):
        self.top_item = None

    def peek(self):
        if self.top_item is None:
            raise AttributeError("Stack is empty. No top item to peek.")
        return self.top_item.get_value()