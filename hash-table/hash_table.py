class hash_item:
    def __init__(self,key,value):
        self.key = key
        self.value = value
    def __str__(self):
        if self is None:
            return ""
        return f"{self.key,self.value}"
class hash_table:
    def __init__(self):
        self.size=8
        self.items=0
        self.memory=[None] * self.size 
        self.n_collision=0       
    def hash(self,k):
        sum=0
        m=self.size
        for c in k:
            sum+=ord(c)
        return sum%m
    def add(self,key,value):
        h = self.hash(key)
        while self.memory[h] is not None and self.memory[h].key != key:
            h = (h+1)%self.size
            self.n_collision+=1
        self.memory[h] = hash_item(key,value)
        self.items+=1
        if self.items/self.size > 0.6:
            self.resize()
    def exists(self,key):
        h = self.hash(key)
        n_looked = 1
        while self.memory[h] is not None and self.memory[h].key != key:
            h = (h+1)%self.size
            n_looked+=1
            if n_looked >= self.size:
                return False
        if self.memory[h] is None:
            return False
        return True
    def get(self,key):
        h = self.hash(key)
        n_looked = 1
        while self.memory[h] is not None and self.memory[h].key != key:
            h = (h+1)%self.size
            n_looked+=1
            if n_looked >= self.size:
                return None
        if self.memory[h] is None:
            return None
        return self.memory[h].value
    def remove(self,key):
        h = self.hash(key)
        n_looked = 1
        while self.memory[h] is not None and self.memory[h].key != key:
            h = (h+1)%self.size
            n_looked+=1
            if n_looked >= self.size:
                return 
        self.memory[h] = None
    def resize(self):
        self.size=self.size*2
        new_memory = [None] * self.size
        for m in self.memory:
            if m is not None:
                new_memory[self.hash(m.key)]=m
        self.memory = new_memory

    def __str__(self):
        to_str=""
        for m in self.memory:
            to_str+=str(m)+" , "
        return to_str

def test_hash_table():
    h=hash_table()
    h.add("jack",1)
    h.add("james",3)
    print(h)
    h.add("kay",4)
    h.add("joe",5)
    h.add("carl",6)
    h.add("jojo",7)
    h.add("jiji",8)
    print(h)
    print(h.n_collision)
    assert h.exists("kay") == True
    h.remove("kay")
    assert h.exists("kay") == False
    assert h.exists("bobo") == False
    assert h.get("jojo") == 7
    assert h.get("kay") == None
    print(h)
test_hash_table()

        


