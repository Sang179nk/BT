#Ho ten: Ng Sang
#Bai 1:
#A = [1,1,2,6,8,9,4,5,6,45,34,66,44,37,78]
#Viết 1 chương trình in ra các số nhỏ hơn 30 và lưu các số đó vào 1 list khác

listA = [1,1,2,6,8,9,4,5,6,45,34,66,44,37,78]

#a
listResult = []

print("List A:", listA)
print("Cac so nho hon 30 trong list A:")
for number in listA:
    if number < 30:
        print(number)
        listResult.append(number) 

print("List result:", listResult)

    
#b
print("Moi ban nhap vao 1 so:")
a = int(input())
print("Cac so lon hon", a, "trong list A la:")
for number in listA:
    if(number > a):
        print(number)
