from sys import argv

class Ban_co_NxN(object):
    def __init__(self, so_luong_quan_hau):
    # Khởi tạo các giá trị bắt đầu cho bàn cờ NxN
        self.n_size = so_luong_quan_hau
        self.vi_tri_quan_hau = [0] * so_luong_quan_hau
        self.cot_j = 0
        self.cot = [True] * so_luong_quan_hau
        diagonal_attack_lines_on_board = (2 * so_luong_quan_hau) - 1
        self.duong_cheo_len = [True] * diagonal_attack_lines_on_board
        self.duong_cheo_xuong = [True] * diagonal_attack_lines_on_board
        self.so_vi_tri_quan_hau = 0
        self.so_luong_giai_phap = 0

    def chi_so_tan_cong_theo_duong_cheo(self, hang_i):
    # Tính chỉ số cho một động tác tấn công theo đường chéo hướng lên cho hàng nhất định trong cột hiện tại 
        return (self.n_size - 1 + self.cot_j - hang_i)

    def chi_so_tan_cong_theo_duong_thang(self, hang_i):
    # Tính chỉ số cho một động tác tấn công theo đường thẳng xuống cho hàng nhất định trong cột hiện tại 
        return (self.cot_j + hang_i)

    def o_vuong_con_trong(self, hang_i):
    # Kiểm tra xem còn trống và có thể đặt quân hậu trên bàn cờ ở hàng nhất định trong cột hiện tại hay không 
        return (self.cot[hang_i] and
                self.duong_cheo_len[self.chi_so_tan_cong_theo_duong_cheo(hang_i)] and
                self.duong_cheo_xuong[self.chi_so_tan_cong_theo_duong_thang(hang_i)])

    def dat_quan_hau(self, hang_i):
    # Đặt một quân hậu trên bàn cờ ở hàng nhất định trong cột hiện tại 
        self.vi_tri_quan_hau[self.cot_j] = hang_i
        self.cot[hang_i] = False
        self.duong_cheo_len[self.chi_so_tan_cong_theo_duong_cheo(hang_i)] = False
        self.duong_cheo_xuong[self.chi_so_tan_cong_theo_duong_thang(hang_i)] = False
        self.cot_j += 1
        self.so_vi_tri_quan_hau += 1

    def loai_bo_quan_hau(self, hang_i):
    # Loại bỏ quân hậu khỏi bàn cờ tại hàng nhất định trong cột hiện tại 
        self.cot_j -= 1
        self.cot[hang_i] = True
        self.duong_cheo_len[self.chi_so_tan_cong_theo_duong_cheo(hang_i)] = True
        self.duong_cheo_xuong[self.chi_so_tan_cong_theo_duong_thang(hang_i)] = True

    def vi_tri_tiep_theo_cua_quan_hau(self):
    # Hàm đệ quy để tìm vị trí quân hậu hợp lệ trên bàn cờ. Khi bảng NxN có N quân hậu được đặt trên đó, bộ đếm giải pháp sẽ tăng lên 
        for hang_i in range(0, self.n_size):
            if self.o_vuong_con_trong(hang_i):
                self.dat_quan_hau(hang_i)
                if self.cot_j == self.n_size:
                    self.so_luong_giai_phap += 1
                else:
                    self.vi_tri_tiep_theo_cua_quan_hau()
                self.loai_bo_quan_hau(hang_i)


def so_luong_giai_phap_hop_le(so_luong_quan_hau):
    # Tính số quân hậu được đặt trên bàn cờ trong khi tìm tất cả các nghiệm hợp lệ cho một số quân hậu nhất định.
    # Sau đó, số lượng vị trí và giải pháp dành cho quân hậu sẽ được trả về 
    tong_so_vi_tri_quan_hau = 0
    tong_so_luong_giai_phap = 0 if so_luong_quan_hau != 1 else 1
    # Hai biến tiếp theo được sử dụng để phân chia không gian tìm kiếm chỗ trống của bàn cờ vua 
    # bàn cờ làm đôi bằng cách tận dụng sự đối xứng trong bàn cờ 
    so_luong_cac_cap_quan_hau = so_luong_quan_hau // 2
    hang_giua = so_luong_cac_cap_quan_hau + (so_luong_quan_hau % 2)
    for hang_i in range(0, hang_giua):
        ban_co_vua = Ban_co_NxN(so_luong_quan_hau)
        ban_co_vua.dat_quan_hau(hang_i)
        ban_co_vua.vi_tri_tiep_theo_cua_quan_hau()
        tong_so_vi_tri_quan_hau += ban_co_vua.so_vi_tri_quan_hau
        tong_so_luong_giai_phap += ban_co_vua.so_luong_giai_phap
        # Câu lệnh if dưới đây sẽ chỉ sai khi hàng i là chỉ số của hàng giữa cho một bàn cờ có số hàng lẻ 
        if hang_i != so_luong_cac_cap_quan_hau:
            tong_so_luong_giai_phap += ban_co_vua.so_luong_giai_phap
    return (tong_so_vi_tri_quan_hau, tong_so_luong_giai_phap)


def main(argv,so_luong_quan_hau):
    # Bàn cờ được khởi tạo và thuật toán giải được N quân hậu
    # Một chuỗi được in ra dòng lệnh với số đếm cho số lượng vị trí nữ hoàng và các giải pháp 
    so_luong_quan_hau = so_luong_quan_hau
    if len(argv) != 0 and int(argv[0]) > 0:
        so_luong_quan_hau = int(argv[0])
    so_vi_tri_quan_hau, so_luong_giai_phap = \
        so_luong_giai_phap_hop_le(so_luong_quan_hau)
    result_string = "\nĐã thử nghiệm %d vị trí đặt quân hậu và " \
                    "tìm được %d giải pháp cho vấn đề đặt %d quân hậu hợp lệ"

    print((result_string) % (so_vi_tri_quan_hau, so_luong_giai_phap, so_luong_quan_hau))


# Chương trình bắt đầu
n = int(input("Nhập số quân hậu bạn muốn thử: "))
main(argv[1:],n)
