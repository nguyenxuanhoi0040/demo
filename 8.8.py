#tính tiền thuê phòng của resort
loai_phong=int(input("nhập số phòng:"))
so_dem=int(input("nhập số đêm ở:"))
if loai_phong==1:
    so_tien=int(1260)
elif loai_phong==2:
        so_tien=int(1550)
elif loai_phong==3:
        so_tien=int(1830)
elif loai_phong==4:
        so_tien=int(1830)
elif loai_phong==5:
        so_tien=int(2120)
elif loai_phong==6:
        so_tien=int(2120)
elif loai_phong==7:
        so_tien=int(2540)
elif loai_phong==8:
        so_tien=int(4800)
if so_dem==2 or so_dem==3:
    so_tien_phong=so_tien*so_dem*1/4
elif so_dem>4:
        so_tien_phong=so_tien*so_dem*3/10
print("số phòng",loai_phong,"số đêm ở",so_dem,"số tiền phải trả",so_tien)


