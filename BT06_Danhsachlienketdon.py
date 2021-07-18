class Node:
    
    #Bắt đầu khởi tạo đối tượng node
    def __init__(self, data):
        self.data = data #Gán dữ liệu
        self.next = None 
class LinkedList: #Bắt đầu tạo 1 danh sách liên kết
    def __init__(self): 
        self.head = None

        
if __name__=='__main__': 
    
    #Bắt đầu với 1 danh sách trống
    listrong = LinkedList()
    
    #Bắt đầu thêm các giá trị vào
    listrong.head = Node(1)
    thuhai = Node(2)
    thuba = Node(3)
    
    #bắt đầu liên kết
    listrong.head.next = thuhai
    listrong.head.next = thuba
    #Như vậy danh sách đã được liên kết với nhau và kết thúc ở vị trí thuba(Null)
