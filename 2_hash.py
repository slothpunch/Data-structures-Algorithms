class HashTable():
    def __init__(self):
        self.MAX = 10
        # self.arr = [None for i in range(self.MAX)]
        # Change None to an array for each value as I am going to store key-value pairs. 
        self.arr = [[] for i in range(self.MAX)]
    
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    # t['march 9'] (key) = 12 (val)
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        
        # idx - number, element - value 
        for idx, element in enumerate(self.arr[h]):
            if (len(element) == 2) & (element[0] == key): # e.g. if element[0] is 'march 9' and key is also 'march 9'
                self.arr[h][idx] = (key, val) # Change the current key and value with the new key and value
                found = True
                break
            
        if not found: # If True
            # Append key and val as a tuple
            self.arr[h].append((key, val))

t = HashTable()
t['march 6'] = 120
t['march 17'] = 459
t['march 6'] = 78
# t['march 8'] = 67
# t['march 9'] = 4

t.arr