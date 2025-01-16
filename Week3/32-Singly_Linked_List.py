"""Singly Linked Lits (Traversal and Insert Last)"""

class DataNode:
    'data'
    def __init__(self, data = None):
        self.data = data              
        self.next = None             

class SinglyLinkedLits:
    'aa'
    def __init__(self):
        self.count = 0
        self.head = None

    def traverse(self):
        current_pos = self.head 
        if not current_pos:
            print("This is an empty list.")
            return
        
        while current_pos:
            print(current_pos.data, end='')
            
            if current_pos.next:
                print(" -> ", end='')
            current_pos = current_pos.next

    def insert_last(self, data):
        new_node = DataNode(data)

        if self.head is None:
            self.head = new_node
        else:
            current_pos = self.head
            while current_pos.next:
                current_pos = current_pos.next
            current_pos.next = new_node
    
        self.count += 1

    def insert_front(self, data):
        pass

def main():
    mylits = SinglyLinkedLits()
    for _ in range(int(input())):
        word = input()
        word = word.rstrip()

        mylits.insert_last(word)
    mylits.traverse()

main()
