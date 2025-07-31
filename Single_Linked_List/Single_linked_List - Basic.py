
#**single linked list
# 
# This represents a very basic SLL in Python
# We have two main classes, node and single_linked_list
#
# **

#node
#This is the basic building block of the SLL, a node contains data and a pointer to the next node
#That's it, it doesn't need to be complicated
class node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __str__(self):
        return str(self.data)
    
    def set_data(self, data):
        self.data = data
        
    def set_next(self, next):
        self.next = next
        
#single_linked_list
#This is the container class for the SLL
#It contains a pointer to the head of the SLL
#It also contains some basic functions to insert and print the SLL - These functions will be expanded on later
class single_linked_list:
    def __init__(self):
        self.head = node(0)
        
    def get_head(self):
        return self.head
    
    def set_head(self, head):
        self.head = head
    #insert
    #this can be done at the head of the SLL or Tail
    #for simplicity, this is a head insert
    def insert(self, data):
        new_node = node(data)
        new_node.next = self.head
        self.head = new_node
        
    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next
            
            
            
#basic code test here
int_list = single_linked_list()
int_list.insert(3)
int_list.insert(2)
int_list.insert(1)
int_list.print_list()

print("--------------------------")

misc_list = single_linked_list()
misc_list.insert('a')
misc_list.insert(2)
misc_list.insert("hello")
misc_list.print_list()