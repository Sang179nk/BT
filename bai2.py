#Ho ten: Ng Sang
#Bai 2:
#A = [1,1,2,3,5,8,13,21,34,55,88]
#B = [1,3,5,4,7,88,66,59,40,54]
#a) In ra các phần tử trùng nhau của 2 list và lưu vào 1 list C mới
#b) Xóa các phần tử bị trùng nhau và in ra lại 2 list A,B 

listA = [1,1,2,3,5,8,13,21,34,55,88]
listB = [1,3,5,4,7,88,66,59,40,54]

#a
listC = []
print("List A:", listA)
print("List B:", listB)

print("Cac so trung nhau cua list A va list B la:")
for numberA in listA:
    for numberB in listB:
        if numberA == numberB:
            print(numberA)
            listC.append(numberA)
            
print("List C:", listC)

#b
for numberC in listC:
    for numberA in listA:
        if numberA==numberC:
            listA.remove(numberC)
    for numberB in listB:
        if numberB==numberC:
            listB.remove(numberB)
            
print("List A sau khi xoa:", listA)
print("List B sau khi xoa:", listB)