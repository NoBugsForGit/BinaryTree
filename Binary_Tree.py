from math import log


# 搜索算法需要改良

class BinaryTree:
    """
    二叉树:
    data储存数据;
    parent储存父节点;
    left,right储存左/右节点;
    count储存序号;
    layer为层数
    """

    def __init__(self, data, count=1, parent=None):
        self.data = data
        self.parent = parent
        self.count = count
        self.left = None
        self.right = None
        self.layer = int(log(self.count, 2) )+ 1

    def insert_left(self, data):
        self.left = BinaryTree(data, self.count * 2, self)

    def insert_right(self, data):
        self.right = BinaryTree(data, self.count * 2 + 1, self)

    def delete(self):
        if self.parent.left == self:
            self.parent.left = None
        else:
            self.parent.right = None
        del self

    def search(self, count):
        # 根据count的值搜索对象
        if self.parent is not None:
            p = self.parent
            while p.parent is not None:
                p = p.parent
        else:
            p = self
        # 此时p为首节点
        way = []  # 存储从首节点到搜索节点的路线信息(倒序),每个元素都为bool,True为左,False为右;
        while not count == 1:
            if count % 2 == 0:
                way.append(True)
            else:
                way.append(False)
            count = count // 2
        for i in range(-1, -len(way) - 1, -1):
            if way[i]:
                p = p.left
            else:
                p = p.right
            if p is None:
                raise KeyError("The object which you search is not found!")
        return p
