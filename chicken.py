print("happy chicken")
print("sad chicken")
print("dead chicken")
print("weird chicken")
A = []
summ = 0
for i in range(4):
    a = input("enter a number")
    A.append(a)
    summ += int(A[i])
print("the sum of numbers is ", sum)
print("The array", A)
print("the average ",summ/4)
