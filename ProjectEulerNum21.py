#Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
#If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
#For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
#The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#Evaluate the sum of all the amicable numbers under 10000.
import math

amicable_pairs = []
answer = 0

def amicable_num(n): # determines if a number is half of a pair of amicable numbers
    sum_divisors = 1
    sum_divisors_2 = 1
    for i in range(2,math.ceil(math.sqrt(n)) + 1):
        if i * i == n:
            sum_divisors += i
        elif n % i == 0:
            sum_divisors += i
            sum_divisors += int(n/i)
    for k in range(2, math.ceil(math.sqrt(sum_divisors)) + 1):
        if k * k == sum_divisors:
            sum_divisors_2 += k
        elif sum_divisors % k == 0:
            sum_divisors_2 += k
            sum_divisors_2 += int(sum_divisors / k)
    if sum_divisors_2 == n:
        if sum_divisors != n: # This accounts for perfect numbers and prevents them from being appended.
            amicable_pairs.append(n)

for i in range(2,10001):
    amicable_num(i)

for k in amicable_pairs:
    answer += k

print(answer)