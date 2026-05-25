class hash_table:
    def __init__(self,size):
        self.size=size
        self.table=[[]for _ in range(size)]
    def hash_function(self,key):
        return key % self.size
    def insert(self,key):
        index=self.hash_function(key)
        self.table[index].append(key)
        print(f"insert{key} at index{index}")
    def search(self,key):
        index=self.hash_function(key)
        if key in  self.table[index]:
            print(f"key{key} found at index{index}")
        else:
            print("key not found")
    def display(self):
        print("hash function:")
        for i,bucket in enumerate(self.table):
            print(f"index{i}:{bucket}")
ht=hash_table(10)
ht.insert(23)
ht.insert(43)
ht.insert(13)
ht.insert(33)
ht.insert(22)
ht.display()
ht.search(33)