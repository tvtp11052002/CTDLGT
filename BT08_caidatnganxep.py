class Stack:
    def __init__(self):
        self.items = []
        print("- Đã tạo danh sách -")

    def Tình_trạng_danh_sách(self):
        """
            Kiểm tra xem danh sách có phần tử hay chưa
            Trả về True nếu có phần tử và False nếu không có phần tử nào
        """
        length = len(self.items)
        if length == 0:
            print("Danh sách trống")
        else:
            print("Danh sách hàng chờ có " + str(length) + " phần tử")

    def Số_lượng_phần_tử(self):
        """
            Số lượng phần tử trong hàng chờ
        """ 
        print(len(self.items))
    
    def Thêm_phần_tử(self, item):
        """
            Thêm phần tử vào hàng chờ
        """ 
        self.items.append(item)
        print(" +\n Đã thêm '{}' vào danh sách\n Danh sách hiện có {} phần tử\n".format(item, len(self.items)))

    def Lấy_phần_tử(self):
        """
            Lấy phần tử ra hàng chờ
        """ 
        item = self.items.pop()
        print(" -\n Đã lấy '{}' ra khỏi danh sách\n Danh sách hiện có {} phần tử\n".format(item, len(self.items)))

if __name__ == "__main__":
    a = Stack()     # Tạo danh sách với tên biến là a

    a.Tình_trạng_danh_sách()    # Xem tình trạng danh sách
	
    a.Thêm_phần_tử(4)
    a.Thêm_phần_tử('dog')
    a.Thêm_phần_tử(True)
    a.Thêm_phần_tử(8.4)

    a.Lấy_phần_tử()
    a.Lấy_phần_tử()
    a.Lấy_phần_tử()
