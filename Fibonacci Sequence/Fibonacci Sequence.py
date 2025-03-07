def ans_valid(ans):
    while ans not in ["N","Y"]:
        ans = input("Invalid input. Please enter either Y or N")

    return ans


def int_valid(num):
    while not num.lstrip("-").isdigit():
        num = input("Invalid input. Please enter an integer.")
    return int(num)


def term_valid(num):
    num = int_valid(num)

    while num < 0:
        num = int_valid(input("Invalid input. Please enter a number greater than or equal to 0."))

    return num


ans = "INVALID"
sequence = [0,1]
terms = 0

print("Welcome to the Fibonacci Sequence!")
print("The Fibonacci Sequence is a series of numbers in which each number is the sum of the two that precede it.")
print("\n")

ans = ans_valid(input("Would you like to print out the sequence? (Y/N)"))

while ans == "Y":
    terms = term_valid(input("How many terms would you like to print?"))

    if terms == 0:
        pass
    elif terms == 1:
        print("0 at number f(0)")
    elif terms == 2:
        print("0 at number f(0)")
        print("1 at number f(1)")
    else:
        for x in range(0, terms-2):
            sequence.append(sequence[-2] + sequence[-1])

        for num in range(0,len(sequence)):
            print("{} at number f({})".format(sequence[num], num))

    ans = ans_valid(input("Would you like to print out more elements of the sequence? (Y/N)"))

    sequence = [0,1]




