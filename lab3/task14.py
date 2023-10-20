def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def next_prime(num):
    while True:
        num += 1
        if is_prime(num):
            return num

while True:
    a = int(input("Enter a number: "))
    if is_prime(a):
        print(f"{a} is a prime number.")
    else:
        print(f"{a} is not prime. The next prime number is {next_prime(a)}")
    if input("Do you want to continue testing (yes/no)? ").strip().lower() != "yes":
        break