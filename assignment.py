# Prime Number and composite number
number = int(input('Enter the number: '))
if number < 2:
    print(f'{number} is not a prime number.')
else:
    for i in range(2, int(number ** .5)+1):
        if number % i == 0:
            print(f'{number} is a composite number.')
            break
    else:
        print(f'{number} is a prime number.')

# Quotient and Remainder:
n1 = int(input('Dividend: '))
n2 = int(input('Divisor: '))
quotient = n1 // n2
remainder = n1 % n2
print(f'Quotient is {quotient} and reminder is {remainder}')

# Prime number in a particular range:
number = int(input('Enter the number: '))
print(2)
for i in range(3, number+1):
    for j in range(2, int(i ** .5) + 1):
        if i % j == 0:
            break
    else:
        print(i)


# prime factors
def prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    for i in range(3, int(n ** .5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i

    if n > 2:
        factors.append(n)
    return factors


number = int(input())
print(prime_factors(number))


# gcd & lcm
a, b = map(int, input().split())


def prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    for j in range(3, int(n ** .5) + 1, 2):
        while n % j == 0:
            factors.append(j)
            n //= j

    if n > 2:
        factors.append(n)
    return factors


prime_factors_a = prime_factors(a)
prime_factors_b = prime_factors(b)

prime_factors_a_no_d = list(set(prime_factors_a))
prime_factors_b_no_d = list(set(prime_factors_b))

whole_list = []
for i in prime_factors_a_no_d:
    whole_list.append(i)
    power_of_a_b = [prime_factors_a.count(i), prime_factors_b.count(i)]
    whole_list.append(power_of_a_b)

for i in prime_factors_b_no_d:
    if i not in whole_list:
        whole_list.append(i)
        power_of_a_b = [prime_factors_a.count(i), prime_factors_b.count(i)]
        whole_list.append(power_of_a_b)

gcd = 1
lcm = 1
for i in range(0, len(whole_list), 2):
    count_for_gcd = whole_list[i] ** min(whole_list[i+1])
    count_for_lcm = whole_list[i] ** max(whole_list[i+1])
    gcd *= count_for_gcd
    lcm *= count_for_lcm

print(f"GCD of {a} and {b} is {gcd}")
print(f"LCM of {a} and {b} is {lcm}")
print(f"({gcd} X {lcm}) = {gcd * lcm}")
print(f"({a} X {b}) = {a * b}")
print(f"Proved ({a} X {b}) = ({gcd} X {lcm})")
