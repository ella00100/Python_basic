#prime number _ while

number = int(input("input number : "))
counts = 0
k = 1

while k <= number:
    if number % k == 0:
        counts = counts + 1
    k=k+1
if counts == 2:
    print(f'{number} is prime number!')
else:
    print(f'{number} is NOT prime number!')

#prime number _ for

number = int(input("input number : "))
counts = 0

for k in range(1,number+1):
    if number % k == 0:
        counts = counts + 1
if counts == 2:
    print(f'{number} is prime number!')
else:
    print(f'{number} is NOT prime number!')
