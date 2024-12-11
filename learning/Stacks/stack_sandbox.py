from Node import Node

class Stack:
    def __init__(self):
        self.top_item = None
    def peek(self):
        if self.top_item is None:
            raise AttributeError("Stack is empty. No top item to peek.")
        return self.top_item.get_value()
    def push(self, value):
        item = Node(value)
        item.set_next_node(self.top_item)
        self.top_item = item
    def pop(self):
        if self.top_item is None:
            raise AttributeError("Stack is empty. No item to pop.")  
        item_to_remove = self.top_item
        self.top_item = item_to_remove.get_next_node()
        return item_to_remove.get_value()