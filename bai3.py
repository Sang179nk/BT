#Ho ten: Ng Sang
#Bai 3: Cho phép người dùng nhập 1 số từ bàn phím và tính giai thừa của số đó

print("Moi ban nhap vao 1 so nguyen duong: ")
while True:
    a = int(input())
    if a<0:
        print("Nhap sai, moi ban nhap lai:")
    else:
        break
        
giaiThua = 1
for i in range(1, a+1):
    giaiThua = giaiThua * i;
print(a, "! =", giaiThua)