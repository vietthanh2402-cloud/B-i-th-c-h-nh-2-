 # bài 2
chuoi = input("Nhập một chuỗi: ")
if chuoi == chuoi[::-1]:
    print(f"đối xứng.")
else:
    print(f" không đối xứng")



 # bài 4
s = input("Nhập câu: ")

kết_quả = s.title()

print("Kết quả:", kết_quả)

# bài 5

s = input("Nhập chuỗi: ")
kết_quả = s.replace("Python", "AI")
print("Kết quả:", kết_quả)


# bài 6
s = input("Nhập câu: ")
print(*s.split(), sep="-")

# bài 7

cau = input("Nhập câu: ")
so_tu = len(cau.split())
print("Số lượng từ trong câu là:", so_tu)


# bài 8

s = (input("nhập vào danh sách số nguyên:")).split()
danh_sach = list(map(int, s))
tong = sum(danh_sach)
trung_bình  = tong/len(danh_sach)
so_lon = max(danh_sach)
print(f" tồng là {tong}, số trung bình là {trung_binh}, số lớn nhất là {so_lon}" )

# bài 9

s = input("nhập vào danh danh các số").split()
cac_so = [int(x) for x in s]
danh_sach =[]
for x in cac_so:
    if x not in danh_sach:
        danh_sach.append(x)
print("Danh sách sau khi loại bỏ phần tử trùng:", danh_sach_moi)


# bài 10

s = input("nhập vào danh danh ").split()
danh_sach = list(map(int, s))
danh_sach_dao = danh_sach[::-1]
print(danh_sach_dao)


# bài 11
s = input("nhập vào danh danh các số").split()
cac_so = [int(x) for x in s]
tong = 0
for x in cac_so:
    if x % 2 ==0:
         tong += x
print(tong)


# bài 13

s1 = input("Nhập danh sách thứ nhất: ").split()
s2 = input("Nhập danh sách thứ hai: ").split()
ds1 = [int(x) for x in s1]
ds2 = [int(x) for x in s2]
ds_gop = ds1 + ds2
ds_gop.sort()
print(ds_gop)

# bài 14
s = input("nhập vào danh danh số  ").split()
danh_sach = list(map(int, s))
n = [x for x in danh_sach if x > 10 ]
print(n)


