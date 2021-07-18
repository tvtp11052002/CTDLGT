n = int(input("Nhập số phần tử của bàn cờ mà bạn muốn tạo: "))

##Kiểm tra xem i, j có phải là các chỉ mục hợp lệ cho bàn cờ N * N hay không
def KT(x, y, Ban_co):
    if(x >=0 and y >=0 and x < n and y < n and Ban_co[x][y] == -1):
        return True
    return False


#In ma trận bàn cờ
def Giai_phap(n, Ban_co):
    for i in range(n):
        for j in range(n):
            print(Ban_co[i][j], end=' ')
        print()
            

def solve(n):
    '''                                                   
      Giải quyết đường đi của quân Mã bằng phương pháp
      Backtracking. 
      Trả về false nếu không có giải pháp
      Nếu không, trả về true và in giải pháp
    '''
    
    #Khởi tạo ma trận Bàn cờ
    Ban_co = [[-1 for i in range(n)] for i in range(n)]
    #DiChuyen_x và DiChuyen_y xác định nước đi tiếp theo của quân Mã
    # DiChuyen_x là giá trị tiếp theo của tọa độ x
    # DiChuyen_y là giá trị tiếp theo của tọa độ y
    DiChuyen_x = [2, 1, -1, -2, -2, -1, 1, 2]
    DiChuyen_y = [1, 2, 2, 1, -1, -2, -2, -1]
    
    #quân Mã ở vt đầu tiên
    Ban_co[3][3] = 0
    
    #Bộ đếm bước đi của quân Mã
    vi_tri = 1
    
    #Kiểm tra xem giải pháp có tồn tại hay không
    if(not solveUtil(n, Ban_co, 0, 0, DiChuyen_x, DiChuyen_y, vi_tri)):
        print("Không có giải pháp giải quyết!")
    else:
        print(Giai_phap(n, Ban_co))
        

def solveUtil(n, Ban_co, x_hientai, y_hientai, DiChuyen_x, DiChuyen_y, vi_tri):
    '''
        Dùng đệ quy để giải quyết vấn đề
    '''
    if(vi_tri == n**2):
        return True
    
    #Thử tất cả các bước di chuyển tiếp theo từ tọa độ x, y hiện tại
    for i in range(n):
        BDM_x = x_hientai + DiChuyen_x[i]
        BDM_y = y_hientai + DiChuyen_y[i]
        if(KT(BDM_x, BDM_y, Ban_co)):
            Ban_co[BDM_x][BDM_y] = vi_tri
            if(solveUtil(n, Ban_co, BDM_x, BDM_y, DiChuyen_x, DiChuyen_y, vi_tri+1)):
                return True
            
            # Backtracking
            Ban_co[BDM_x][BDM_y] = -1
    return False


print(solve(n))
