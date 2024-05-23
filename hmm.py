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




class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None



    def add_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node

    def add_after(self, data, x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.next
        if n is None:
            print("Node is not present in the Linked List.")
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node

    def add_before(self, data, x):
        if self.head is None:
            print("The Linked list is empty")
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return
        n = self.head
        while n.next is not None:
            if n.next.data == x:
                break
            n = n.next
        if n.next is None:
            print("Node is not found.")
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node

    def print_ll(self):
        if self.head is None:
            print("Linked list is empty.")
        else:
            n = self.head
            while n is not None:
                print(n.data, end='-->')
                n = n.next
            print("null")


ll1 = LinkedList()
ll1.add_begin(10)
ll1.add_begin(5)
ll1.add_end(20)
ll1.add_after(15, 10)
ll1.add_before(18, 20)
ll1.add_before(3, 5)

ll1.print_ll()
