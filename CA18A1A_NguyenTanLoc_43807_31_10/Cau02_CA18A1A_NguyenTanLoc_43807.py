"""
De thi 01
Date: 31/10/2021
Nguyen Tan Loc
"""

def CAU2():
    data=[] # list chứa các đối tương
    n = 0 # số lương mặt hàng

    class MatHang:
        def __init__(self, ma, ten, sl, dg) -> None:
            self.ma_mat_hang = ma
            self.ten_mat_hang = ten
            self.so_luong = sl
            self.don_gia = dg

        @property
        def thanh_tien(self):
            return self.so_luong * self.don_gia

    def cv23():


        # mở file
        f = open("CA18A1A_NguyenTanLoc_43807_inp.txt", mode="r", encoding="utf-8")
        # đọc dữ liệu và đưa vào class
        n = int(f.readline()) # n là số lượng mặt hàng

        for i in range (n):
             row_data = f.readline().split("|")
             mat_hang =MatHang(row_data [0], row_data[1], int(row_data[2]), int(row_data[3]))
             data.append (mat_hang) # đưa dữ liệu vào data các object

        # đóng file
        f.close()
        print("=="*10)
        print(" > Hoàn thành việc nhập dữ liệu từ file: CA18A1A_NguyenTanLoc_43807_inp.txt")

    def cv24():
        print("=="*20)
        if len(data) == 0:
            print("Bạn cần chọn nhập thông tin về mặt hàng từ file")
        else:
              # đã có thông tin, xử lý
              print("\nIn thông tin các mặt hàng:\n")
              print("==" * 20)
              for i in data:
                  print("{:<5} {:<15} {:>5} {:>10} {:>10}"
                        .format (i.ma_mat_hang, i.ten_mat_hang, i.so_luong, i.don_gia, i.thanh_tien))
        print("==" * 20)
    def cv25():
        if len(data) == 8:
            print("Bạn cần chọn nhập thông tin về mặt hàng")
        else:
             # ghi dữ liệu
             f = open("CA18A1A_NguyenTanLoc_43807_out.txt", mode="w", encoding="utf-8")

             f.write(str(len(data)) + "\n")

             for i in data:
                 s = i.ma_mat_hang + "|" +i.ten_mat_hang + "|" + str(i.so_luong) \
                    + "|" +str(i.don_gia) + "|" + str(i.thanh_tien) + "\n"
                 f.write(s)
             f.close()
             print("Hoan thanh ghi ra file:  CA18A1A_NguyenTanLoc_43807_out.txt")
             print("++"*20)

    def cau25():
        """ Hien thị mặt hàng có đơn giá cao nhất """
        print("====Mat hang dat nhat====")
        # Tin ra mặt hàng có đơn giá cao nhất
        mathangdatnhat= data[0]
        for i in data:
            if i.don_gia> mathangdatnhat.don_gia:
                mathangdatnhat = i
         # Hien thị ra mặt hàng co đơn giá cao nhất
            mathangdatnhat_str = mathangdatnhat.ma_mat_hang + "|" + mathangdatnhat.ten_mat_hang + "|" + str(mathangdatnhat.so_luong) \
                + "|" + str(mathangdatnhat.don_gia) + "|" + str(mathangdatnhat.thanh_tien)
            print(mathangdatnhat_str)
            print("=="*20)


    while True:
        print("---MENU---")
        print("1. Nhập dữ liệu từ file.")
        print("2. In dữ liệu ra màn hình .")
        print("25. In mặt hàng đơn  giá cao nhất.")
        print("3. Ghi thông tin vào file.")
        cv = input("Bạn chon công việc, bấm phím Q để thoát: ")
        if cv == "1":
            cv23()
        elif cv == "2":
            cv24()
        elif cv == "25":
            cau25()
        elif cv == "3":
            cv25()
        elif cv.upper() == "Q":
            break
if __name__=='__main__':
    CAU2()