# EXERCISE 1
# Cube Number Test... Print out all cubed numbers up to the total value 1000. Meaning that if the cubed number is over 1000 break the loop.

def cubes():
    num = 0
    while num**3 <= 1000:
        print(num**3)
        num += 1


# EXERCISE 2
# Get first prime numbers up to 100
def primes():
    for i in range(1,  101):
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            print(i)


# EXERCISE 3
# Take in a users input for their age, if they are younger than 18 print kids,
# if they're 18 to 65 print adults, else print seniors


def ages():
    age = int(input("How old are you? "))
    if age < 18:
        print('kids')
    elif age > 65:
        print('seniors')
    else:
        print('adults')


ages()
