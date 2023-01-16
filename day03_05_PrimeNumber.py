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

#prime number _ for2

number = int(input("input number : "))
counts = 0

for k in range(2,number):
    if number % k == 0:
        counts = counts + 1
if counts: #0이면 False 0이 아니면 True
    print(f'{number} is NOT prime number!')
else:
    print(f'{number} is prime number!')

#prime number _bool
number = int(input("input number : "))
is_prime = True

for k in range(2,number):
    if number % k ==0:
        is_prime = False
        break

if is_prime:
    print(f'{number} is prime number!')
else:
    print(f'{number} is NOT prime number!')