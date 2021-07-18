def uscln(a, b):
    if (b == 0):
        return a;
    return uscln(b, a % b)
a = int(input("Nhập số nguyên dương a = "))
b = int(input("Nhập số nguyên dương b = "))
print("Ước số chung lớn nhất của", a, "và", b, "là:", uscln(a, b))
