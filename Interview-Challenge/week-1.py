# Algorithm 1

for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)

# Algorithm 2

sum = 0
for n in range(1, 1000):
    if n % 3 == 0 or n % 5 == 0:
        sum += n
print("Sum = {}".format(sum))

# Algorithm 3

fib_seq = [1, 2]
new_num = 0
n = 2
fib_even_sum = 2

while new_num <= 4000000:
    new_num = fib_seq[n - 1] + fib_seq[n - 2]
    fib_seq.append(new_num)
    n += 1
    print(new_num)
    if new_num % 2 == 0:
        fib_even_sum += new_num
print("Total even sum = {}".format(fib_even_sum))

# Algorithm 4

# Find largest prime factor of a given number (big_number)
big_number = 600851475143
n = 4
known_primes = [2,3]
def is_prime(n):
    total_primes = len(known_primes)
    for i in range(0,total_primes):
        if(n % known_primes[i] == 0):
            # NOT PRIME!!
            return False
        else:
            # it might be prime, it might not. 
            # Its just not divisible by this number
            continue
    known_primes.append(n)
    return True

while n <= int(big_number / 2):
    if is_prime(n) == True:
        if big_number % n == 0:
            large_Factor = n
            print(large_Factor)
  
    n = n + 1
    
print("Largest prime factor of {} is: {}".format(big_number, large_Factor))

# Algorithm 5

nth_prime_num = 10001
counter = 2
n = 4
known_primes = [2,3]

def is_prime(n):
    total_primes = len(known_primes)
    for i in range(0,total_primes):
        if(n % known_primes[i] == 0):
            # NOT PRIME!!
            return False
        else:
            # it might be prime, it might not. 
            # Its just not divisible by this number
            continue
    known_primes.append(n)
    return True

while counter < nth_prime_num:
	if is_prime(n) == True:
		counter += 1
	n += 1
    
print("The #{} prime number is: {}".format(nth_prime_num, n - 1))