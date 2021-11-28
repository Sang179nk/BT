#Ho ten: Ng Sang
#Bai 4:  Viết một chương trình yêu cầu người dùng nhập 1 số nguyên dương n
#        từ bàn phím và tính tổng từng chữ số

print("Moi ban nhap vao 1 so nguyen duong: ")
while True:
    a = int(input())
    if a<0:
        print("Nhap sai, moi ban nhap lai:")
    else:
        break

tongCacChuSo = 0
thuong = a
while True:
    du = thuong%10
    thuong = int(thuong/10)
    tongCacChuSo += du
    if thuong==0:
        break
print("Tong cac chu so cua so", a, "la:", tongCacChuSo)