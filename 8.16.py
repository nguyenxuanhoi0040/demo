def UCLN_1(a, b):
    if b == 0:
        return a
    return UCLN_1(b, a % b)


def UCLN_2(a, b):
    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b
    return b


a = int(input('Nhap vao so nguyen duong a = '))
b = int(input('Nhao vao so nguyen duong b = '))

print('Uoc so chung lon nhat cua a va b la: ', UCLN_1(a, b))
print('Uoc so chung lon nhat cua a va b la: ', UCLN_2(a, b))