class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
    
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_begining(self, data):
        node = Node(data, self.head) # self.head is next in Node __init__ --> (data, None)
        self.head = node # data: 5, next: None
        print(self.head.next)

    def print_out(self):
        if self.head is None:
            return('Linked list is empty')

        itr = self.head # iterator
        listr = '' # linked list string

        while itr:
            listr += str(itr.data) + '-->'
            itr = itr.next
        
        print(listr)
        
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        # Go to the last value
        while itr.next:
            itr = itr.next
        
        # Add Node(data, None) at the last value's next. -> last_value_Node(data, Node(data, None))
        itr.next = Node(data, None)
        
    
    def insert_values(self, data_list):
        self.head = None
        
        for data in data_list:
            self.insert_at_end(data)
    
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        
        return print(count)
    
    def remove_at(self, index):
        # Check if the index is within the index range 
        # if index < 0 or index >= self.get_length(): Not working
        if index < 0 | index >= self.get_length():
            raise Exception('Invalid Index')
        
        # Remove the head and move the head's next value to the head after deleting the head.
        if index == 0:
            self.head = self.head.next
            return
            
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                # Once the specified index is removed, the next value of the removed value will be the next value
                itr.next = itr.next.next
                return
            
            itr = itr.next
            count += 1
            
    def insert_at(self, index, data):
        if index < 0 | index > self.get_length():
            raise Exception('Invalid Index')
        
        if index == 0 :
            self.insert_at_begining(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            
            itr = itr.next
            count += 1
    
if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(['banana', 'mango', 'grapes', 'orange'])
    ll.remove_at(2)
    ll.print_out()
    ll.get_length()


# The order str is appended at the begining
    # ll.insert_at_begining(5)
    # ll.insert_at_begining(35)
    # ll.insert_at_begining(85)

    # 5-->
    # 35--> 5-->
    # 85--> 35--> 5-->

# The order str is appended at the end
    # ll.insert_at_end(5)
    # ll.insert_at_end(35)
    # ll.insert_at_end(85)

    # 5--> 85--> 35-->
    
# 1. The code is run for the first time, there is not next. Next is None. 
# 2. The code is run for the second time, there is next, which is the data in 1.
# 3. The code is run for the thrid time, there is next, which is the data in 2.  

# But where are they stored? --> items are stored in the memory? 
