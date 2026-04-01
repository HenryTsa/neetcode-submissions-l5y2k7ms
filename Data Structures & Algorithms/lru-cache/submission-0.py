class Node:
    def __init__(self,key,value) -> None:
        self.key , self.val = key,value
        self.prev,self.nxt = None,None
        return  
        
class LRUCache:
    def __init__(self, capacity: int):
        self.dic = {}
        self.cap = capacity
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.nxt = self.tail
        self.tail.prev = self.head

    def remove(self,Node):
        Node.prev.nxt = Node.nxt
        Node.nxt.prev = Node.prev
    # 插入我們的到最 tail，tail 當作 dummy。
    def insert(self,Node):
        prev , nxt = self.tail.prev , self.tail
        prev.nxt = nxt.prev = Node
        Node.nxt , Node.prev = nxt , prev
    def get(self, key: int) -> int:
        if key  in self.dic:
            self.remove(self.dic[key])
            self.insert(self.dic[key])
            return self.dic[key].val
        
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.remove(self.dic[key])
        self.dic[key] = Node(key,value)
        self.insert(self.dic[key])

        if len(self.dic) > self.cap:
            lru = self.head.nxt
            self.remove(lru)
            del self.dic[lru.key]

