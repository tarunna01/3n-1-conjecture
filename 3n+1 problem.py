num = int(input("Enter a positive number: "))
count = 0

while num > 1:
    if num % 2 == 0:
       num = num // 2
       print(num)
       count += 1
    else:
        num = (3 * num) + 1
        print(num)
        count += 1

print("Total count:", count)
