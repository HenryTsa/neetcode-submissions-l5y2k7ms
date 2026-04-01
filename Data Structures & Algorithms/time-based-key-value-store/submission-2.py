class TimeMap:
    # key 是"alice" , 在get 這個 timestep 最近設置的值 value
    # 我在這個 timestep 設定的 在這之前的不會得到值
    def __init__(self):
        self.dic = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        # 因為保證 set 會是小到大，所以他會是 timestamp 小 -> 大
        if key not in self.dic:
            self.dic[key] = {}
            self.dic[key][timestamp] = value
        else:
            self.dic[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        #print(self.dic,key,timestamp)
        #print(self.dic[key].keys())
        if key not in self.dic:
            return ""
        final_key = self.find_max_lower(list(self.dic[key].keys()),timestamp)
        #print(final_key)
        if final_key > timestamp:
            return ""
        #print(self.dic[key][final_key])
        #print(self.dic,timestamp)
        return self.dic[key][final_key]
    def find_max_lower(self,keys,target):
        #print(keys)
        l,r = 0,len(keys)-1
        final_idx = -1
        while l<=r:
            mid = (l+r)//2
            if keys[mid] == target:
                return keys[mid]
            elif keys[mid] < target:
                final_idx = mid
                l = mid + 1
            else:
                r = mid - 1
        #print(keys,fin)
        return keys[final_idx] 

    