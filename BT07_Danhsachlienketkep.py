class Node: 
    def __init__(self, next=None, prev=None, data=None): 
        self.next = next # tham chiếu đến nút tiếp theo 
        self.prev = prev # tham chiếu đến nút trước đó
        self.data = data 
