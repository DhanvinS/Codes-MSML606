from Problem3 import eval_postfix

def run_tests():

# jsut testing if my program can handle all the edge cases 
    print("Edge Cases test")

    # Empty input
    print("Empty input:", eval_postfix(""))

    # Insufficient operands
    try:
        eval_postfix("5 +")
    except ValueError as e:
        print("Insufficient operands caught:", e)

    # in case of too many operands
    try:
        eval_postfix("5 6 7 +")
    except ValueError as e:
        print("Too many operands caught:", e)

    # Division by zero
    try:
        eval_postfix("10 0 /")
    except ZeroDivisionError as e:
        print("Division by zero caught:", e)

    # Invalid token
    try:
        eval_postfix("5 a +")
    except ValueError as e:
        print("Invalid token caught:", e)

    # Very large numbers
    print("Large number test:",
          eval_postfix("1000000000 1000000000 *"))

    # Negative numbers
    print("Negative number test:",
          eval_postfix("-3 4 +"))


if __name__ == "__main__":
    run_tests()
