print("Adding even number from 1 to 100")
total = 0
even = 0
for i in range(1,101):
    if (i%2 ==0):
        even = i
        total = even + total
print(total, " is the sum of even number from 1 to 100")
