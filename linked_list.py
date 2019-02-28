class LinkedList:
    
    def __init__(self,head = None):
        self.head = head
        self.size = 0
    def get_size(self):
        return self.size
    def add_node(self,data):
        newNode = Node(data,self.head)
        self.head = newNode
        self.size+=1
        return True
    def print_node(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.get_next()
    def remove_node(self):
        curr=self.head
        self.head=curr.get_next()
        self.size-=1
        print("item deleted",curr.get_data())

class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next_node
    def set_next(self,new_next):
        self.next_node = new_next

List1 = LinkedList()
print("Inserting")
print(List1.add_node(5))
print(List1.add_node(15))
print(List1.add_node(25))
print("Printing")
List1.print_node()
print("Size")
print(List1.get_size())
print("deleting")
List1.remove_node()
print("Size after deletion")
print(List1.get_size())
