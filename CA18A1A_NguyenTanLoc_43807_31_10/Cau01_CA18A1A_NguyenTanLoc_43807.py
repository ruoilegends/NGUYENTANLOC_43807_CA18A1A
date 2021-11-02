"""
De thi 01
Date: 31/10/2021
Nguyen Tan Loc
"""


def Cau1():
    def snt(n):
        """Check so nguyen to"""
        f = True
        for j in range(2, n):
            if n % j == 0:
                f = False
                break
        return f
    def in_snt(a=30, b=200):
        print("Danh sach cac so nguyen to: ")
        """Kiem tra so nguyen to trong khoang tu a den b"""
        for i in range(a, b + 1):
            if snt(i):
                print(i, end= " ")
                print()
    #thuc thi tim so nguyen to
    in_snt(30, 200)


if __name__ == '__main__':
    Cau1()
