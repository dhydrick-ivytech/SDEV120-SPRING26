'''#I dont want to print the number 3, but I want to print all the other numbers from 1 to 5.

# for i in range(1,31):
#     if i %3 == 0:
#         continue
#     else:
#         print(i)    

# for i in range(1,31):
#     if i == 17:
#         break
#     else:
#         print(i)'''

# scores=[90, 85, 78, 92, 88, 60, 55, 70, 82, 95]
# for grade in scores:
#     if grade > 60:
#         print(grade)


sum = 0

n = int(input("Enter a number (or 0 to stop): "))
while n != 0:
    sum += n
    n = int(input("Enter a number (or 0 to stop): "))
print("The sum of the numbers is:", sum)    
