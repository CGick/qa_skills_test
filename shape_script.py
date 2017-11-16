
def print_shape(lines):
    """
    Prints out a right facing arrow of '#'s with a given number of lines
    to include.

    :param lines: Integer number of lines to include in the shape
    """
    odd = is_odd(lines)
    mid_num = find_middle(lines, odd)
    for line in range(0, mid_num + 1, 1):
        print('#' * line)
    if odd:
        for line in range(mid_num - 1, 0, -1):
            print('#' * line)
    else:
        for line in range(mid_num, 0, -1):
            print('#' * line)

def find_middle(number, odd):
    """
    Finds the middle number for use in a pattern.

    :param number: Integer number for dividing in 2
    :param odd: Boolean flag for odd or even divition
    :return: Integer median number rounded up if odd
    """
    if odd:
        return number // 2 + 1
    else:
        return number // 2


def is_odd(number):
    """
    Determins if a number is odd or not.

    :param number: Integer number for determining odd or not
    :return: Boolean True if odd False if even
    """
    if (number % 2) == 0:
        return False
    else:
        return True


def main():
    """
    Main function of script asks for number of lines to include in the shape.
    """
    number = int(raw_input("Enter a number: "))
    print_shape(number)


if __name__ == "__main__":
    main()
