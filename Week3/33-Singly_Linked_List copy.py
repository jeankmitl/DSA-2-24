"""Singly Linked Lits (Insert Front)"""

class DataNode:
    'data'
    def __init__(self, data = None):
        self.data = data              
        self.next = None             

class SinglyLinkedList:
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
        new_node = DataNode(data)
        new_node.next = self.head

        self.head = new_node

        self.count += 1
    
    def insert_before(self, node, data):
        new_node = DataNode(data)
        
        if self.head is None:
            print(f"Cannot insert, " + node +  " does not exist.")
            return
        
        if self.head.data == node:
            new_node.next = self.head
            self.head = new_node
            self.count += 1
            return
        
        current_pos = self.head
        while current_pos and current_pos.next:
            if current_pos.next.data == node:
                new_node.next = current_pos.next
                current_pos.next = new_node
                self.count += 1
                return
            current_pos = current_pos.next
        print(f"Cannot insert, " + node +  " does not exist.")
   
    def delete(self, data):
        if self.head is None:
            print(f"Cannot delete, " + data +  " does not exist.")
            return
        
        if self.head.data == data:
            self.head = self.head.next
            self.count -= 1
            return
        
        current_pos = self.head
        while current_pos and current_pos.next:
            if current_pos.next.data == data:
                current_pos.next = current_pos.next.next
                self.count -= 1
                return
            current_pos = current_pos.next
        print(f"Cannot delete, " + data +  " does not exist.")


def main():
    mylist = SinglyLinkedList()
    for _ in range(int(input())):
        text = input()
        condition, data = text.split(": ")
        if condition == "F":
            mylist.insert_front(data)
        elif condition == "L":
            mylist.insert_last(data)
        elif condition == "B":
            mylist.insert_before(*data.split(", "))
        elif condition == "D":
            mylist.delete(data)
        else:
            print("Invalid Condition!")
    mylist.traverse()

main()
