#chương trình kiểm tra năm nhuận 
year=int(input("nhập năm ="))
if (year % 4==0 and year % 100!=0)or year % 400 ==0:
    print("năm",year,"là năm nhuận")
else:
    print("năm",year,"không phải năm nhuận")

