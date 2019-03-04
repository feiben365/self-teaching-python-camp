# the sum of 1 to 100
sum = 0
for i in range(1,101):
    sum += i
print(sum)

# multiplication table
for a in range(1, 10):
    for b in range(1, a+1):
        print("%d*%d=%d\t"%(a,b,a*b), end="")
    print("")




# while loop condition i % 7 == 0：
i = 0  
while i <= 100:   
    i += 1
    if i%7 ==0: 
        print(i) 


# even odd while loop
i = int(input("Please enter a number")) 
while i <= 100:   
    i += -1
    if i == 0:
        break
    if i%2 == 0: 
        print(i, "is an even number") 
    if i%2 == 1:
        print(i, "is an odd number")
