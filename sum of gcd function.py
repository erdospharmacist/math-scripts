#https://oeis.org/A066862 
import math

def gcd_sum(n):
    return sum(math.gcd(k, n) for k in range(1, n + 1))

def find_divisors(bound):
    results = []
    for n in range(1, bound + 1):
        if gcd_sum(n) % n == 0:
            results.append(n)
    return results

bound = int(input("Enter an upper bound: "))
divisible_numbers = find_divisors(bound)
print(f"Numbers n up to {bound} where n divides S(n): {divisible_numbers}")