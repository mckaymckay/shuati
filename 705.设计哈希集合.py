#
# @lc app=leetcode.cn id=705 lang=python3
#
# [705] 设计哈希集合
#


# @lc code=start
class MyHashSet:
    def __init__(self):
        self.buckets = 1009
        self.table = [[] for _ in range(self.buckets)]
        """
        Initialize your data structure here.
        """

    # 分桶函数
    def hash(self, key):
        return key % self.buckets

    def add(self, key: int) -> None:
        hashkey = self.hash(key)

        if key not in self.table[hashkey]:
            self.table[hashkey].append(key)

    def remove(self, key: int) -> None:
        hashkey = self.hash(key)
        
        if key in self.table[hashkey]:
            self.table[hashkey].remove(key)
            

    def contains(self, key: int) -> bool:
        hashkey = self.hash(key)

        return key in self.table[hashkey]
        """
        Returns true if this set contains the specified element
        """


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
# @lc code=end
