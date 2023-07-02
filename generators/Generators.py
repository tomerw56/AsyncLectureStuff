import random
def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1, -1, -1):
        yield my_str[i]
    print(f" Done !!!")


def none_stop_random_numbers():
    while True:
        yield random.randint(0,100)



if __name__ == '__main__':
    # For loop to reverse the string
    for char in rev_str("hello"):
        print(char)

    #random int
    rand_generator=none_stop_random_numbers()

    for iteration in range(0,10):
        print (f"random number {next(rand_generator)}")

    print (f"random number with no loop-1 {next(rand_generator)}")
    print (f"random number with no loop-2 {next(rand_generator)}")
    print (f"random number with no loop-3 {next(rand_generator)}")


    #pythonic example
    # Initialize the list
    my_list = [1, 3, 6, 10]

    a = (x ** 2 for x in my_list)
    for item in a:
        print(f"a is {item}")

